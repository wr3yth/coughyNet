// public/scripts/nav-effects.js

document.addEventListener("DOMContentLoaded", function () {
  var links = document.querySelectorAll("[data-nav-link]");

  links.forEach(function (link) {
    var wave = link.querySelector(".wave");
    if (!wave) return;

    var letters = wave.querySelectorAll(".wave-letter");
    if (!letters.length) return;

    // Store original characters once
    var originals = [];
    letters.forEach(function (l) {
      originals.push(l.textContent || "");
    });

    // ===========================
    // 🌊 HOVER WAVES
    // ===========================
    var waveRunId = 0;
    var hadEntered = false;

    function playWave(direction) {
      waveRunId++;
      var id = waveRunId;

      link.classList.remove("glitch-strong");
      wave.classList.remove("wave-active");
      wave.classList.remove("wave-reverse");

      // force reflow so animation restarts
      void wave.offsetWidth;

      if (direction === "forward") {
        wave.classList.add("wave-active");
      } else {
        wave.classList.add("wave-reverse");
      }

      var total = 800 + letters.length * 120;

      setTimeout(function () {
        if (waveRunId !== id) return; // a newer wave started
        wave.classList.remove("wave-active");
        wave.classList.remove("wave-reverse");
        link.classList.add("glitch-strong");
      }, total);
    }

    link.addEventListener("mouseenter", function () {
      hadEntered = true;
      playWave("forward");
    });

    link.addEventListener("mouseleave", function () {
      if (!hadEntered) return;
      hadEntered = false;
      playWave("reverse");
    });

    // ===========================
    // 🎰 SLOT MACHINE ON CLICK
    // ===========================
    link.addEventListener("click", function (e) {
      // only intercept simple left-clicks
      if (
        e.button !== 0 ||
        e.metaKey ||
        e.ctrlKey ||
        e.shiftKey ||
        e.altKey
      ) {
        return;
      }

      e.preventDefault(); // stop immediate navigation

      var alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
      var spins = 5;          // how many random chars per letter
      var frame = 70;         // ms between random chars
      var letterDelay = 80;   // stagger between letters

      letters.forEach(function (letter, index) {
        var original = originals[index] || "";
        var startDelay = index * letterDelay;
        var step = 0;

        setTimeout(function runStep() {
          if (step >= spins) {
            letter.textContent = original;
            return;
          }
          var randomIndex = Math.floor(Math.random() * alphabet.length);
          letter.textContent = alphabet.charAt(randomIndex);
          step++;
          setTimeout(runStep, frame);
        }, startDelay);
      });

      // total time until the last letter is done
      var totalDuration =
        (letters.length - 1) * letterDelay +
        spins * frame +
        80;

      var href = link.getAttribute("href");
      if (href) {
        setTimeout(function () {
          window.location.href = href;
        }, totalDuration);
      }
    });
  });
});
