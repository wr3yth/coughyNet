document.addEventListener("DOMContentLoaded", () => { 
  const hamburger =
    document.querySelector("[data-hamburger]") ||
    document.querySelector("button[aria-label='Menu']");

  const sidebar = document.querySelector("[data-sidebar]");
  const backdrop = document.querySelector("[data-sidebar-backdrop]");
  const utilityBg = document.querySelector("[data-utility-bg]");
  const modeWrapper = document.querySelector("[data-mode-wrapper]");
  const mainNav = document.querySelector("[data-main-nav]");

  if (!(hamburger && sidebar && backdrop && utilityBg && modeWrapper && mainNav)) {
    console.warn("[navbar.js] Missing one or more required elements.");
    return;
  }

  const navLinks = mainNav.querySelectorAll("a");

  // ==============================
  // SOCIAL BAR FETCH (async load)
  // ==============================
  let social = null;
  window.addEventListener("load", () => {
    social = document.querySelector("[data-social]") || document.getElementById("social");
  });


  // ==============================
  // HELPER FUNCTIONS
  // ==============================
  const computeShift = () => {
    const sidebarWidth = sidebar.offsetWidth || 300;
    return -(sidebarWidth / 2.4);
  };

  const moveSocialToSidebarCenter = () => {
    if (!social) return;

    const socialRect = social.getBoundingClientRect();
    const sidebarRect = sidebar.getBoundingClientRect();

    const deltaX =
      (sidebarRect.left + sidebarRect.width / 2) -
      (socialRect.left + socialRect.width / 2);

    const base = getComputedStyle(social).transform;
    social.style.transform = `${base === "none" ? "" : base} translateX(${deltaX}px)`;
  };

  const resetSocialPosition = () => {
    if (!social) return;
    social.style.transform = "";
  };

  const disableMainNavTabbing = () => {
    navLinks.forEach(link => {
      link.dataset.oldTabindex = link.getAttribute("tabindex") ?? "";
      link.setAttribute("tabindex", "-1");
    });
  };

  const enableMainNavTabbing = () => {
    navLinks.forEach(link => {
      const old = link.dataset.oldTabindex;
      if (old === "") link.removeAttribute("tabindex");
      else link.setAttribute("tabindex", old);
      delete link.dataset.oldTabindex;
    });
  };

  const disableMainNav = () => {
    disableMainNavTabbing();
    mainNav.setAttribute("aria-hidden", "true");
    mainNav.classList.add("nav-hidden");
  };

  const enableMainNav = () => {
    enableMainNavTabbing();
    mainNav.removeAttribute("aria-hidden");
    mainNav.classList.remove("nav-hidden");
  };


  // ==============================
  // SIDEBAR OPEN/CLOSE
  // ==============================
  const openSidebar = () => {
    sidebar.classList.remove("translate-x-full");
    sidebar.classList.add("translate-x-0");

    backdrop.classList.remove("opacity-0", "pointer-events-none");

    utilityBg.classList.add("fade-out", "expanded");

    sidebar.removeAttribute("inert");
    sidebar.setAttribute("aria-hidden", "false");

    const shift = computeShift();
    modeWrapper.style.transform = `translateX(${shift}px)`;

    disableMainNav();

    setTimeout(() => moveSocialToSidebarCenter(), 400);

    setTimeout(() => {
      const firstLink = sidebar.querySelector("a");
      if (firstLink) firstLink.focus();
    }, 300);

    document.dispatchEvent(new Event("sidebar:open"));
  };

  const closeSidebar = () => {
    sidebar.classList.add("translate-x-full");
    sidebar.classList.remove("translate-x-0");

    backdrop.classList.add("opacity-0", "pointer-events-none");

    utilityBg.classList.remove("fade-out", "expanded");

    sidebar.setAttribute("inert", "");
    sidebar.setAttribute("aria-hidden", "true");

    modeWrapper.style.transform = "";

    // only enable if screen is large
    if (window.innerWidth >= 768) enableMainNav();

    resetSocialPosition();

    document.dispatchEvent(new Event("sidebar:close"));
  };


  // ==============================
  // EVENT LISTENERS
  // ==============================
  hamburger.addEventListener("click", (e) => {
    e.stopPropagation();
    const isOpen = sidebar.classList.contains("translate-x-0");
    isOpen ? closeSidebar() : openSidebar();
  });

  backdrop.addEventListener("click", (e) => {
    if (e.target === backdrop) closeSidebar();
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeSidebar();
  });

  window.addEventListener("resize", () => {
    if (sidebar.classList.contains("translate-x-0")) {
      const shift = computeShift();
      modeWrapper.style.transform = `translateX(${shift}px)`;
      moveSocialToSidebarCenter();
    }
    applyResponsiveNavState();
  });


  // ==============================
  // RESPONSIVE NAV LOGIC
  // ==============================
  const applyResponsiveNavState = () => {
    if (window.innerWidth < 768) {
      disableMainNav();
    } else {
      // If sidebar is open → keep nav disabled
      if (!sidebar.classList.contains("translate-x-0")) {
        enableMainNav();
      }
    }
  };

  applyResponsiveNavState();
});
