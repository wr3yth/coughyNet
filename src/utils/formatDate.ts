export function formatDate(
  date: Date,
  lang: "en" | "fa" = "en",
  mode: "full" | "short" = "full"
) {
  if (!(date instanceof Date) || isNaN(date.getTime())) {
    return "";
  }

  if (lang === "fa") {
    // Persian (Jalali)
    return date.toLocaleDateString("fa-IR", {
      year: "numeric",
      month: mode === "full" ? "long" : "numeric",
      day: "numeric",
    });
  }

  // English (Gregorian)
  return date.toLocaleDateString("en-US", {
    year: "numeric",
    month: mode === "full" ? "long" : "short",
    day: "numeric",
  });
}
