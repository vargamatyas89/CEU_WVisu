/**
 * RiverRadar — EU GDPR (2016/679) & ePrivacy (2002/58/EC Art. 5(3)) Consent Manager
 *
 * Strictly enforces opt-in prior consent before writing optional localStorage preferences
 * or loading external third-party basemap tiles (OpenTopoMap / OpenStreetMap).
 * Zero tracking cookies, zero ads, zero third-party analytics.
 */

(() => {
  "use strict";

  const CONSENT_STORAGE_KEY = "riverradar_consent_v1";
  const CONSENT_VERSION = 1;
  const CONSENT_TTL_MS = 365 * 24 * 60 * 60 * 1000; // 12 months
  const OPTIONAL_STORAGE_KEYS = ["riverradar_lang", "riverradar_theme", "fluvio_lang", "wvis_lang"];

  let currentRecord = loadStoredConsent();
  let previewExternalBasemaps = null;

  function loadStoredConsent() {
    try {
      const raw = localStorage.getItem(CONSENT_STORAGE_KEY);
      if (!raw) return null;
      const parsed = JSON.parse(raw);
      if (
        !parsed ||
        parsed.v !== CONSENT_VERSION ||
        typeof parsed.expiresAt !== "number" ||
        Date.now() > parsed.expiresAt ||
        !parsed.categories
      ) {
        localStorage.removeItem(CONSENT_STORAGE_KEY);
        return null;
      }
      return {
        v: CONSENT_VERSION,
        decidedAt: parsed.decidedAt || new Date().toISOString(),
        expiresAt: parsed.expiresAt,
        categories: {
          necessary: true,
          preferences: Boolean(parsed.categories.preferences),
          externalBasemaps: Boolean(parsed.categories.externalBasemaps),
        },
      };
    } catch {
      return null;
    }
  }

  function purgeOptionalStorage() {
    try {
      for (const k of OPTIONAL_STORAGE_KEYS) {
        localStorage.removeItem(k);
      }
    } catch {
      // Ignore storage access restrictions
    }
  }

  function saveConsent(categories) {
    const now = Date.now();
    const clean = {
      necessary: true,
      preferences: Boolean(categories.preferences),
      externalBasemaps: Boolean(categories.externalBasemaps),
    };

    if (!clean.preferences) {
      purgeOptionalStorage();
    }

    currentRecord = {
      v: CONSENT_VERSION,
      decidedAt: new Date(now).toISOString(),
      expiresAt: now + CONSENT_TTL_MS,
      categories: clean,
    };

    try {
      localStorage.setItem(CONSENT_STORAGE_KEY, JSON.stringify(currentRecord));
    } catch {
      // Fall back to in-memory decision if storage is blocked
    }

    updateBannerVisibility();
    syncDialogInputs();

    window.dispatchEvent(
      new CustomEvent("riverradar:consent-changed", {
        detail: {
          decided: true,
          categories: { ...clean },
        },
      })
    );
  }

  function getCategories() {
    if (!currentRecord) {
      return {
        necessary: true,
        preferences: true,
        externalBasemaps: true,
      };
    }
    return { ...currentRecord.categories };
  }

  function allows(category) {
    if (category === "necessary") return true;
    if (category === "externalBasemaps" && previewExternalBasemaps !== null) {
      return previewExternalBasemaps;
    }
    return Boolean(getCategories()[category]);
  }

  function hasDecision() {
    return currentRecord !== null;
  }

  function updateBannerVisibility() {
    const banner = document.getElementById("cookie-banner");
    const dialog = document.getElementById("cookie-settings-dialog");
    if (!banner) return;
    banner.classList.toggle("hidden", hasDecision() || Boolean(dialog && dialog.open));
  }

  function syncDialogInputs() {
    const cats = getCategories();
    const prefInput = document.getElementById("consent-opt-preferences");
    const mapInput = document.getElementById("consent-opt-basemaps");
    if (prefInput) prefInput.checked = cats.preferences;
    if (mapInput) mapInput.checked = cats.externalBasemaps;
  }

  function openSettings() {
    const dialog = document.getElementById("cookie-settings-dialog");
    if (!dialog) return;
    previewExternalBasemaps = null;
    syncDialogInputs();
    if (!dialog.open) {
      if (typeof dialog.showModal === "function") {
        dialog.showModal();
      } else {
        dialog.setAttribute("open", "");
      }
    }
    updateBannerVisibility();
  }

  function initConsentUI() {
    const dialog = document.getElementById("cookie-settings-dialog");
    const btnAccept = document.getElementById("btn-cookie-accept");
    const btnReject = document.getElementById("btn-cookie-reject");
    const btnCustomize = document.getElementById("btn-cookie-customize");
    const btnReopen = document.getElementById("btn-cookie-settings");

    updateBannerVisibility();
    syncDialogInputs();

    if (btnAccept) {
      btnAccept.addEventListener("click", () => {
        saveConsent({ preferences: true, externalBasemaps: true });
      });
    }

    if (btnReject) {
      btnReject.addEventListener("click", () => {
        saveConsent({ preferences: false, externalBasemaps: false });
      });
    }

    if (btnCustomize) {
      btnCustomize.addEventListener("click", () => {
        openSettings();
      });
    }

    if (btnReopen) {
      btnReopen.addEventListener("click", () => {
        openSettings();
      });
    }

    // Live-switch background basemap as soon as the user toggles the map checkbox
    const mapInput = document.getElementById("consent-opt-basemaps");
    if (mapInput) {
      mapInput.addEventListener("change", () => {
        previewExternalBasemaps = mapInput.checked;
        window.dispatchEvent(
          new CustomEvent("riverradar:consent-changed", {
            detail: {
              decided: hasDecision(),
              preview: true,
              categories: {
                ...getCategories(),
                externalBasemaps: mapInput.checked,
              },
            },
          })
        );
      });
    }

    // Native <dialog> close handling (always reset returnValue to avoid stale state on Esc/light-dismiss)
    if (dialog) {
      dialog.addEventListener("close", () => {
        const action = dialog.returnValue;
        dialog.returnValue = "";
        previewExternalBasemaps = null;

        if (action === "accept-all") {
          saveConsent({ preferences: true, externalBasemaps: true });
        } else if (action === "reject-optional") {
          saveConsent({ preferences: false, externalBasemaps: false });
        } else if (action === "save") {
          const prefInput = document.getElementById("consent-opt-preferences");
          saveConsent({
            preferences: Boolean(prefInput && prefInput.checked),
            externalBasemaps: Boolean(mapInput && mapInput.checked),
          });
        } else {
          // Dismissed without saving — revert live map preview to stored/default state
          window.dispatchEvent(
            new CustomEvent("riverradar:consent-changed", {
              detail: {
                decided: hasDecision(),
                preview: true,
                categories: getCategories(),
              },
            })
          );
          updateBannerVisibility();
        }
      });

      // Fallback for browsers without native <dialog closedby="any"> support (e.g. Safari)
      if (!("closedBy" in HTMLDialogElement.prototype)) {
        const isOutside = (e) => {
          const r = dialog.getBoundingClientRect();
          return (
            e.clientX < r.left ||
            e.clientX > r.right ||
            e.clientY < r.top ||
            e.clientY > r.bottom
          );
        };
        let pressedOutside = false;
        dialog.addEventListener("pointerdown", (e) => {
          pressedOutside = isOutside(e);
        });
        dialog.addEventListener("pointerup", (e) => {
          if (pressedOutside && isOutside(e)) {
            dialog.returnValue = "";
            dialog.close();
          }
          pressedOutside = false;
        });
      }
    }

    // Ensure accessibility role fallback where native <input type="checkbox" switch> is unsupported
    if (!("switch" in HTMLInputElement.prototype)) {
      document.querySelectorAll('input[type="checkbox"][switch]').forEach((el) => {
        el.setAttribute("role", "switch");
      });
    }

    // Immediately pop up the GDPR modal on first visit (with all options checked by default)
    if (!hasDecision()) {
      openSettings();
    }
  }

  // Expose public consent API before app.js initializes
  window.RiverRadarConsent = {
    hasDecision,
    allows,
    getState: () => ({ decided: hasDecision(), categories: getCategories() }),
    openSettings,
    acceptAll: () => saveConsent({ preferences: true, externalBasemaps: true }),
    rejectOptional: () => saveConsent({ preferences: false, externalBasemaps: false }),
    saveCustom: saveConsent,
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initConsentUI);
  } else {
    initConsentUI();
  }
})();
