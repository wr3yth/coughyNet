# 📦 flatshot Project Snapshot

**Generated:** 2025-11-24 21:40:01

## raw structure
```
├── assets
│   └── backgrounds
│       ├── bwca-dusk.png
│       └── bwca-night.png
├── blog
│   ├── post-1.md
│   ├── post-2.md
│   ├── post-3.md
│   └── post-4.md
├── categoryMapFa.ts
├── components
│   ├── Astrogen.astro
│   ├── Background.astro
│   ├── BlogPost.astro
│   ├── BrandBadge.astro
│   ├── BrandBadgeWiki.astro
│   ├── Hamburger.astro
│   ├── Header.astro
│   ├── HeaderWiki.astro
│   ├── LangToggle.astro
│   ├── ModeToggle.astro
│   ├── Navbar.astro
│   ├── NavbarWiki.astro
│   ├── SidebarMenu.astro
│   ├── SocialBar.astro
│   ├── UtilityBar.astro
│   ├── Welcome.astro
│   └── WikiTree.astro
├── content.config.ts
├── data
│   └── nav.ts
├── layouts
│   ├── BaseLayout.astro
│   ├── FictionLayout.astro
│   ├── FictionLayoutFa.astro
│   ├── Layout.astro
│   ├── LayoutWiki.astro
│   ├── MarkdownPostLayout.astro
│   └── PoetryLayout.astro
├── lib
│   └── utils.ts
├── pages
│   ├── LightMeNow.html
│   ├── about.astro
│   ├── animation.astro
│   ├── art.astro
│   ├── blog.astro
│   ├── fa
│   │   ├── about.astro
│   │   ├── art.astro
│   │   ├── blog.astro
│   │   ├── index.astro
│   │   ├── literature.astro
│   │   ├── partners.astro
│   │   ├── poems
│   │   │   ├── [id].astro
│   │   │   └── index.astro
│   │   ├── projects.astro
│   │   ├── research
│   │   │   └── index.astro
│   │   ├── stories
│   │   │   ├── [id].astro
│   │   │   └── index.astro
│   │   └── wiki
│   │       ├── [id].astro
│   │       ├── about.astro
│   │       ├── effects.astro
│   │       ├── harm_reduction.astro
│   │       ├── index.astro
│   │       ├── interactions.astro
│   │       ├── reports.astro
│   │       └── substances.astro
│   ├── index.astro
│   ├── literature
│   │   └── index.astro
│   ├── partners.astro
│   ├── poems
│   │   ├── [id].astro
│   │   └── index.astro
│   ├── posts
│   │   └── [...slug].astro
│   ├── projects.astro
│   ├── research
│   │   └── index.astro
│   ├── rss.xml.js
│   ├── stories
│   │   ├── [id].astro
│   │   └── index.astro
│   ├── tags
│   │   ├── [tag].astro
│   │   └── index.astro
│   └── wiki
│       ├── [id].astro
│       ├── about.astro
│       ├── effects.astro
│       ├── harm_reduction.astro
│       ├── index.astro
│       ├── interactions.astro
│       ├── psychoactives.astro
│       └── reports.astro
├── poems
│   ├── Sum Things Up.md
│   └── Violent Bloom.md
├── stories
│   ├── cry_as_punishment.md
│   └── make love, not with eggs.md
├── stories-fa
│   ├── bedoone_khodahafezi.md
│   ├── khianat_va_mokafat.md
│   ├── tasmim_baraye_cobra_11.md
│   ├── vincenzo.md
│   ├── اثاثیاست یک دست میز و صندلی نگران.md
│   └── محل تبلیغات شما.md
├── styles
│   └── global.css
├── types
│   └── wiki.ts
├── utils
│   └── formatDate.ts
└── wiki
    ├── Neurotransmitters
    │   ├── acetylcholine.fa.md
    │   ├── acetylcholine.md
    │   ├── amino-acids.fa.md
    │   ├── amino-acids.md
    │   ├── aminobutyric-acid.fa.md
    │   ├── aminobutyric-acid.md
    │   ├── catecholamines.fa.md
    │   ├── catecholamines.md
    │   ├── dopamine.fa.md
    │   ├── dopamine.md
    │   ├── epinephrine.fa.md
    │   ├── epinephrine.md
    │   ├── histamine.fa.md
    │   ├── histamine.md
    │   ├── l-glutamate.fa.md
    │   ├── l-glutamate.md
    │   ├── melatonin.fa.md
    │   ├── melatonin.md
    │   ├── monoamines.fa.md
    │   ├── monoamines.md
    │   ├── neurotransmitters.fa.md
    │   ├── neurotransmitters.md
    │   ├── norepinephrine.fa.md
    │   ├── norepinephrine.md
    │   ├── other.fa.md
    │   ├── other.md
    │   ├── peptides.fa.md
    │   ├── peptides.md
    │   ├── phenethylamine.fa.md
    │   ├── phenethylamine.md
    │   ├── phenethylamines.fa.md
    │   ├── phenethylamines.md
    │   ├── semax.fa.md
    │   ├── semax.md
    │   ├── serotonin.fa.md
    │   ├── serotonin.md
    │   ├── trace-amines.fa.md
    │   ├── trace-amines.md
    │   ├── tryptamine.fa.md
    │   └── tryptamine.md
    ├── Psychoactive_Effects
    │   ├── Cognitive_effects
    │   │   ├── Cognitive_effects.fa.md
    │   │   ├── Cognitive_effects.md
    │   │   ├── Disconnective_effects
    │   │   │   ├── cognitive-disconnection.fa.md
    │   │   │   ├── cognitive-disconnection.md
    │   │   │   ├── detachment-plateaus.fa.md
    │   │   │   ├── detachment-plateaus.md
    │   │   │   ├── disconnective-effects.fa.md
    │   │   │   ├── disconnective-effects.md
    │   │   │   ├── dj-vu.fa.md
    │   │   │   ├── dj-vu.md
    │   │   │   ├── holes-spaces-and-voids.fa.md
    │   │   │   ├── holes-spaces-and-voids.md
    │   │   │   ├── physical-disconnection.fa.md
    │   │   │   ├── physical-disconnection.md
    │   │   │   ├── structures.fa.md
    │   │   │   ├── structures.md
    │   │   │   ├── visual-disconnection.fa.md
    │   │   │   └── visual-disconnection.md
    │   │   ├── addiction-suppression.fa.md
    │   │   ├── addiction-suppression.md
    │   │   ├── amnesia copy.md
    │   │   ├── amnesia.fa copy.md
    │   │   ├── amnesia.fa.md
    │   │   ├── amnesia.md
    │   │   ├── analysis-depression.fa.md
    │   │   ├── analysis-depression.md
    │   │   ├── analysis-enhancement.fa.md
    │   │   ├── analysis-enhancement.md
    │   │   ├── anhedonia.fa.md
    │   │   ├── anhedonia.md
    │   │   ├── anxiety-suppression.fa.md
    │   │   ├── anxiety-suppression.md
    │   │   ├── anxiety.fa.md
    │   │   ├── anxiety.md
    │   │   ├── atemporality.fa.md
    │   │   ├── atemporality.md
    │   │   ├── catharsis.fa.md
    │   │   ├── catharsis.md
    │   │   ├── cognitive-dysphoria.fa.md
    │   │   ├── cognitive-dysphoria.md
    │   │   ├── cognitive-effects.fa.md
    │   │   ├── cognitive-effects.md
    │   │   ├── cognitive-euphoria.fa.md
    │   │   ├── cognitive-euphoria.md
    │   │   ├── cognitive-fatigue.fa.md
    │   │   ├── cognitive-fatigue.md
    │   │   ├── compulsive-redosing.fa.md
    │   │   ├── compulsive-redosing.md
    │   │   ├── conceptual-thinking.fa.md
    │   │   ├── conceptual-thinking.md
    │   │   ├── confusion.fa.md
    │   │   ├── confusion.md
    │   │   ├── creativity-depression.fa.md
    │   │   ├── creativity-depression.md
    │   │   ├── creativity-enhancement.fa.md
    │   │   ├── creativity-enhancement.md
    │   │   ├── delirium.fa.md
    │   │   ├── delirium.md
    │   │   ├── delusions.fa.md
    │   │   ├── delusions.md
    │   │   ├── depersonalization.fa.md
    │   │   ├── depersonalization.md
    │   │   ├── depression-reduction.fa.md
    │   │   ├── depression-reduction.md
    │   │   ├── depression.fa.md
    │   │   ├── depression.md
    │   │   ├── depressions.fa.md
    │   │   ├── depressions.md
    │   │   ├── derealization.fa.md
    │   │   ├── derealization.md
    │   │   ├── disinhibition.fa.md
    │   │   ├── disinhibition.md
    │   │   ├── dream-potentiation.fa.md
    │   │   ├── dream-potentiation.md
    │   │   ├── dream-suppression.fa.md
    │   │   ├── dream-suppression.md
    │   │   ├── ego-dissolution.fa.md
    │   │   ├── ego-dissolution.md
    │   │   ├── ego-inflation.fa.md
    │   │   ├── ego-inflation.md
    │   │   ├── ego-replacement.fa.md
    │   │   ├── ego-replacement.md
    │   │   ├── emotion-intensification.fa.md
    │   │   ├── emotion-intensification.md
    │   │   ├── emotion-suppression.fa.md
    │   │   ├── emotion-suppression.md
    │   │   ├── empathy-affection-and-sociability-enhancement.fa.md
    │   │   ├── empathy-affection-and-sociability-enhancement.md
    │   │   ├── enhancements.fa.md
    │   │   ├── enhancements.md
    │   │   ├── euthymia.fa.md
    │   │   ├── euthymia.md
    │   │   ├── existential-self-realization.fa.md
    │   │   ├── existential-self-realization.md
    │   │   ├── feelings-of-impending-doom.fa.md
    │   │   ├── feelings-of-impending-doom.md
    │   │   ├── focus-intensification.fa.md
    │   │   ├── focus-intensification.md
    │   │   ├── focus-suppression.fa.md
    │   │   ├── focus-suppression.md
    │   │   ├── glossolalia.fa.md
    │   │   ├── glossolalia.md
    │   │   ├── identity-alteration.fa.md
    │   │   ├── identity-alteration.md
    │   │   ├── immersion-intensification.fa.md
    │   │   ├── immersion-intensification.md
    │   │   ├── increased-introspection.fa.md
    │   │   ├── increased-introspection.md
    │   │   ├── increased-music-appreciation.fa.md
    │   │   ├── increased-music-appreciation.md
    │   │   ├── increased-sense-of-humor.fa.md
    │   │   ├── increased-sense-of-humor.md
    │   │   ├── intensifications.fa.md
    │   │   ├── intensifications.md
    │   │   ├── irritability.fa.md
    │   │   ├── irritability.md
    │   │   ├── language-depression.fa.md
    │   │   ├── language-depression.md
    │   │   ├── mania.fa.md
    │   │   ├── mania.md
    │   │   ├── memory-enhancement.fa.md
    │   │   ├── memory-enhancement.md
    │   │   ├── memory-suppression.fa.md
    │   │   ├── memory-suppression.md
    │   │   ├── mindfulness.fa.md
    │   │   ├── mindfulness.md
    │   │   ├── motivation-depression.fa.md
    │   │   ├── motivation-depression.md
    │   │   ├── motivation-enhancement.fa.md
    │   │   ├── motivation-enhancement.md
    │   │   ├── multiple-thought-streams.fa.md
    │   │   ├── multiple-thought-streams.md
    │   │   ├── no-umbrella-reviews-done-below-this-line.fa.md
    │   │   ├── no-umbrella-reviews-done-below-this-line.md
    │   │   ├── novel.fa.md
    │   │   ├── novel.md
    │   │   ├── novelty-enhancement.fa.md
    │   │   ├── novelty-enhancement.md
    │   │   ├── panic-attack.fa.md
    │   │   ├── panic-attack.md
    │   │   ├── paranoia.fa.md
    │   │   ├── paranoia.md
    │   │   ├── perceived-exposure-to-inner-mechanics-of-consciousness.fa.md
    │   │   ├── perceived-exposure-to-inner-mechanics-of-consciousness.md
    │   │   ├── perception-of-eternalism.fa.md
    │   │   ├── perception-of-eternalism.md
    │   │   ├── perception-of-interdependent-opposites.fa.md
    │   │   ├── perception-of-interdependent-opposites.md
    │   │   ├── perception-of-predeterminism.fa.md
    │   │   ├── perception-of-predeterminism.md
    │   │   ├── perception-of-self-design.fa.md
    │   │   ├── perception-of-self-design.md
    │   │   ├── personal-bias-suppression.fa.md
    │   │   ├── personal-bias-suppression.md
    │   │   ├── personal-meaning-intensification.fa.md
    │   │   ├── personal-meaning-intensification.md
    │   │   ├── personality-regression.fa.md
    │   │   ├── personality-regression.md
    │   │   ├── psychological.fa.md
    │   │   ├── psychological.md
    │   │   ├── psychosis.fa.md
    │   │   ├── psychosis.md
    │   │   ├── rejuvenation.fa.md
    │   │   ├── rejuvenation.md
    │   │   ├── simultaneous-emotions.fa.md
    │   │   ├── simultaneous-emotions.md
    │   │   ├── sleepiness.fa.md
    │   │   ├── sleepiness.md
    │   │   ├── sociability-depression.fa.md
    │   │   ├── sociability-depression.md
    │   │   ├── spirituality-intensification.fa.md
    │   │   ├── spirituality-intensification.md
    │   │   ├── suggestibility-intensification.fa.md
    │   │   ├── suggestibility-intensification.md
    │   │   ├── suggestibility-suppression.fa.md
    │   │   ├── suggestibility-suppression.md
    │   │   ├── suicidal-ideation.fa.md
    │   │   ├── suicidal-ideation.md
    │   │   ├── thought-acceleration.fa.md
    │   │   ├── thought-acceleration.md
    │   │   ├── thought-connectivity.fa.md
    │   │   ├── thought-connectivity.md
    │   │   ├── thought-deceleration.fa.md
    │   │   ├── thought-deceleration.md
    │   │   ├── thought-disorganization.fa.md
    │   │   ├── thought-disorganization.md
    │   │   ├── thought-loop.fa.md
    │   │   ├── thought-loop.md
    │   │   ├── thought-organization.fa.md
    │   │   ├── thought-organization.md
    │   │   ├── time-compression.fa.md
    │   │   ├── time-compression.md
    │   │   ├── time-dilation.fa.md
    │   │   ├── time-dilation.md
    │   │   ├── time-distortion.fa.md
    │   │   ├── time-distortion.md
    │   │   ├── time-reversal.fa.md
    │   │   ├── time-reversal.md
    │   │   ├── transpersonal.fa.md
    │   │   ├── transpersonal.md
    │   │   ├── unity-and-interconnectedness.fa.md
    │   │   ├── unity-and-interconnectedness.md
    │   │   ├── wakefulness copy.md
    │   │   ├── wakefulness.fa copy.md
    │   │   ├── wakefulness.fa.md
    │   │   └── wakefulness.md
    │   ├── Physical_effects
    │   │   ├── Gustatory_and_olfactory_effects
    │   │   │   ├── gustatory-and-olfactory-effects.fa.md
    │   │   │   ├── gustatory-and-olfactory-effects.md
    │   │   │   ├── gustatory-depression.fa.md
    │   │   │   ├── gustatory-depression.md
    │   │   │   ├── gustatory-hallucination.fa.md
    │   │   │   ├── gustatory-hallucination.md
    │   │   │   ├── gustatory-intensification.fa.md
    │   │   │   ├── gustatory-intensification.md
    │   │   │   ├── olfactory-depression.fa.md
    │   │   │   ├── olfactory-depression.md
    │   │   │   ├── olfactory-hallucination.fa.md
    │   │   │   ├── olfactory-hallucination.md
    │   │   │   ├── olfactory-intensification.fa.md
    │   │   │   └── olfactory-intensification.md
    │   │   ├── Uncomfortable physical effects
    │   │   │   ├── abnormal-heartbeat.fa.md
    │   │   │   ├── abnormal-heartbeat.md
    │   │   │   ├── back-pain.fa.md
    │   │   │   ├── back-pain.md
    │   │   │   ├── bodily-pressures.fa.md
    │   │   │   ├── bodily-pressures.md
    │   │   │   ├── bodily.fa.md
    │   │   │   ├── bodily.md
    │   │   │   ├── brain-zaps.fa.md
    │   │   │   ├── brain-zaps.md
    │   │   │   ├── cardiovascular.fa.md
    │   │   │   ├── cardiovascular.md
    │   │   │   ├── cerebrovascular.fa.md
    │   │   │   ├── cerebrovascular.md
    │   │   │   ├── constipation.fa.md
    │   │   │   ├── constipation.md
    │   │   │   ├── decreased-blood-pressure.fa.md
    │   │   │   ├── decreased-blood-pressure.md
    │   │   │   ├── decreased-heart-rate.fa.md
    │   │   │   ├── decreased-heart-rate.md
    │   │   │   ├── dehydration.fa.md
    │   │   │   ├── dehydration.md
    │   │   │   ├── diarrhea.fa.md
    │   │   │   ├── diarrhea.md
    │   │   │   ├── difficulty-urinating.fa.md
    │   │   │   ├── difficulty-urinating.md
    │   │   │   ├── dizziness.fa.md
    │   │   │   ├── dizziness.md
    │   │   │   ├── dry-mouth.fa.md
    │   │   │   ├── dry-mouth.md
    │   │   │   ├── frequent-urination.fa.md
    │   │   │   ├── frequent-urination.md
    │   │   │   ├── headache.fa.md
    │   │   │   ├── headache.md
    │   │   │   ├── increased-blood-pressure.fa.md
    │   │   │   ├── increased-blood-pressure.md
    │   │   │   ├── increased-bodily-temperature.fa.md
    │   │   │   ├── increased-bodily-temperature.md
    │   │   │   ├── increased-heart-rate.fa.md
    │   │   │   ├── increased-heart-rate.md
    │   │   │   ├── increased-perspiration.fa.md
    │   │   │   ├── increased-perspiration.md
    │   │   │   ├── increased-phlegm-production.fa.md
    │   │   │   ├── increased-phlegm-production.md
    │   │   │   ├── itchiness.fa.md
    │   │   │   ├── itchiness.md
    │   │   │   ├── muscle-contractions.fa.md
    │   │   │   ├── muscle-contractions.md
    │   │   │   ├── muscle-cramps.fa.md
    │   │   │   ├── muscle-cramps.md
    │   │   │   ├── muscle-tension.fa.md
    │   │   │   ├── muscle-tension.md
    │   │   │   ├── muscle-twitching.fa.md
    │   │   │   ├── muscle-twitching.md
    │   │   │   ├── nausea.fa.md
    │   │   │   ├── nausea.md
    │   │   │   ├── optical-sliding.fa.md
    │   │   │   ├── optical-sliding.md
    │   │   │   ├── photophobia.fa.md
    │   │   │   ├── photophobia.md
    │   │   │   ├── physical-fatigue.fa.md
    │   │   │   ├── physical-fatigue.md
    │   │   │   ├── respiratory-depression.fa.md
    │   │   │   ├── respiratory-depression.md
    │   │   │   ├── restless-legs.fa.md
    │   │   │   ├── restless-legs.md
    │   │   │   ├── runny-nose.fa.md
    │   │   │   ├── runny-nose.md
    │   │   │   ├── seizure.fa.md
    │   │   │   ├── seizure.md
    │   │   │   ├── skin-flushing.fa.md
    │   │   │   ├── skin-flushing.md
    │   │   │   ├── stomach-bloating.fa.md
    │   │   │   ├── stomach-bloating.md
    │   │   │   ├── stomach-cramp.fa.md
    │   │   │   ├── stomach-cramp.md
    │   │   │   ├── teeth-grinding.fa.md
    │   │   │   ├── teeth-grinding.md
    │   │   │   ├── temperature-regulation-suppression.fa.md
    │   │   │   ├── temperature-regulation-suppression.md
    │   │   │   ├── temporary-erectile-dysfunction.fa.md
    │   │   │   ├── temporary-erectile-dysfunction.md
    │   │   │   ├── uncomfortable-physical-effects.fa.md
    │   │   │   ├── uncomfortable-physical-effects.md
    │   │   │   ├── vasoconstriction.fa.md
    │   │   │   ├── vasoconstriction.md
    │   │   │   ├── vasodilation.fa.md
    │   │   │   ├── vasodilation.md
    │   │   │   ├── vibrating-vision.fa.md
    │   │   │   ├── vibrating-vision.md
    │   │   │   ├── vomiting.fa.md
    │   │   │   ├── vomiting.md
    │   │   │   ├── wate.fa.md
    │   │   │   └── wate.md
    │   │   ├── alterations.fa.md
    │   │   ├── alterations.md
    │   │   ├── amplifications.fa.md
    │   │   ├── amplifications.md
    │   │   ├── appetite-intensification.fa.md
    │   │   ├── appetite-intensification.md
    │   │   ├── appetite-suppression.fa.md
    │   │   ├── appetite-suppression.md
    │   │   ├── bodily-control-enhancement.fa.md
    │   │   ├── bodily-control-enhancement.md
    │   │   ├── body-odor-alteration.fa.md
    │   │   ├── body-odor-alteration.md
    │   │   ├── bronchodilation.fa.md
    │   │   ├── bronchodilation.md
    │   │   ├── changes-in-felt-bodily-form.fa.md
    │   │   ├── changes-in-felt-bodily-form.md
    │   │   ├── changes-in-felt-gravity.fa.md
    │   │   ├── changes-in-felt-gravity.md
    │   │   ├── cough-suppression.fa.md
    │   │   ├── cough-suppression.md
    │   │   ├── decreased-libido.fa.md
    │   │   ├── decreased-libido.md
    │   │   ├── excessive-yawning.fa.md
    │   │   ├── excessive-yawning.md
    │   │   ├── increased-libido.fa.md
    │   │   ├── increased-libido.md
    │   │   ├── increased-respiration.fa.md
    │   │   ├── increased-respiration.md
    │   │   ├── increased-salivation.fa.md
    │   │   ├── increased-salivation.md
    │   │   ├── laughter-fits.fa.md
    │   │   ├── laughter-fits.md
    │   │   ├── motor-control-loss.fa.md
    │   │   ├── motor-control-loss.md
    │   │   ├── mouth-numbing.fa.md
    │   │   ├── mouth-numbing.md
    │   │   ├── muscle-relaxation.fa.md
    │   │   ├── muscle-relaxation.md
    │   │   ├── nausea-suppression.fa.md
    │   │   ├── nausea-suppression.md
    │   │   ├── orgasm-depression.fa.md
    │   │   ├── orgasm-depression.md
    │   │   ├── pain-relief.fa.md
    │   │   ├── pain-relief.md
    │   │   ├── perception-of-bodily-heaviness.fa.md
    │   │   ├── perception-of-bodily-heaviness.md
    │   │   ├── perception-of-bodily-lightness.fa.md
    │   │   ├── perception-of-bodily-lightness.md
    │   │   ├── physical-autonomy.fa.md
    │   │   ├── physical-autonomy.md
    │   │   ├── physical-effects.fa.md
    │   │   ├── physical-effects.md
    │   │   ├── physical-euphoria.fa.md
    │   │   ├── physical-euphoria.md
    │   │   ├── pupil-constriction.fa.md
    │   │   ├── pupil-constriction.md
    │   │   ├── pupil-dilation.fa.md
    │   │   ├── pupil-dilation.md
    │   │   ├── sedation.fa.md
    │   │   ├── sedation.md
    │   │   ├── seizure-suppression.fa.md
    │   │   ├── seizure-suppression.md
    │   │   ├── stamina-intensification.fa.md
    │   │   ├── stamina-intensification.md
    │   │   ├── stimulation.fa.md
    │   │   ├── stimulation.md
    │   │   ├── suppressions.fa.md
    │   │   └── suppressions.md
    │   ├── Psychoactive_effects.fa.md
    │   ├── Psychoactive_effects.md
    │   └── Sensory_effects
    │       ├── Auditory_effects
    │       │   ├── auditory-acuity-enhancement.fa.md
    │       │   ├── auditory-acuity-enhancement.md
    │       │   ├── auditory-acuity-suppression.fa.md
    │       │   ├── auditory-acuity-suppression.md
    │       │   ├── auditory-distortion.fa.md
    │       │   ├── auditory-distortion.md
    │       │   ├── auditory-effects.fa.md
    │       │   ├── auditory-effects.md
    │       │   ├── auditory-hallucination.fa.md
    │       │   ├── auditory-hallucination.md
    │       │   ├── auditory-misinterpretation.fa.md
    │       │   ├── auditory-misinterpretation.md
    │       │   ├── autonomous-voice-communication.fa.md
    │       │   ├── autonomous-voice-communication.md
    │       │   ├── external-auditory-hallucination.fa.md
    │       │   ├── external-auditory-hallucination.md
    │       │   ├── internal-auditory-hallucination.fa.md
    │       │   ├── internal-auditory-hallucination.md
    │       │   ├── temporal-scaling.fa.md
    │       │   └── temporal-scaling.md
    │       ├── Multisensory_effects
    │       │   ├── anticipatory-response.fa.md
    │       │   ├── anticipatory-response.md
    │       │   ├── component-controllability.fa.md
    │       │   ├── component-controllability.md
    │       │   ├── dosage-independent-intensity.fa.md
    │       │   ├── dosage-independent-intensity.md
    │       │   ├── machinescapes.fa.md
    │       │   ├── machinescapes.md
    │       │   ├── memory-replays.fa.md
    │       │   ├── memory-replays.md
    │       │   ├── multisensory-effects.fa.md
    │       │   ├── multisensory-effects.md
    │       │   ├── scenarios-and-plots.fa.md
    │       │   ├── scenarios-and-plots.md
    │       │   ├── spatial-disorientation.fa.md
    │       │   ├── spatial-disorientation.md
    │       │   ├── spontaneous-physical-movements.fa.md
    │       │   ├── spontaneous-physical-movements.md
    │       │   ├── synaesthesia.fa.md
    │       │   └── synaesthesia.md
    │       ├── Sensory_effects.fa.md
    │       ├── Sensory_effects.md
    │       ├── Tactile_effects
    │       │   ├── spontaneous-bodily-sensations.fa.md
    │       │   ├── spontaneous-bodily-sensations.md
    │       │   ├── tactile-effects.fa.md
    │       │   ├── tactile-effects.md
    │       │   ├── tactile-hallucination.fa.md
    │       │   ├── tactile-hallucination.md
    │       │   ├── tactile-intensification.fa.md
    │       │   ├── tactile-intensification.md
    │       │   ├── tactile-suppression.fa.md
    │       │   └── tactile-suppression.md
    │       └── Visual_effects
    │           ├── 8a-perceived-exposure-to-semantic-concept-network.fa.md
    │           ├── 8a-perceived-exposure-to-semantic-concept-network.md
    │           ├── 8b-perceived-exposure-to-inner-mechanics-of-consciousness.fa.md
    │           ├── 8b-perceived-exposure-to-inner-mechanics-of-consciousness.md
    │           ├── after-images.fa.md
    │           ├── after-images.md
    │           ├── autonomous-entity.fa.md
    │           ├── autonomous-entity.md
    │           ├── breathing.fa.md
    │           ├── breathing.md
    │           ├── brightness-alteration.fa.md
    │           ├── brightness-alteration.md
    │           ├── color-depression.fa.md
    │           ├── color-depression.md
    │           ├── color-enhancement.fa.md
    │           ├── color-enhancement.md
    │           ├── color-replacement.fa.md
    │           ├── color-replacement.md
    │           ├── color-shifting.fa.md
    │           ├── color-shifting.md
    │           ├── color-tinting.fa.md
    │           ├── color-tinting.md
    │           ├── depth-perception-distortions.fa.md
    │           ├── depth-perception-distortions.md
    │           ├── diffraction.fa.md
    │           ├── diffraction.md
    │           ├── distortions.fa.md
    │           ├── distortions.md
    │           ├── double-vision.fa.md
    │           ├── double-vision.md
    │           ├── drifting.fa.md
    │           ├── drifting.md
    │           ├── environmental-cubism.fa.md
    │           ├── environmental-cubism.md
    │           ├── environmental-orbism.fa.md
    │           ├── environmental-orbism.md
    │           ├── environmental-patterning.fa.md
    │           ├── environmental-patterning.md
    │           ├── external-hallucination.fa.md
    │           ├── external-hallucination.md
    │           ├── flowing.fa.md
    │           ├── flowing.md
    │           ├── geometry.fa.md
    │           ├── geometry.md
    │           ├── hallucinatory-states.fa.md
    │           ├── hallucinatory-states.md
    │           ├── internal-hallucination.fa.md
    │           ├── internal-hallucination.md
    │           ├── magnification.fa.md
    │           ├── magnification.md
    │           ├── melting.fa.md
    │           ├── melting.md
    │           ├── morphing.fa.md
    │           ├── morphing.md
    │           ├── object-activation.fa.md
    │           ├── object-activation.md
    │           ├── object-alteration.fa.md
    │           ├── object-alteration.md
    │           ├── pattern-recognition-enhancement.fa.md
    │           ├── pattern-recognition-enhancement.md
    │           ├── pattern-recognition-suppression.fa.md
    │           ├── pattern-recognition-suppression.md
    │           ├── peripheral-information-misinterpretation.fa.md
    │           ├── peripheral-information-misinterpretation.md
    │           ├── perspective-distortion.fa.md
    │           ├── perspective-distortion.md
    │           ├── perspective-hallucination.fa.md
    │           ├── perspective-hallucination.md
    │           ├── recursion.fa.md
    │           ├── recursion.md
    │           ├── scenery-slicing.fa.md
    │           ├── scenery-slicing.md
    │           ├── settings-sceneries-and-landscapes.fa.md
    │           ├── settings-sceneries-and-landscapes.md
    │           ├── shadow-people.fa.md
    │           ├── shadow-people.md
    │           ├── symmetrical-texture-repetition.fa.md
    │           ├── symmetrical-texture-repetition.md
    │           ├── texture-liquidation.fa.md
    │           ├── texture-liquidation.md
    │           ├── tracers.fa.md
    │           ├── tracers.md
    │           ├── transformations.fa.md
    │           ├── transformations.md
    │           ├── unspeakable-horrors.fa.md
    │           ├── unspeakable-horrors.md
    │           ├── visual-acuity-enhancement.fa.md
    │           ├── visual-acuity-enhancement.md
    │           ├── visual-acuity-suppression.fa.md
    │           ├── visual-acuity-suppression.md
    │           ├── visual-effects.fa.md
    │           ├── visual-effects.md
    │           ├── visual-flipping.fa.md
    │           ├── visual-flipping.md
    │           ├── visual-haze.fa.md
    │           ├── visual-haze.md
    │           ├── visual-processing-acceleration.fa.md
    │           ├── visual-processing-acceleration.md
    │           ├── visual-processing-deceleration.fa.md
    │           ├── visual-processing-deceleration.md
    │           ├── visual-stretching.fa.md
    │           └── visual-stretching.md
    └── Psychoactives
        ├── Depressants
        │   ├── 14-butanediol.fa.md
        │   ├── 14-butanediol.md
        │   ├── 2-methyl-2-butanol.fa.md
        │   ├── 2-methyl-2-butanol.md
        │   ├── 7-hydroxymitragynine.fa.md
        │   ├── 7-hydroxymitragynine.md
        │   ├── acetylfentanyl.fa.md
        │   ├── acetylfentanyl.md
        │   ├── alcohol.fa.md
        │   ├── alcohol.md
        │   ├── alcohols.fa.md
        │   ├── alcohols.md
        │   ├── alprazolam.fa.md
        │   ├── alprazolam.md
        │   ├── baclofen.fa.md
        │   ├── baclofen.md
        │   ├── barbiturates.fa.md
        │   ├── barbiturates.md
        │   ├── benzodiazepines.fa.md
        │   ├── benzodiazepines.md
        │   ├── bromazepam.fa.md
        │   ├── bromazepam.md
        │   ├── buprenorphine.fa.md
        │   ├── buprenorphine.md
        │   ├── carisoprodol.fa.md
        │   ├── carisoprodol.md
        │   ├── clonazepam.fa.md
        │   ├── clonazepam.md
        │   ├── clonazolam.fa.md
        │   ├── clonazolam.md
        │   ├── clonidine.fa.md
        │   ├── clonidine.md
        │   ├── codeine.fa.md
        │   ├── codeine.md
        │   ├── depressants.fa.md
        │   ├── depressants.md
        │   ├── deschloroetizolam.fa.md
        │   ├── deschloroetizolam.md
        │   ├── desomorphine.fa.md
        │   ├── desomorphine.md
        │   ├── dextropropoxyphene.fa.md
        │   ├── dextropropoxyphene.md
        │   ├── diacetylmorphine.fa.md
        │   ├── diacetylmorphine.md
        │   ├── diazepam.fa.md
        │   ├── diazepam.md
        │   ├── diclazepam.fa.md
        │   ├── diclazepam.md
        │   ├── dihydrocodeine.fa.md
        │   ├── dihydrocodeine.md
        │   ├── diphenhydramine.fa.md
        │   ├── diphenhydramine.md
        │   ├── eszopiclone.fa.md
        │   ├── eszopiclone.md
        │   ├── ethylmorphine.fa.md
        │   ├── ethylmorphine.md
        │   ├── etizolam.fa.md
        │   ├── etizolam.md
        │   ├── f-phenibut.fa.md
        │   ├── f-phenibut.md
        │   ├── fentanyl.fa.md
        │   ├── fentanyl.md
        │   ├── flualprazolam.fa.md
        │   ├── flualprazolam.md
        │   ├── flubromazepam.fa.md
        │   ├── flubromazepam.md
        │   ├── flubromazolam.fa.md
        │   ├── flubromazolam.md
        │   ├── flunitrazepam.fa.md
        │   ├── flunitrazepam.md
        │   ├── flunitrazolam.fa.md
        │   ├── flunitrazolam.md
        │   ├── gabaa-1-agonists.fa.md
        │   ├── gabaa-1-agonists.md
        │   ├── gabapentin.fa.md
        │   ├── gabapentin.md
        │   ├── gabapentinoids.fa.md
        │   ├── gabapentinoids.md
        │   ├── gaboxadol.fa.md
        │   ├── gaboxadol.md
        │   ├── gbl.fa.md
        │   ├── gbl.md
        │   ├── ghb.fa.md
        │   ├── ghb.md
        │   ├── hydrocodone.fa.md
        │   ├── hydrocodone.md
        │   ├── hydromorphone.fa.md
        │   ├── hydromorphone.md
        │   ├── ibotenic-acid.fa.md
        │   ├── ibotenic-acid.md
        │   ├── kava.fa.md
        │   ├── kava.md
        │   ├── kratom.fa.md
        │   ├── kratom.md
        │   ├── lorazepam.fa.md
        │   ├── lorazepam.md
        │   ├── lormetazepam.fa.md
        │   ├── lormetazepam.md
        │   ├── methadone.fa.md
        │   ├── methadone.md
        │   ├── methaqualone.fa.md
        │   ├── methaqualone.md
        │   ├── metizolam.fa.md
        │   ├── metizolam.md
        │   ├── midazolam.fa.md
        │   ├── midazolam.md
        │   ├── mirtazapine.fa.md
        │   ├── mirtazapine.md
        │   ├── morphine.fa.md
        │   ├── morphine.md
        │   ├── muscimol.fa.md
        │   ├── muscimol.md
        │   ├── nifoxipam.fa.md
        │   ├── nifoxipam.md
        │   ├── nitromethaqualone.fa.md
        │   ├── nitromethaqualone.md
        │   ├── o-desmethyltramadol.fa.md
        │   ├── o-desmethyltramadol.md
        │   ├── opioids.fa.md
        │   ├── opioids.md
        │   ├── other-gabaergics.fa.md
        │   ├── other-gabaergics.md
        │   ├── oxycodone.fa.md
        │   ├── oxycodone.md
        │   ├── oxymorphone.fa.md
        │   ├── oxymorphone.md
        │   ├── pentobarbital.fa.md
        │   ├── pentobarbital.md
        │   ├── pethidine.fa.md
        │   ├── pethidine.md
        │   ├── phenibut.fa.md
        │   ├── phenibut.md
        │   ├── phenobarbital.fa.md
        │   ├── phenobarbital.md
        │   ├── pregabalin.fa.md
        │   ├── pregabalin.md
        │   ├── pyrazolam.fa.md
        │   ├── pyrazolam.md
        │   ├── secobarbital.fa.md
        │   ├── secobarbital.md
        │   ├── sufentanil.fa.md
        │   ├── sufentanil.md
        │   ├── tapentadol.fa.md
        │   ├── tapentadol.md
        │   ├── temazepam.fa.md
        │   ├── temazepam.md
        │   ├── thienodiazepines.fa.md
        │   ├── thienodiazepines.md
        │   ├── tizanidine.fa.md
        │   ├── tizanidine.md
        │   ├── tramadol.fa.md
        │   ├── tramadol.md
        │   ├── u-47700.fa.md
        │   ├── u-47700.md
        │   ├── zolpidem.fa.md
        │   ├── zolpidem.md
        │   ├── zopiclone.fa.md
        │   └── zopiclone.md
        ├── Entheogens
        │   ├── acacia-confusa.fa.md
        │   ├── acacia-confusa.md
        │   ├── amanita-muscaria.fa.md
        │   ├── amanita-muscaria.md
        │   ├── argyreia-nervosa.fa.md
        │   ├── argyreia-nervosa.md
        │   ├── banisteriopsis-caapi.fa.md
        │   ├── banisteriopsis-caapi.md
        │   ├── blue-lotus.fa.md
        │   ├── blue-lotus.md
        │   ├── cannabis.fa.md
        │   ├── cannabis.md
        │   ├── datura.fa.md
        │   ├── datura.md
        │   ├── entheogens.fa.md
        │   ├── entheogens.md
        │   ├── iboga.fa.md
        │   ├── iboga.md
        │   ├── ipomoea-tricolor.fa.md
        │   ├── ipomoea-tricolor.md
        │   ├── mimosa-hostilis.fa.md
        │   ├── mimosa-hostilis.md
        │   ├── nicotiana.fa.md
        │   ├── nicotiana.md
        │   ├── peyote.fa.md
        │   ├── peyote.md
        │   ├── psilocybin-mushrooms.fa.md
        │   ├── psilocybin-mushrooms.md
        │   ├── salvia-divinorum.fa.md
        │   ├── salvia-divinorum.md
        │   ├── san-pedro.fa.md
        │   ├── san-pedro.md
        │   ├── syrian-rue.fa.md
        │   ├── syrian-rue.md
        │   ├── yopo.fa.md
        │   └── yopo.md
        ├── Hallucinogens
        │   ├── Cannabinoids
        │   │   ├── 5f-akb48.fa.md
        │   │   ├── 5f-akb48.md
        │   │   ├── 5f-pb-22.fa.md
        │   │   ├── 5f-pb-22.md
        │   │   ├── ab-fubinaca.fa.md
        │   │   ├── ab-fubinaca.md
        │   │   ├── apica.fa.md
        │   │   ├── apica.md
        │   │   ├── cannabinoids.fa.md
        │   │   ├── cannabinoids.md
        │   │   ├── cbd.fa.md
        │   │   ├── cbd.md
        │   │   ├── cbda.fa.md
        │   │   ├── cbda.md
        │   │   ├── cbdh.fa.md
        │   │   ├── cbdh.md
        │   │   ├── cbdp.fa.md
        │   │   ├── cbdp.md
        │   │   ├── delta-10-thc.fa.md
        │   │   ├── delta-10-thc.md
        │   │   ├── delta-11-thc.fa.md
        │   │   ├── delta-11-thc.md
        │   │   ├── delta-8-thc.fa.md
        │   │   ├── delta-8-thc.md
        │   │   ├── hhc.fa.md
        │   │   ├── hhc.md
        │   │   ├── jwh-018.fa.md
        │   │   ├── jwh-018.md
        │   │   ├── jwh-073.fa.md
        │   │   ├── jwh-073.md
        │   │   ├── phytocannabinoids.fa.md
        │   │   ├── phytocannabinoids.md
        │   │   ├── semi-synthetic-phytocannabinoids.fa.md
        │   │   ├── semi-synthetic-phytocannabinoids.md
        │   │   ├── sts-135.fa.md
        │   │   ├── sts-135.md
        │   │   ├── synthetic-cannabinoids.fa.md
        │   │   ├── synthetic-cannabinoids.md
        │   │   ├── thc-o-acetate.fa.md
        │   │   ├── thc-o-acetate.md
        │   │   ├── thc.fa.md
        │   │   ├── thc.md
        │   │   ├── thca.fa.md
        │   │   ├── thca.md
        │   │   ├── thcb.fa.md
        │   │   ├── thcb.md
        │   │   ├── thch.fa.md
        │   │   ├── thch.md
        │   │   ├── thcp.fa.md
        │   │   ├── thcp.md
        │   │   ├── thj-018.fa.md
        │   │   ├── thj-018.md
        │   │   ├── thj-2201.fa.md
        │   │   └── thj-2201.md
        │   ├── Deliriants
        │   │   ├── antihistamines.fa.md
        │   │   ├── antihistamines.md
        │   │   ├── atropine.fa.md
        │   │   ├── atropine.md
        │   │   ├── benzydamine.fa.md
        │   │   ├── benzydamine.md
        │   │   ├── deliriants.fa.md
        │   │   ├── deliriants.md
        │   │   ├── elemicin.fa.md
        │   │   ├── elemicin.md
        │   │   ├── hyoscyamine.fa.md
        │   │   ├── hyoscyamine.md
        │   │   ├── myristicin.fa.md
        │   │   ├── myristicin.md
        │   │   ├── promethazine.fa.md
        │   │   ├── promethazine.md
        │   │   ├── scopolamine.fa.md
        │   │   ├── scopolamine.md
        │   │   ├── tropane-alkaloids.fa.md
        │   │   └── tropane-alkaloids.md
        │   ├── Dissociatives
        │   │   ├── 2-fluorodeschloroketamine.fa.md
        │   │   ├── 2-fluorodeschloroketamine.md
        │   │   ├── 2-oxo-pce.fa.md
        │   │   ├── 2-oxo-pce.md
        │   │   ├── 2-oxo-pcm.fa.md
        │   │   ├── 2-oxo-pcm.md
        │   │   ├── 3-cl-pcp.fa.md
        │   │   ├── 3-cl-pcp.md
        │   │   ├── 3-ho-pce.fa.md
        │   │   ├── 3-ho-pce.md
        │   │   ├── 3-ho-pcp.fa.md
        │   │   ├── 3-ho-pcp.md
        │   │   ├── 3-meo-pce.fa.md
        │   │   ├── 3-meo-pce.md
        │   │   ├── 3-meo-pcmo.fa.md
        │   │   ├── 3-meo-pcmo.md
        │   │   ├── 3-meo-pcp.fa.md
        │   │   ├── 3-meo-pcp.md
        │   │   ├── 4-meo-pcp.fa.md
        │   │   ├── 4-meo-pcp.md
        │   │   ├── adamantanes.fa.md
        │   │   ├── adamantanes.md
        │   │   ├── arylcyclohexylamines.fa.md
        │   │   ├── arylcyclohexylamines.md
        │   │   ├── dextromethorphan.fa.md
        │   │   ├── dextromethorphan.md
        │   │   ├── dextrorphan.fa.md
        │   │   ├── dextrorphan.md
        │   │   ├── diarylethylamines.fa.md
        │   │   ├── diarylethylamines.md
        │   │   ├── diphenidine.fa.md
        │   │   ├── diphenidine.md
        │   │   ├── dissociatives.fa.md
        │   │   ├── dissociatives.md
        │   │   ├── ephenidine.fa.md
        │   │   ├── ephenidine.md
        │   │   ├── eticyclidine.fa.md
        │   │   ├── eticyclidine.md
        │   │   ├── hydroxetamine.fa.md
        │   │   ├── hydroxetamine.md
        │   │   ├── ketamine.fa.md
        │   │   ├── ketamine.md
        │   │   ├── methoxetamine.fa.md
        │   │   ├── methoxetamine.md
        │   │   ├── morphinans.fa.md
        │   │   ├── morphinans.md
        │   │   ├── phencyclidine.fa.md
        │   │   ├── phencyclidine.md
        │   │   ├── r-ketamine.fa.md
        │   │   ├── r-ketamine.md
        │   │   ├── s-ketamine.fa.md
        │   │   └── s-ketamine.md
        │   ├── Psychedelics
        │   │   ├── 2C-x
        │   │   │   ├── 2c-b.fa.md
        │   │   │   ├── 2c-b.md
        │   │   │   ├── 2c-c.fa.md
        │   │   │   ├── 2c-c.md
        │   │   │   ├── 2c-d.fa.md
        │   │   │   ├── 2c-d.md
        │   │   │   ├── 2c-e.fa.md
        │   │   │   ├── 2c-e.md
        │   │   │   ├── 2c-h.fa.md
        │   │   │   ├── 2c-h.md
        │   │   │   ├── 2c-i.fa.md
        │   │   │   ├── 2c-i.md
        │   │   │   ├── 2c-p.fa.md
        │   │   │   ├── 2c-p.md
        │   │   │   ├── 2c-t-2.fa.md
        │   │   │   ├── 2c-t-2.md
        │   │   │   ├── 2c-t-21.fa.md
        │   │   │   ├── 2c-t-21.md
        │   │   │   ├── 2c-t-7.fa.md
        │   │   │   ├── 2c-t-7.md
        │   │   │   ├── 2c-t-x.fa.md
        │   │   │   ├── 2c-t-x.md
        │   │   │   ├── 2c-t.fa.md
        │   │   │   ├── 2c-t.md
        │   │   │   ├── 2c-x.fa.md
        │   │   │   ├── 2c-x.md
        │   │   │   ├── 2c-xderivatives.fa.md
        │   │   │   └── 2c-xderivatives.md
        │   │   ├── Classical_psychedelics
        │   │   │   ├── classical-psychedelics.fa.md
        │   │   │   └── classical-psychedelics.md
        │   │   ├── DOx
        │   │   │   ├── 25-dma.fa.md
        │   │   │   ├── 25-dma.md
        │   │   │   ├── dob.fa.md
        │   │   │   ├── dob.md
        │   │   │   ├── doc.fa.md
        │   │   │   ├── doc.md
        │   │   │   ├── doi.fa.md
        │   │   │   ├── doi.md
        │   │   │   ├── dom.fa.md
        │   │   │   ├── dom.md
        │   │   │   ├── dox.fa.md
        │   │   │   ├── dox.md
        │   │   │   ├── doxderivatives.fa.md
        │   │   │   └── doxderivatives.md
        │   │   ├── Empathogens
        │   │   │   ├── 5-apb.fa.md
        │   │   │   ├── 5-apb.md
        │   │   │   ├── 5-mapb.fa.md
        │   │   │   ├── 5-mapb.md
        │   │   │   ├── 6-apb.fa.md
        │   │   │   ├── 6-apb.md
        │   │   │   ├── 6-apdb.fa.md
        │   │   │   ├── 6-apdb.md
        │   │   │   ├── benzofurans.fa.md
        │   │   │   ├── benzofurans.md
        │   │   │   ├── empathogens.fa.md
        │   │   │   ├── empathogens.md
        │   │   │   ├── mda.fa.md
        │   │   │   ├── mda.md
        │   │   │   ├── mdai.fa.md
        │   │   │   ├── mdai.md
        │   │   │   ├── mdea.fa.md
        │   │   │   ├── mdea.md
        │   │   │   ├── mdma.fa.md
        │   │   │   ├── mdma.md
        │   │   │   ├── mdxx.fa.md
        │   │   │   ├── mdxx.md
        │   │   │   ├── methylone.fa.md
        │   │   │   ├── methylone.md
        │   │   │   ├── pma.fa.md
        │   │   │   ├── pma.md
        │   │   │   ├── pmma.fa.md
        │   │   │   └── pmma.md
        │   │   ├── Lysergamides
        │   │   │   ├── 1b-lsd.fa.md
        │   │   │   ├── 1b-lsd.md
        │   │   │   ├── 1cp-al-lad.fa.md
        │   │   │   ├── 1cp-al-lad.md
        │   │   │   ├── 1cp-lsd.fa.md
        │   │   │   ├── 1cp-lsd.md
        │   │   │   ├── 1cp-mipla.fa.md
        │   │   │   ├── 1cp-mipla.md
        │   │   │   ├── 1p-eth-lad.fa.md
        │   │   │   ├── 1p-eth-lad.md
        │   │   │   ├── 1p-lsd.fa.md
        │   │   │   ├── 1p-lsd.md
        │   │   │   ├── 1v-lsd.fa.md
        │   │   │   ├── 1v-lsd.md
        │   │   │   ├── al-lad.fa.md
        │   │   │   ├── al-lad.md
        │   │   │   ├── ald-52.fa.md
        │   │   │   ├── ald-52.md
        │   │   │   ├── eth-lad.fa.md
        │   │   │   ├── eth-lad.md
        │   │   │   ├── lae-32.fa.md
        │   │   │   ├── lae-32.md
        │   │   │   ├── lsa.fa.md
        │   │   │   ├── lsa.md
        │   │   │   ├── lsd.fa.md
        │   │   │   ├── lsd.md
        │   │   │   ├── lsh.fa.md
        │   │   │   ├── lsh.md
        │   │   │   ├── lsm-775.fa.md
        │   │   │   ├── lsm-775.md
        │   │   │   ├── lsz.fa.md
        │   │   │   ├── lsz.md
        │   │   │   ├── lysergamides.fa.md
        │   │   │   ├── lysergamides.md
        │   │   │   ├── mipla.fa.md
        │   │   │   ├── mipla.md
        │   │   │   ├── pargy-lad.fa.md
        │   │   │   ├── pargy-lad.md
        │   │   │   ├── pro-lad.fa.md
        │   │   │   └── pro-lad.md
        │   │   ├── Mescaline_homologues
        │   │   │   ├── 3c-e.fa.md
        │   │   │   ├── 3c-e.md
        │   │   │   ├── 3c-p.fa.md
        │   │   │   ├── 3c-p.md
        │   │   │   ├── allylescaline.fa.md
        │   │   │   ├── allylescaline.md
        │   │   │   ├── escaline.fa.md
        │   │   │   ├── escaline.md
        │   │   │   ├── mescaline-homologues.fa.md
        │   │   │   ├── mescaline-homologues.md
        │   │   │   ├── mescaline.fa.md
        │   │   │   ├── mescaline.md
        │   │   │   ├── methallylescaline.fa.md
        │   │   │   ├── methallylescaline.md
        │   │   │   ├── proscaline.fa.md
        │   │   │   └── proscaline.md
        │   │   ├── Miscellaneousـphenethylamines
        │   │   │   ├── 2c-b-fly.fa.md
        │   │   │   ├── 2c-b-fly.md
        │   │   │   ├── bromo-dragonfly.fa.md
        │   │   │   ├── bromo-dragonfly.md
        │   │   │   ├── k-2c-b.fa.md
        │   │   │   ├── k-2c-b.md
        │   │   │   ├── miscellaneousphenethylamines.fa.md
        │   │   │   ├── miscellaneousphenethylamines.md
        │   │   │   ├── tma-2.fa.md
        │   │   │   ├── tma-2.md
        │   │   │   ├── tma-6.fa.md
        │   │   │   └── tma-6.md
        │   │   ├── N-Benzylـphenethylamines
        │   │   │   ├── 25b-nboh.fa.md
        │   │   │   ├── 25b-nboh.md
        │   │   │   ├── 25b-nbome.fa.md
        │   │   │   ├── 25b-nbome.md
        │   │   │   ├── 25c-nboh.fa.md
        │   │   │   ├── 25c-nboh.md
        │   │   │   ├── 25c-nbome.fa.md
        │   │   │   ├── 25c-nbome.md
        │   │   │   ├── 25d-nbome.fa.md
        │   │   │   ├── 25d-nbome.md
        │   │   │   ├── 25e-nboh.fa.md
        │   │   │   ├── 25e-nboh.md
        │   │   │   ├── 25i-nboh.fa.md
        │   │   │   ├── 25i-nboh.md
        │   │   │   ├── 25i-nbome.fa.md
        │   │   │   ├── 25i-nbome.md
        │   │   │   ├── 25n-nbome.fa.md
        │   │   │   ├── 25n-nbome.md
        │   │   │   ├── n-benzylphenethylamines.fa.md
        │   │   │   └── n-benzylphenethylamines.md
        │   │   ├── Others
        │   │   │   ├── 5-meo-dibf.fa.md
        │   │   │   ├── 5-meo-dibf.md
        │   │   │   ├── efavirenz.fa.md
        │   │   │   └── efavirenz.md
        │   │   ├── Tryptamines
        │   │   │   ├── Base Tryptamines
        │   │   │   │   ├── amt.fa.md
        │   │   │   │   ├── amt.md
        │   │   │   │   ├── base-tryptamines.fa.md
        │   │   │   │   ├── base-tryptamines.md
        │   │   │   │   ├── det.fa.md
        │   │   │   │   ├── det.md
        │   │   │   │   ├── dipt.fa.md
        │   │   │   │   ├── dipt.md
        │   │   │   │   ├── dmt.fa.md
        │   │   │   │   ├── dmt.md
        │   │   │   │   ├── dpt.fa.md
        │   │   │   │   ├── dpt.md
        │   │   │   │   ├── ept.fa.md
        │   │   │   │   ├── ept.md
        │   │   │   │   ├── met.fa.md
        │   │   │   │   ├── met.md
        │   │   │   │   ├── mipt.fa.md
        │   │   │   │   ├── mipt.md
        │   │   │   │   ├── mpt.fa.md
        │   │   │   │   └── mpt.md
        │   │   │   ├── Substituted tryptamines
        │   │   │   │   ├── 4-aco-det.fa.md
        │   │   │   │   ├── 4-aco-det.md
        │   │   │   │   ├── 4-aco-dipt.fa.md
        │   │   │   │   ├── 4-aco-dipt.md
        │   │   │   │   ├── 4-aco-dmt.fa.md
        │   │   │   │   ├── 4-aco-dmt.md
        │   │   │   │   ├── 4-aco-met.fa.md
        │   │   │   │   ├── 4-aco-met.md
        │   │   │   │   ├── 4-aco-mipt.fa.md
        │   │   │   │   ├── 4-aco-mipt.md
        │   │   │   │   ├── 4-ho-det.fa.md
        │   │   │   │   ├── 4-ho-det.md
        │   │   │   │   ├── 4-ho-dipt.fa.md
        │   │   │   │   ├── 4-ho-dipt.md
        │   │   │   │   ├── 4-ho-dpt.fa.md
        │   │   │   │   ├── 4-ho-dpt.md
        │   │   │   │   ├── 4-ho-ept.fa.md
        │   │   │   │   ├── 4-ho-ept.md
        │   │   │   │   ├── 4-ho-met.fa.md
        │   │   │   │   ├── 4-ho-met.md
        │   │   │   │   ├── 4-ho-mipt.fa.md
        │   │   │   │   ├── 4-ho-mipt.md
        │   │   │   │   ├── 4-ho-mpt.fa.md
        │   │   │   │   ├── 4-ho-mpt.md
        │   │   │   │   ├── 5-meo-dalt.fa.md
        │   │   │   │   ├── 5-meo-dalt.md
        │   │   │   │   ├── 5-meo-dipt.fa.md
        │   │   │   │   ├── 5-meo-dipt.md
        │   │   │   │   ├── 5-meo-dmt.fa.md
        │   │   │   │   ├── 5-meo-dmt.md
        │   │   │   │   ├── 5-meo-mipt.fa.md
        │   │   │   │   ├── 5-meo-mipt.md
        │   │   │   │   ├── 56-mdo-dmt.fa.md
        │   │   │   │   ├── 56-mdo-dmt.md
        │   │   │   │   ├── baeocystin.fa.md
        │   │   │   │   ├── baeocystin.md
        │   │   │   │   ├── bufotenin.fa.md
        │   │   │   │   ├── bufotenin.md
        │   │   │   │   ├── psilocin.fa.md
        │   │   │   │   ├── psilocin.md
        │   │   │   │   ├── psilocybin.fa.md
        │   │   │   │   └── psilocybin.md
        │   │   │   ├── tryptamines.fa.md
        │   │   │   └── tryptamines.md
        │   │   ├── psychedelics.fa.md
        │   │   └── psychedelics.md
        │   ├── hallucinogens.fa.md
        │   ├── hallucinogens.md
        │   └── β-Carbolines
        │       ├── harmaline.fa.md
        │       ├── harmaline.md
        │       ├── harmine.fa.md
        │       ├── harmine.md
        │       ├── tetrahydroharmine.fa.md
        │       ├── tetrahydroharmine.md
        │       ├── β-Carbolines.fa.md
        │       └── β-Carbolines.md
        ├── Miscellaneous
        │   ├── 5-hydroxytryptophan.fa.md
        │   ├── 5-hydroxytryptophan.md
        │   ├── acetylcholine-boosters.fa.md
        │   ├── acetylcholine-boosters.md
        │   ├── acetylcholinesterase-inhibitors.fa.md
        │   ├── acetylcholinesterase-inhibitors.md
        │   ├── alkyl-nitrites.fa.md
        │   ├── alkyl-nitrites.md
        │   ├── amyl-nitrite.fa.md
        │   ├── amyl-nitrite.md
        │   ├── ayahuasca.fa.md
        │   ├── ayahuasca.md
        │   ├── calea-ternifolia.fa.md
        │   ├── calea-ternifolia.md
        │   ├── changa.fa.md
        │   ├── changa.md
        │   ├── chloroform.fa.md
        │   ├── chloroform.md
        │   ├── diethyl-ether.fa.md
        │   ├── diethyl-ether.md
        │   ├── dxm-and-dph.fa.md
        │   ├── dxm-and-dph.md
        │   ├── dxm.fa.md
        │   ├── dxm.md
        │   ├── entada-rheedii.fa.md
        │   ├── entada-rheedii.md
        │   ├── galantamine.fa.md
        │   ├── galantamine.md
        │   ├── ibogaine.fa.md
        │   ├── ibogaine.md
        │   ├── inhalants.fa.md
        │   ├── inhalants.md
        │   ├── isobutyl-nitrite.fa.md
        │   ├── isobutyl-nitrite.md
        │   ├── isopropyl-nitrite.fa.md
        │   ├── isopropyl-nitrite.md
        │   ├── miscellaneous.fa.md
        │   ├── miscellaneous.md
        │   ├── nitrous-oxide.fa.md
        │   ├── nitrous-oxide.md
        │   ├── oneirogens.fa.md
        │   ├── oneirogens.md
        │   ├── opioid-receptor-agonists.fa.md
        │   ├── opioid-receptor-agonists.md
        │   ├── polysubstance-combinations.fa.md
        │   ├── polysubstance-combinations.md
        │   ├── progesterone.fa.md
        │   ├── progesterone.md
        │   ├── salvinorin-a.fa.md
        │   ├── salvinorin-a.md
        │   ├── salvinorin-b-methoxymethyl-ether.fa.md
        │   ├── salvinorin-b-methoxymethyl-ether.md
        │   ├── sigmaergics.fa.md
        │   ├── sigmaergics.md
        │   ├── various.fa.md
        │   ├── various.md
        │   ├── xenon.fa.md
        │   └── xenon.md
        ├── Psychoactives.fa.md
        ├── Stimulants
        │   ├── 2-ai.fa.md
        │   ├── 2-ai.md
        │   ├── 2-fa.fa.md
        │   ├── 2-fa.md
        │   ├── 2-fea.fa.md
        │   ├── 2-fea.md
        │   ├── 2-fma.fa.md
        │   ├── 2-fma.md
        │   ├── 3-fa.fa.md
        │   ├── 3-fa.md
        │   ├── 3-fea.fa.md
        │   ├── 3-fea.md
        │   ├── 3-fma.fa.md
        │   ├── 3-fma.md
        │   ├── 3-fpm.fa.md
        │   ├── 3-fpm.md
        │   ├── 3-mmc.fa.md
        │   ├── 3-mmc.md
        │   ├── 34-ctmp.fa.md
        │   ├── 34-ctmp.md
        │   ├── 4-fa.fa.md
        │   ├── 4-fa.md
        │   ├── 4-fma.fa.md
        │   ├── 4-fma.md
        │   ├── 4f-eph.fa.md
        │   ├── 4f-eph.md
        │   ├── 4f-mph.fa.md
        │   ├── 4f-mph.md
        │   ├── 8-chlorotheophylline.fa.md
        │   ├── 8-chlorotheophylline.md
        │   ├── Nootropics
        │   │   ├── 5-htp.fa.md
        │   │   ├── 5-htp.md
        │   │   ├── adrafinil.fa.md
        │   │   ├── adrafinil.md
        │   │   ├── alpha-gpc.fa.md
        │   │   ├── alpha-gpc.md
        │   │   ├── aniracetam.fa.md
        │   │   ├── aniracetam.md
        │   │   ├── armodafinil.fa.md
        │   │   ├── armodafinil.md
        │   │   ├── bromantane.fa.md
        │   │   ├── bromantane.md
        │   │   ├── choline-bitartrate.fa.md
        │   │   ├── choline-bitartrate.md
        │   │   ├── choline.fa.md
        │   │   ├── choline.md
        │   │   ├── citicoline.fa.md
        │   │   ├── citicoline.md
        │   │   ├── coluracetam.fa.md
        │   │   ├── coluracetam.md
        │   │   ├── creatine.fa.md
        │   │   ├── creatine.md
        │   │   ├── dietary-supplements.fa.md
        │   │   ├── dietary-supplements.md
        │   │   ├── eugeroics.fa.md
        │   │   ├── eugeroics.md
        │   │   ├── gaba.fa.md
        │   │   ├── gaba.md
        │   │   ├── l-theanine.fa.md
        │   │   ├── l-theanine.md
        │   │   ├── l-tyrosine.fa.md
        │   │   ├── l-tyrosine.md
        │   │   ├── meclofenoxate.fa.md
        │   │   ├── meclofenoxate.md
        │   │   ├── memantine.fa.md
        │   │   ├── memantine.md
        │   │   ├── modafinil.fa.md
        │   │   ├── modafinil.md
        │   │   ├── n-acetylcysteine.fa.md
        │   │   ├── n-acetylcysteine.md
        │   │   ├── n-methylbisfluoromodafinil.fa.md
        │   │   ├── n-methylbisfluoromodafinil.md
        │   │   ├── noopept.fa.md
        │   │   ├── noopept.md
        │   │   ├── nootropics.fa.md
        │   │   ├── nootropics.md
        │   │   ├── others.fa.md
        │   │   ├── others.md
        │   │   ├── oxiracetam.fa.md
        │   │   ├── oxiracetam.md
        │   │   ├── phenylpiracetam.fa.md
        │   │   ├── phenylpiracetam.md
        │   │   ├── piracetam.fa.md
        │   │   ├── piracetam.md
        │   │   ├── pramiracetam.fa.md
        │   │   ├── pramiracetam.md
        │   │   ├── racetams.fa.md
        │   │   ├── racetams.md
        │   │   ├── s-adenosyl-methionine.fa.md
        │   │   ├── s-adenosyl-methionine.md
        │   │   ├── tianeptine.fa.md
        │   │   └── tianeptine.md
        │   ├── aminorexes.fa.md
        │   ├── aminorexes.md
        │   ├── amphetamine.fa.md
        │   ├── amphetamine.md
        │   ├── amphetamines.fa.md
        │   ├── amphetamines.md
        │   ├── butylone.fa.md
        │   ├── butylone.md
        │   ├── caffeine.fa.md
        │   ├── caffeine.md
        │   ├── cathinone.fa.md
        │   ├── cathinone.md
        │   ├── cathinones.fa.md
        │   ├── cathinones.md
        │   ├── cocaine.fa.md
        │   ├── cocaine.md
        │   ├── cyclazodone.fa.md
        │   ├── cyclazodone.md
        │   ├── desoxypipradrol.fa.md
        │   ├── desoxypipradrol.md
        │   ├── dexmethylphenidate.fa.md
        │   ├── dexmethylphenidate.md
        │   ├── dextroamphetamine.fa.md
        │   ├── dextroamphetamine.md
        │   ├── ephedrine.fa.md
        │   ├── ephedrine.md
        │   ├── ephylone.fa.md
        │   ├── ephylone.md
        │   ├── ethcathinone.fa.md
        │   ├── ethcathinone.md
        │   ├── ethylone.fa.md
        │   ├── ethylone.md
        │   ├── ethylphenidate.fa.md
        │   ├── ethylphenidate.md
        │   ├── fenethylline.fa.md
        │   ├── fenethylline.md
        │   ├── hexedrone.fa.md
        │   ├── hexedrone.md
        │   ├── isopropylphenidate.fa.md
        │   ├── isopropylphenidate.md
        │   ├── lisdexamfetamine.fa.md
        │   ├── lisdexamfetamine.md
        │   ├── mcpp.fa.md
        │   ├── mcpp.md
        │   ├── mdpv.fa.md
        │   ├── mdpv.md
        │   ├── mephedrone.fa.md
        │   ├── mephedrone.md
        │   ├── methamphetamine.fa.md
        │   ├── methamphetamine.md
        │   ├── methcathinone.fa.md
        │   ├── methcathinone.md
        │   ├── methiopropamine.fa.md
        │   ├── methiopropamine.md
        │   ├── methylnaphthidate.fa.md
        │   ├── methylnaphthidate.md
        │   ├── methylphenidate.fa.md
        │   ├── methylphenidate.md
        │   ├── mexedrone.fa.md
        │   ├── mexedrone.md
        │   ├── n-ethylhexedrone.fa.md
        │   ├── n-ethylhexedrone.md
        │   ├── n-ethylpentedrone.fa.md
        │   ├── n-ethylpentedrone.md
        │   ├── nicotine.fa.md
        │   ├── nicotine.md
        │   ├── nm-2-ai.fa.md
        │   ├── nm-2-ai.md
        │   ├── pentedrone.fa.md
        │   ├── pentedrone.md
        │   ├── phenidates.fa.md
        │   ├── phenidates.md
        │   ├── phenmetrazines.fa.md
        │   ├── phenmetrazines.md
        │   ├── php.fa.md
        │   ├── php.md
        │   ├── piperazines.fa.md
        │   ├── piperazines.md
        │   ├── prolintane.fa.md
        │   ├── prolintane.md
        │   ├── propylhexedrine.fa.md
        │   ├── propylhexedrine.md
        │   ├── pvp.fa.md
        │   ├── pvp.md
        │   ├── pyrrolidinophenones.fa.md
        │   ├── pyrrolidinophenones.md
        │   ├── rti-111.fa.md
        │   ├── rti-111.md
        │   ├── stimulants.fa.md
        │   ├── stimulants.md
        │   ├── theacrine.fa.md
        │   ├── theacrine.md
        │   ├── tropanes.fa.md
        │   ├── tropanes.md
        │   ├── xanthines.fa.md
        │   └── xanthines.md
        └── index.md
```

---
### `categoryMapFa.ts`
```ts
export const categoryFaMap = {
  Psychonautics: "سایکوناتیک",
  Dissociatives: "مواد بی‌حسی",
  Substances: "مواد",
  Effects: "تأثیرات",
  Interactions: "تداخلات",
  "Harm Reduction": "کاهش آسیب",
  Consciousness: "هشیاری",
  Models: "مدل‌ها",
} as const;

```

---
### `content.config.ts`
```ts
// Import the glob loader
import { glob } from "astro/loaders";
// Import utilities from `astro:content`
import { z, defineCollection } from "astro:content";

// =========================
// BLOG COLLECTION (existing)
// =========================
const blog = defineCollection({
  loader: glob({ pattern: "**/[^_]*.md", base: "./src/blog" }),
  schema: z.object({
    title: z.string(),
    pubDate: z.date(),
    description: z.string(),
    author: z.string(),
    image: z.object({
      url: z.string(),
      alt: z.string(),
    }),
    tags: z.array(z.string()),
  }),
});


const stories = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/stories" }),
  schema: z.object({
  title: z.string().optional(),
  description: z.string().optional(),
  published: z.date().optional(),
  }),
});

const poetry = defineCollection({
  loader: glob({
    pattern: "**/*.md",
    base: "./src/poems",
  }),
  schema: z.object({
    title: z.string(),
    poet: z.string().optional(),
    date: z.string().optional(),
    loyalty: z.string().optional(),
    image: z.string().optional(),
  }),
});

const storiesFa = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/stories-fa" }),
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    file: z.string().optional(),
    image: z.string().optional(),
    link: z.string().optional(),
    date: z.string().optional(),
    published: z.boolean().default(true),
  }),
});

const wiki = defineCollection({
  loader: glob({
    pattern: "**/*.md",
    base: "./src/wiki",
    entries: true,   // ⭐ THIS enables full path info
  }),
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
  }),
});



const wikiFa = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/wiki" }),
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    category: z.string().optional(),
    tags: z.array(z.string()).optional(),
    image: z.string().optional(),
  }),
});




export const collections = {
  blog,
  stories,
  poetry,
  storiesFa,
  wiki,
  wikiFa,
};

```

---
### `blog\post-1.md`
```md
---
title: 'My First Blog Post'
pubDate: 2022-07-01
description: 'This is the first post of my new Astro blog.'
author: 'Astro Learner'
image:
    url: 'https://docs.astro.build/assets/rose.webp'
    alt: 'The Astro logo on a dark background with a pink glow.'
tags: ["Vibe Coding", "Animation", "Coughy Net"]
---




Welcome to my _new blog_ about learning Astro! Here, I will share my learning journey as I build a new website.

## What I've accomplished

1. **Installing Astro**: First, I created a new Astro project and set up my online accounts.

2. **Making Pages**: I then learned how to make pages by creating new `.astro` files and placing them in the `src/pages/` folder.

3. **Making Blog Posts**: This is my first blog post! I now have Astro pages and Markdown posts!

## What's next

I will finish the Astro tutorial, and then keep adding more posts. Watch this space for more to come.
```

---
### `blog\post-2.md`
```md
---
title: My Second Blog Post
author: Astro Learner
description: "After learning some Astro, I couldn't stop!"
image:
    url: "https://docs.astro.build/assets/arc.webp"
    alt: "The Astro logo on a dark background with a purple gradient arc."
pubDate: 2022-07-08
tags: ["astro", "literature", "Coughy Net", "Ali Ghorbani"]
---
After a successful first week learning Astro, I decided to try some more. I wrote and imported a small component from memory!
```

---
### `blog\post-3.md`
```md
---
title: My Third Blog Post
author: Astro Learner
description: "I had some challenges, but asking in the community really helped!"
image:
    url: "https://docs.astro.build/assets/rays.webp"
    alt: "The Astro logo on a dark background with rainbow rays."
pubDate: 2022-07-15
tags: ["astro", "learning in public", "setbacks", "community"]
---
It wasn't always smooth sailing, but I'm enjoying building with Astro. And, the [Discord community](https://astro.build/chat) is really friendly and helpful!
```

---
### `blog\post-4.md`
```md
---
title: My Fourth Blog Post
author: Astro Learner
description: "This post will show up on its own!"
image:
    url: "https://docs.astro.build/default-og-image.png"
    alt: "The word astro against an illustration of planets and stars."
pubDate: 2022-08-08
tags: ["astro", "successes"]
---
This post should show up with my other blog posts, because `import.meta.glob()` is returning a list of all my posts in order to create my list.
```

---
### `components\Astrogen.astro`
```astro
---

---

<style>
    html::before,
    html::after {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        z-index: -1;
        transition: opacity 0.25s ease-in-out;
        pointer-events: none;
    }

    html::before {
        background-image: url(/src/assets/backgrounds/bwca-day.png);
        opacity: 1;
    }

    html.dark::before {
        opacity: 0;
    }

    html::after {
        background-image: url(/src/assets/backgrounds/bwca-night.png);
        opacity: 0;
    }

    html.dark::after {
        opacity: 1;
    }
    
</style>

```

---
### `components\Background.astro`
```astro
---
/* FINAL FIXED VERSION — SSR initial theme + dual layers + no flash */

let initialTheme = "light";
const cookieTheme = Astro.cookies.get("theme")?.value;

if (cookieTheme === "dark") initialTheme = "dark";
---

<style>
  .layer-light,
  .layer-dark {
    transition: opacity 0.45s ease-in-out;
  }

  /* Initial theme is applied BEFORE paint using SSR */
  #bg[data-theme="light"] .layer-light { opacity: 1; }
  #bg[data-theme="light"] .layer-dark  { opacity: 0; }

  #bg[data-theme="dark"] .layer-light { opacity: 0; }
  #bg[data-theme="dark"] .layer-dark  { opacity: 1; }

  svg [data-depth] {
    transition: transform 0.15s ease-out;
    transform-origin: center;
    transform-box: fill-box;
  }
</style>

<div
  id="bg"
  data-theme={initialTheme}
  class="fixed inset-0 w-full h-full overflow-hidden -z-10 pointer-events-none"
>

  <svg
    class="absolute inset-0 w-full h-full"
    viewBox="0 0 1440 900"
    preserveAspectRatio="xMidYMid slice"
  >

    <!-- SKY -->
    <g data-depth="0.05">

      <!-- LIGHT -->
      <g class="layer-light">
        <defs>
          <linearGradient id="skyLight" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#e2f1ff" />
            <stop offset="100%" stop-color="#8cc4ff" />
          </linearGradient>
        </defs>
        <rect width="1440" height="900" fill="url(#skyLight)" />
      </g>

      <!-- DARK -->
      <g class="layer-dark">
        <defs>
          <linearGradient id="skyDark" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#050b25" />
            <stop offset="100%" stop-color="#1a2751" />
          </linearGradient>
        </defs>
        <rect width="1440" height="900" fill="url(#skyDark)" />
      </g>

    </g>

    <!-- FAR -->
    <g data-depth="0.12">

      <path
        class="layer-light"
        d="M0 450 Q300 380 600 430 T1200 420 T1440 440 L1440 900 0 900 Z"
        fill="#b3d4ff"
      />

      <path
        class="layer-dark"
        d="M0 450 Q300 380 600 430 T1200 420 T1440 440 L1440 900 0 900 Z"
        fill="#111b3a"
      />

    </g>

    <!-- MID -->
    <g data-depth="0.2">

      <path
        class="layer-light"
        d="M0 520 Q200 470 450 510 T950 520 T1440 500 L1440 900 0 900 Z"
        fill="#8ab7f5"
      />

      <path
        class="layer-dark"
        d="M0 520 Q200 470 450 510 T950 520 T1440 500 L1440 900 0 900 Z"
        fill="#141f3f"
      />

    </g>

    <!-- WATER -->
    <g data-depth="0.25">

      <rect class="layer-light" x="0" y="540" width="1440" height="360" fill="#a4d8ff" />

      <rect class="layer-dark" x="0" y="540" width="1440" height="360" fill="#0b1732" />

    </g>

    <!-- FOREGROUND -->
    <g data-depth="0.35">

      <path
        class="layer-light"
        d="M0 580 Q150 540 260 580 T520 600 T800 590 T1100 610 T1440 580 L1440 900 0 900 Z"
        fill="#4a7cc2"
      />

      <path
        class="layer-dark"
        d="M0 580 Q150 540 260 580 T520 600 T800 590 T1100 610 T1440 580 L1440 900 0 900 Z"
        fill="#050816"
      />

    </g>

  </svg>
</div>

<script>
  const bg = document.getElementById("bg");
  const layers = bg.querySelectorAll("[data-depth]");

  /* PARALLAX */
  function scrollParallax() {
    const y = window.scrollY;
    layers.forEach(el => {
      const d = parseFloat(el.dataset.depth);
      el.style.transform = `translateY(${y * d * -0.25}px)`;
    });
  }
  window.addEventListener("scroll", scrollParallax, { passive: true });
  scrollParallax();

  window.addEventListener("mousemove", e => {
    const x = e.clientX / window.innerWidth - 0.5;
    const y = e.clientY / window.innerHeight - 0.5;
    layers.forEach(el => {
      const d = parseFloat(el.dataset.depth);
      el.style.transform = `translate(${x * d * -20}px, ${y * d * -10}px)`;
    });
  });

  /* THEME SWITCH (client side) */
  const observer = new MutationObserver(() => {
    const dark = document.documentElement.classList.contains("dark");
    const newTheme = dark ? "dark" : "light";

    bg.dataset.theme = newTheme;

    /* Store theme for SSR next refresh */
    document.cookie = `theme=${newTheme}; Path=/; SameSite=Lax; Max-Age=31536000`;
  });

  observer.observe(document.documentElement, {
    attributes: true,
    attributeFilter: ["class"],
  });
</script>

```

---
### `components\BlogPost.astro`
```astro
---
const { title, url } = Astro.props
---
<li><a href={url}>{title}</a></li>
```

---
### `components\BrandBadge.astro`
```astro
---
import LangToggle from "./LangToggle.astro";
---

<div class="fixed top-3 left-3 z-200 pointer-events-none">
  <div
    class="relative pointer-events-auto flex items-center gap-2
           h-[3.1rem] px-[clamp(0.9rem,1.2vw,1.2rem)] 
           rounded-full"
  >
    <!-- Background -->
    <div
      class="absolute inset-0 rounded-full 
            
             transition-color-scale duration-300 ease-out z-10"
    ></div>

    <!-- Brand title -->
    <a
      href="/"
      class="relative z-210 font-semibold select-none
             text-[clamp(1.08rem,1.35vw,1.45rem)]
             whitespace-nowrap hover:scale-105 duration-500"
    >
      Coughy.net
    </a>

    <!-- Language toggle next to brand -->
    <div class="relative z-210 ml-1">
      <LangToggle />
    </div>

  </div>
</div>

```

---
### `components\BrandBadgeWiki.astro`
```astro
---
import LangToggle from "./LangToggle.astro";

// AUTO-DETECT from URL (correct)
const pathname = Astro.url.pathname;
const isFA = pathname.startsWith("/fa/");
const wikiHome = isFA ? "/fa/wiki" : "/wiki";
---

<div class="fixed top-3 left-3 z-200 pointer-events-none">
  <div
    class="relative pointer-events-auto flex items-center gap-2
           h-[3.1rem] px-[clamp(0.9rem,1.2vw,1.2rem)] 
           rounded-full"
  >
    <div
      class="absolute inset-0 rounded-full 
             transition-color-scale duration-300 ease-out z-10"
    ></div>

    <a
      href={wikiHome}
      class="relative z-210 font-semibold select-none
             text-[clamp(1.08rem,1.35vw,1.45rem)]
             whitespace-nowrap hover:scale-105 duration-500"
    >
      Coughy's Wiki
    </a>

    <div class="relative z-210 ml-1">
      <LangToggle />
    </div>

  </div>
</div>

```

---
### `components\Hamburger.astro`
```astro
---
/*
  Hamburger.astro
*/
---

<button
  id="menu-toggle"
  class="relative flex items-center justify-center w-10 h-10
         rounded-full hover:bg-white/20 drop-shadow hover:scale-110
         transition-all duration-300 pointer-events-auto active:scale-95"
>
  <span
    id="line-top"
    class="block absolute w-5 h-0.5 bg-neutral-900 dark:bg-white rounded
           transition-transform duration-300 ease-in-out origin-center"
    style="transform: translateY(-6px);"
  ></span>

  <span
    id="line-mid"
    class="block absolute w-5 h-0.5 bg-neutral-900 dark:bg-white rounded
           transition-opacity duration-200 ease-in-out origin-center"
  ></span>

  <span
    id="line-bot"
    class="block absolute w-5 h-0.5 bg-neutral-900 dark:bg-white rounded
           transition-transform duration-300 ease-in-out origin-center"
    style="transform: translateY(6px);"
  ></span>
</button>

<script>
  // @ts-nocheck
  document.addEventListener("DOMContentLoaded", () => {
    const btn = document.getElementById("menu-toggle");
    const top = document.getElementById("line-top");
    const mid = document.getElementById("line-mid");
    const bot = document.getElementById("line-bot");

    if (!btn) return;

    let isOpen = false;

    function animateOpen() {
      top.style.transform = "translateY(0px) rotate(45deg)";
      bot.style.transform = "translateY(0px) rotate(-45deg)";
      mid.style.opacity = "0";
      isOpen = true;
    }

    function animateClose() {
      top.style.transform = "translateY(-6px) rotate(0deg)";
      bot.style.transform = "translateY(6px) rotate(0deg)";
      mid.style.opacity = "1";
      isOpen = false;
    }

    // Button click → open or close
    btn.addEventListener("click", () => {
      if (isOpen) window.closeSidebar(); // sidebar will call animateClose()
      else window.openSidebar();         // sidebar will call animateOpen()
    });

    // Expose animation functions globally
    window.hamburgerOpen = animateOpen;
    window.hamburgerClose = animateClose;
  });
</script>

```

---
### `components\Header.astro`
```astro
---
import BrandBadge from "./BrandBadge.astro";
import Navbar from "./Navbar.astro";
import UtilityBar from "./UtilityBar.astro";
import SidebarMenu from "./SidebarMenu.astro";
import { navLinks, farLinks } from "../data/nav";

const { lang = "en" } = Astro.props;
const links = lang === "fa" ? farLinks : navLinks;
const isFA = lang === "fa";


---



<!-- BRAND: fixed top left -->
<BrandBadge />


<!-- HEADER containing Navbar in proper grid -->
<header
  class={[
    "fixed top-3 left-0 right-0 z-50",
    "text-neutral-700 dark:text-white font-medium tracking-tight",
    "transition-color-scale duration-500 ease-in-out select-none",
  ].join(" ")}
>

  <div
    class="mx-auto w-full max-w-7xl
           px-[clamp(1rem,3vw,2.5rem)]
           grid grid-cols-[auto_1fr_auto] items-center gap-4"
  >
    <!-- LEFT SPACER -->
    <div aria-hidden="true" class="h-[2.7rem]"></div>

    <!-- NAVBAR CENTERED -->
    <Navbar navLinks={links} lang={lang} />


    <!-- RIGHT SPACER (balances utility bar) -->
    <div aria-hidden="true" class="h-[2.7rem]"></div>
  </div>
</header>


<!-- UTILITY BAR (top-right, fixed) -->
<UtilityBar />


<!-- SIDEBAR MENU -->
<SidebarMenu navLinks={links} lang={lang} />


<!-- NAVBAR JS -->
<script src="/scripts/navbar.js" defer></script>

```

---
### `components\HeaderWiki.astro`
```astro
---
import BrandBadge from "./BrandBadgeWiki.astro";
import Navbar from "./Navbar.astro";
import UtilityBar from "./UtilityBar.astro";
import SidebarMenu from "./SidebarMenu.astro";
import { farWikiLinks, wikiLinks } from "../data/nav";

const { lang = "en" } = Astro.props;
const links = lang === "fa" ? farWikiLinks : wikiLinks;
const isFA = lang === "fa";


---



<!-- BRAND: fixed top left -->
<BrandBadge lang={lang} />


<!-- HEADER containing Navbar in proper grid -->
<header lang={lang}
  class={[
    "fixed top-3 left-0 right-0 z-50",
    "text-neutral-700 dark:text-white font-medium tracking-tight",
    "transition-color-scale duration-500 ease-in-out select-none",
  ].join(" ")}
>

  <div
    class="mx-auto w-full max-w-7xl
           px-[clamp(1rem,3vw,2.5rem)]
           grid grid-cols-[auto_1fr_auto] items-center gap-4"
  >
    <!-- LEFT SPACER -->
    <div aria-hidden="true" class="h-[2.7rem]"></div>

    <!-- NAVBAR CENTERED -->
    <Navbar navLinks={links} lang={lang} />


    <!-- RIGHT SPACER (balances utility bar) -->
    <div aria-hidden="true" class="h-[2.7rem]"></div>
  </div>
</header>


<!-- UTILITY BAR (top-right, fixed) -->
<UtilityBar />


<!-- SIDEBAR MENU -->
<SidebarMenu navLinks={links} lang={lang} />


<!-- NAVBAR JS -->
<script src="/scripts/navbar.js" defer></script>

```

---
### `components\LangToggle.astro`
```astro
<button
  id="lang-toggle"
  class="relative flex items-center justify-center w-10 h-10 rounded-full
         hover:bg-white/20 transition-all duration-300 drop-shadow-xs/30 hover:scale-110"
  aria-label="Toggle language"
  title="Change language"
>
  <!-- EN icon -->
  <span
    id="icon-en"
    class="absolute text-sm font-bold transition-all duration-500"
  >
    فا
  </span>

  <!-- FA icon -->
  <span
    id="icon-fa"
    class="absolute text-sm font-bold transition-all duration-500"
  >
    en
  </span>
</button>

<script is:inline>
  ;(() => {
    const urlLang = location.pathname.startsWith("/fa") ? "fa" : "en";

    // THE REAL FINAL SOURCE OF TRUTH
    const lang = urlLang;

    const css = `
      #icon-en {
        opacity: ${lang === "en" ? "1" : "0"};
        transform: ${lang === "en" ? "scale(1)" : "scale(0.5)"};
      }
      #icon-fa {
        opacity: ${lang === "fa" ? "1" : "0"};
        transform: ${lang === "fa" ? "scale(1)" : "scale(0.5)"};
      }
    `;
    const tag = document.createElement("style");
    tag.innerHTML = css;
    document.head.appendChild(tag);
  })();
</script>

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const btn = document.getElementById("lang-toggle")!;
    const iconEN = document.getElementById("icon-en")!;
    const iconFA = document.getElementById("icon-fa")!;

    const animateIcons = (toFA: boolean) => {
      iconEN.style.opacity = toFA ? "0" : "1";
      iconEN.style.transform = toFA ? "scale(0.5)" : "scale(1)";

      iconFA.style.opacity = toFA ? "1" : "0";
      iconFA.style.transform = toFA ? "scale(1)" : "scale(0.5)";
    };

    btn.addEventListener("click", () => {
      const isFA = location.pathname.startsWith("/fa");
      let newPath;
    
      if (isFA) {
        // FA → EN
        newPath = location.pathname.replace(/^\/fa/, "") || "/";
        localStorage.setItem("lang", "en");
      } else {
        // EN → FA
        newPath = "/fa" + (location.pathname === "/" ? "" : location.pathname);
        localStorage.setItem("lang", "fa");
      }
    
      window.location.href = newPath;
    });
  });
</script>


```

---
### `components\ModeToggle.astro`
```astro
<button
  id="theme-toggle"
  class="relative flex items-center justify-center w-10 h-10 rounded-full
         hover:bg-white/20 transition-all duration-300 drop-shadow-xs/30 hover:scale-110"
  aria-label="Toggle theme"
  title="Toggle dark mode"
>
  <!-- Moon -->
  <svg
    id="icon-moon"
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 24 24"
    fill="currentColor"
    class="absolute w-6 h-6 text-yellow-300 transition-all duration-500"
  >
    <path d="M12 1.992a10 10 0 1 0 9.236 13.838c.341 -.82 -.476 -1.644 -1.298 -1.31a6.5 6.5 0 0 1 -6.864 -10.787l.077 -.08c.551 -.63 .113 -1.653 -.758 -1.653h-.266l-.068 -.006l-.06 -.002z" />
  </svg>

  <!-- Sun -->
  <svg
    id="icon-sun"
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 24 24"
    fill="currentColor"
    class="absolute w-6 h-6 text-yellow-300 transition-all duration-500"
  >
    <path d="M12 19a1 1 0 0 1 .993 .883l.007 .117v1a1 1 0 0 1 -1.993 .117l-.007 -.117v-1a1 1 0 0 1 1 -1z" />
    <path d="M18.313 16.91l.094 .083l.7 .7a1 1 0 0 1 -1.32 1.497l-.094 -.083l-.7 -.7a1 1 0 0 1 1.218 -1.567l.102 .07z" />
    <path d="M7.007 16.993a1 1 0 0 1 .083 1.32l-.083 .094l-.7 .7a1 1 0 0 1 -1.497 -1.32l.083 -.094l-.7 -.7a1 1 0 0 1 1.414 0z" />
    <path d="M4 11a1 1 0 0 1 .117 1.993l-.117 .007h-1a1 1 0 0 1 -.117 -1.993l.117 -.007h1z" />
    <path d="M21 11a1 1 0 0 1 .117 1.993l-.117 .007h-1a1 1 0 0 1 -.117 -1.993l.117 -.007h1z" />
    <path d="M6.213 4.81l.094 .083l.7 .7a1 1 0 0 1 -1.32 1.497l-.094 -.083l-.7 -.7a1 1 0 0 1 1.217 -1.567l.102 .07z" />
    <path d="M19.107 4.893a1 1 0 0 1 .083 1.32l-.083 .094l-.7 .7a1 1 0 0 1 -1.497 -1.32l.083 -.094l.7 -.7a1 1 0 0 1 1.414 0z" />
    <path d="M12 2a1 1 0 0 1 .993 .883l.007 .117v1a1 1 0 0 1 -1.993 .117l-.007 -.117v-1a1 1 0 0 1 1 -1z" />
    <path d="M12 7a5 5 0 1 1 -4.995 5.217l-.005 -.217l.005 -.217a5 5 0 0 1 4.995 -4.783z" />
  </svg>
</button>

<script is:inline>
  /**
   * PRE-PAINT THEME + ICON STATE (no FOUC)
   */
  ;(() => {
    const stored = localStorage.getItem("theme");
    const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
    const isDark = stored === "dark" || (!stored && prefersDark);

    // apply theme immediately
    document.documentElement.classList.toggle("dark", isDark);

    // preload icon states
    const css = `
      #icon-sun {
        opacity: ${isDark ? "1" : "0"};
        transform: ${isDark ? "scale(1) rotate(0deg)" : "scale(0.5) rotate(90deg)"};
      }
      #icon-moon {
        opacity: ${isDark ? "0" : "1"};
        transform: ${isDark ? "scale(0.5) rotate(-90deg)" : "scale(1) rotate(0deg)"};
      }
    `;
    const tag = document.createElement("style");
    tag.innerHTML = css;
    document.head.appendChild(tag);
  })();
</script>

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const root = document.documentElement;

    // Non-null DOM elements (safe inside component)
    const btn = document.getElementById("theme-toggle")!;
    const sun = document.getElementById("icon-sun")!;
    const moon = document.getElementById("icon-moon")!;

    const updateIcons = (isDark: boolean) => {
      sun.style.opacity = isDark ? "1" : "0";
      sun.style.transform = isDark
        ? "scale(1) rotate(0deg)"
        : "scale(0.5) rotate(90deg)";

      moon.style.opacity = isDark ? "0" : "1";
      moon.style.transform = isDark
        ? "scale(0.5) rotate(-90deg)"
        : "scale(1) rotate(0deg)";
    };

    btn.addEventListener("click", () => {
      const newDark = !root.classList.contains("dark");
      root.classList.toggle("dark", newDark);
      updateIcons(newDark);
      localStorage.setItem("theme", newDark ? "dark" : "light");
    });
  });
</script>

```

---
### `components\Navbar.astro`
```astro
---
interface NavItem {
  label: string;
  href: string;
}

interface Props {
  navLinks: NavItem[] | [string, string][];
  lang?: "en" | "fa";
}

function normalizeNavLinks(raw: Props["navLinks"]) {
  return raw.map((item) => {
    if (Array.isArray(item)) return { label: item[0], href: item[1] };
    return item as NavItem;
  });
}

// Auto-detect language from URL
const pathname = Astro.url.pathname;
const isWiki = pathname.startsWith("/wiki") || pathname.startsWith("/fa/wiki");
const isFA = pathname.startsWith("/fa/");

// Import all link sets 
import { navLinks, farLinks, wikiLinks, farWikiLinks } from "../data/nav";

// Decide which set to use
let rawLinks;

if (isWiki) {
  rawLinks = isFA ? farWikiLinks : wikiLinks;
} else {
  rawLinks = isFA ? farLinks : navLinks;
}

// Normalize
const links = normalizeNavLinks(rawLinks);


// normalize current path
const current = Astro.url.pathname.replace(/\/+$/, "") || "/";
---

<script src="/scripts/nav-effects.js" defer></script>


<header
  class={[
    "fixed top-3 left-0 right-0 z-50",
    "text-neutral-700 dark:text-white font-medium tracking-tight",
    "transition-color-scale duration-500 ease-in-out select-none",
    isFA && "direction-rtl text-right",        // RTL fix
  ].join(" ")}
>
  <nav
    data-main-nav
    class={[
      "relative justify-self-center flex items-center justify-center h-[3.1rem]",
      "px-[clamp(0.6rem,1.5vw,1.5rem)] max-w-[900px] w-full rounded-full",
      "bg-[rgba(250,250,250,0.15)] hover:bg-white/30 dark:hover:bg-black/30",
      "backdrop-blur-xl shadow-lg shadow-black/10",
      "transition-all duration-300 ease-in-out min-w-0 overflow-hidden",
      isFA && "flex-row-reverse",              // RTL fix
    ].join(" ")}
    aria-label="Main Navigation"
  >
    <ul
      class={[
        "flex justify-center items-center flex-nowrap",
        "gap-[clamp(0.3rem,1.2vw,2rem)] list-none m-0 p-0",
        isFA && "flex-row-reverse",            // RTL fix
      ].join(" ")}
    >
      {links.map(({ label, href }) => {
        const normalized = href.replace(/\/+$/, "") || "/";
        const isActive = current === normalized;

        return (
          <li class="shrink">
            <a
              href={href}
              data-nav-link
              data-text={label}
              class={[
                "relative inline-block px-[clamp(0.4rem,0.8vw,0.8rem)] py-1",
                "transition-all duration-300 ease-out",
                "text-neutral-700 dark:text-white",

                // underline
                "after:absolute after:left-1/2 after:-bottom-1 after:w-0 after:h-0.5",
                "after:rounded-full after:bg-linear-to-r after:from-blue-400 after:to-purple-400",
                "after:transition-all after:duration-400 after:ease-out",

                // hover
                "hover:text-white hover:after:w-2/3 hover:after:-translate-x-1/2 hover:scale-125",

                // glitch
                "glitch-strong",

                // active
                isActive &&
                  "text-white scale-110 after:w-2/3 after:-translate-x-1/2 hover:scale-125",
              ]
                .filter(Boolean)
                .join(" ")}
            >

              {isFA ? (
                /* FA MODE — full word (ligature-safe), keeps animations */
                <span class="wave-fa">{label}</span>
              ) : (
                /* EN MODE — letter wave animation preserved */
                <span class="wave">
                  {label.split("").map((char, i) => (
                    <span class="wave-letter" style={`--i:${i}`}>{char}</span>
                  ))}
                </span>
              )}

            </a>
          </li>
        );
      })}
    </ul>
  </nav>
</header>

<style>
/* EN wave animation */
.wave {
  display: inline-flex;
}
.wave-letter {
  display: inline-block;
  transition: transform 0.2s ease, color 0.3s ease;
}

/* Persian: full-word, no breaking */
.wave-fa {
  display: inline-block;
}
</style>


<style>
.wave {
  display: inline-flex;
}

.wave-letter {
  display: inline-block;
  transition: transform 0.2s ease, color 0.3s ease;
}

/* 🌊 Forward wave (default, triggered by JS) */
.wave-active .wave-letter {
  animation: wave-up 0.75s ease forwards;
  animation-delay: calc(var(--i) * 90ms);
}

/* 🔄 Reverse wave (triggered by JS on mouseleave) */
.wave-reverse .wave-letter {
  animation: wave-down 0.75s ease forwards;
  animation-delay: calc(var(--i) * 90ms);
}

/* 💫 Double wave (optional mode: forward → backward)
   you can trigger by adding class="wave-double"
*/
.wave-double .wave-letter {
  animation: wave-double 1.2s ease forwards;
  animation-delay: calc(var(--i) * 100ms);
}

/* 🌈 Color shifting during wave */
.wave-active .wave-letter,
.wave-reverse .wave-letter,
.wave-double .wave-letter {
  color: var(--wave-color, #7dd3fc); /* default cyan glow */
}

@keyframes wave-up {
  0%   { transform: translateY(0); color: inherit; }
  40%  { transform: translateY(-6px); color: #60a5fa; }  /* blue-ish */
  60%  { transform: translateY(0); }
  100% { transform: translateY(0); color: inherit; }
}

@keyframes wave-down {
  0%   { transform: translateY(0); color: inherit; }
  40%  { transform: translateY(6px); color: #a78bfa; }  /* purple-ish */
  60%  { transform: translateY(0); }
  100% { transform: translateY(0); color: inherit; }
}

/* Forward → Backward */
@keyframes wave-double {
  0%   { transform: translateY(0) }
  25%  { transform: translateY(-6px) }
  50%  { transform: translateY(0) }
  75%  { transform: translateY(6px) }
  100% { transform: translateY(0) }
}
.wave-letter.spin-blur {
  filter: blur(1.2px);
  opacity: 0.75;
  transition: filter 120ms, opacity 120ms;
}

@media (max-width: 768px) {
  [data-main-nav] {
    opacity: 0;
    transform: scale(0.9);
    pointer-events: none;
    visibility: hidden;
  }
}



</style>

```

---
### `components\NavbarWiki.astro`
```astro
---
interface NavItem {
  label: string;
  href: string;
}

interface Props {
  navLinks: NavItem[] | [string, string][];
  lang?: "en" | "fa";
}

function normalizeNavLinks(raw: Props["navLinks"]) {
  return raw.map((item) => {
    if (Array.isArray(item)) return { label: item[0], href: item[1] };
    return item as NavItem;
  });
}

const { navLinks, lang = "en" } = Astro.props as Props;
const isFA = lang === "fa";

const links = normalizeNavLinks(navLinks);
const current = Astro.url.pathname.replace(/\/+$/, "") || "/";
---

<script src="/scripts/nav-effects.js" defer></script>

<header
  class={[
    "fixed top-3 left-0 right-0 z-50",
    "text-neutral-700 dark:text-neutral-100",
    "font-medium tracking-tight select-none",
    "transition-colors duration-500 ease-in-out",
    isFA && "direction-rtl text-right",
  ].join(" ")}
>

  <nav
    data-main-nav
    class={[
      // 🔥 Wiki style: softer, flatter, more academic
      "relative justify-self-center flex items-center justify-center h-[3.1rem]",
      "px-[clamp(0.6rem,1.2vw,1.2rem)] max-w-[1100px] w-full rounded-full",
      "bg-white/10 dark:bg-black/20",
      "border border-white/20 dark:border-white/10",
      "backdrop-blur-xl shadow-md shadow-black/10",
      "hover:bg-white/20 dark:hover:bg-black/30",
      "transition-all duration-300 ease-in-out min-w-0 overflow-hidden",
      isFA && "flex-row-reverse",
    ].join(" ")}
    aria-label="Wiki Navigation"
  >

    <ul
      class={[
        "flex justify-center items-center flex-nowrap",
        "gap-[clamp(0.3rem,1.2vw,1.8rem)] list-none m-0 p-0",
        isFA && "flex-row-reverse",
      ].join(" ")}
    >

      {links.map(({ label, href }) => {
        const normalized = href.replace(/\/+$/, "") || "/";
        const isActive = current === normalized;

        return (
          <li class="shrink">
            <a
              href={href}
              data-nav-link
              data-text={label}
              class={[
                "relative inline-block px-[0.6rem] py-1",
                "transition-all duration-300 ease-out",
                "text-neutral-700 dark:text-neutral-100",

                // 🔥 Wiki underline — thinner, more elegant
                "after:absolute after:left-1/2 after:-bottom-0.5 after:w-0 after:h-px",
                "after:bg-neutral-700/40 dark:after:bg-neutral-100/40",
                "after:rounded-full after:transition-all after:duration-300",

                // Hover
                "hover:after:w-2/3 hover:after:-translate-x-1/2",
                "hover:text-neutral-900 dark:hover:text-white",
                "hover:opacity-90",

                // 🔥 Removed loud hover scaling
                // "hover:scale-125" → removed for academic tone

                // Disabled glitch
                // "glitch-strong" → removed

                // Active
                isActive &&
                  "text-white after:w-2/3 after:-translate-x-1/2 opacity-100",
              ]
                .filter(Boolean)
                .join(" ")}
            >

              {isFA ? (
                <span class="wiki-fa">{label}</span>
              ) : (
                <span class="wiki-en">{label}</span>
              )}

            </a>
          </li>
        );
      })}

    </ul>
  </nav>
</header>

<style>
/* ========== ENGLISH STYLE (Wiki) ========== */
.wiki-en {
  font-family: "Noto Serif", serif;
  letter-spacing: 0.3px;
}

/* ========== PERSIAN STYLE (Wiki) ========== */
.wiki-fa {
  font-family: "Noto Serif", serif;
  font-weight: 500;
}

/* Remove wave animations from wiki version */
.wave,
.wave-letter,
.wave-active,
.wave-reverse,
.wave-double {
  animation: none !important;
  transform: none !important;
}
</style>

<style>
@media (max-width: 768px) {
  [data-main-nav] {
    opacity: 0;
    transform: scale(0.9);
    pointer-events: none;
    visibility: hidden;
  }
}
</style>

```

---
### `components\SidebarMenu.astro`
```astro
---
type LinkTuple = [string, string];

const { navLinks, lang = "en" } = Astro.props as {
  navLinks: LinkTuple[];
  lang?: "en" | "fa";
};
---

<div
  id="sidebar-backdrop"
  data-sidebar-backdrop
  class="fixed inset-0 bg-black/40 backdrop-blur-md opacity-0 pointer-events-none
         transition-opacity duration-500 z-60"
>
  <aside
    id="sidebar-overlay"
    data-sidebar
    class="select-none absolute top-0 right-0 w-[min(80vw,300px)] h-full 
           bg-white/10 dark:bg-black/40
           border-l border-white/20 backdrop-blur-2xl backdrop-saturate-150 shadow-xl
           flex flex-col items-center justify-center gap-6
           text-white text-lg font-medium
           transform translate-x-full transition-transform duration-500 z-70"
    inert
  >
    <ul class="flex flex-col gap-6" dir={lang === "fa" ? "rtl" : "ltr"}>
      {navLinks.map(([label, href]: [string, string]) => (
        <li>
          <a
            href={href}
            class={lang === "fa" ? "block text-right" : ""}
          >
            {label}
          </a>
        </li>
      ))}
    </ul>
  </aside>
</div>

<style is:global>
  [data-sidebar].open {
    transform: translateX(0);
  }

  [data-sidebar-backdrop].visible {
    opacity: 1;
    pointer-events: auto;
  }
</style>

<script>
  // @ts-nocheck
  document.addEventListener("DOMContentLoaded", () => {
    const backdrop = document.getElementById("sidebar-backdrop");
    const sidebar = document.getElementById("sidebar-overlay");

    function openSidebar() {
      sidebar.classList.add("open");
      backdrop.classList.add("visible");
      sidebar.removeAttribute("inert");
      window.hamburgerOpen();
    }

    function closeSidebar() {
      sidebar.classList.remove("open");
      backdrop.classList.remove("visible");
      sidebar.setAttribute("inert", "");
      window.hamburgerClose();
    }

    window.openSidebar = openSidebar;
    window.closeSidebar = closeSidebar;

    backdrop.addEventListener("click", () => closeSidebar());
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") closeSidebar();
    });

    sidebar.querySelectorAll("a").forEach(a =>
      a.addEventListener("click", () => closeSidebar())
    );
  });
</script>

```

---
### `components\SocialBar.astro`
```astro
---

---


<!-- Social -->

<div
  id="social"
  class="fixed bottom-4 left-1/2 -translate-x-1/2 z-70
         flex items-center justify-center gap-4 px-5 py-2
         bg-white/10 backdrop-blur-lg hover:bg-white/30 dark:hover:bg-white/5
         transition-all duration-500 ease-in-out
         rounded-xl shadow-md text-sm w-fit"
>
  <!-- Twitter -->
  <a
    href="https://twitter.com/coughman8"
    target="_blank"
    class="text-white dark:text-white hover:text-blue-400 transition-all duration-300 hover:scale-150"
    aria-label="Twitter"
  >
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="currentColor"
    >
      <path d="M14.058 3.41c-1.807 .767 -2.995 2.453 -3.056 4.38l-.002 .182l-.243 -.023c-2.392 -.269 -4.498 -1.512 -5.944 -3.531a1 1 0 0 0 -1.685 .092l-.097 .186l-.049 .099c-.719 1.485 -1.19 3.29 -1.017 5.203l.03 .273c.283 2.263 1.5 4.215 3.779 5.679l.173 .107l-.081 .043c-1.315 .663 -2.518 .952 -3.827 .9c-1.056 -.04 -1.446 1.372 -.518 1.878c3.598 1.961 7.461 2.566 10.792 1.6c4.06 -1.18 7.152 -4.223 8.335 -8.433l.127 -.495c.238 -.993 .372 -2.006 .401 -3.024l.003 -.332l.393 -.779l.44 -.862l.214 -.434l.118 -.247c.265 -.565 .456 -1.033 .574 -1.43l.014 -.056l.008 -.018c.22 -.593 -.166 -1.358 -.941 -1.358l-.122 .007a.997 .997 0 0 0 -.231 .057l-.086 .038a7.46 7.46 0 0 1 -.88 .36l-.356 .115l-.271 .08l-.772 .214c-1.336 -1.118 -3.144 -1.254 -5.012 -.554l-.211 .084z" />
    </svg>
  </a>

  <!-- GitHub -->
  <a
    href="https://github.com/wr3yth"
    target="_blank"
    class="text-white dark:text-white hover:text-gray-600 transition-all duration-300 hover:scale-150"
    aria-label="GitHub"
  >
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="currentColor"
    >
      <path d="M5.315 2.1c.791 -.113 1.9 .145 3.333 .966l.272 .161l.16 .1l.397 -.083a13.3 13.3 0 0 1 4.59 -.08l.456 .08l.396 .083l.161 -.1c1.385 -.84 2.487 -1.17 3.322 -1.148l.164 .008l.147 .017l.076 .014l.05 .011l.144 .047a1 1 0 0 1 .53 .514a5.2 5.2 0 0 1 .397 2.91l-.047 .267l-.046 .196l.123 .163c.574 .795 .93 1.728 1.03 2.707l.023 .295l.007 .272c0 3.855 -1.659 5.883 -4.644 6.68l-.245 .061l-.132 .029l.014 .161l.008 .157l.004 .365l-.002 .213l-.003 3.834a1 1 0 0 1 -.883 .993l-.117 .007h-6a1 1 0 0 1 -.993 -.883l-.007 -.117v-.734c-1.818 .26 -3.03 -.424 -4.11 -1.878l-.535 -.766c-.28 -.396 -.455 -.579 -.589 -.644l-.048 -.019a1 1 0 0 1 .564 -1.918c.642 .188 1.074 .568 1.57 1.239l.538 .769c.76 1.079 1.36 1.459 2.609 1.191l.001 -.678l-.018 -.168a5.03 5.03 0 0 1 -.021 -.824l.017 -.185l.019 -.12l-.108 -.024c-2.976 -.71 -4.703 -2.573 -4.875 -6.139l-.01 -.31l-.004 -.292a5.6 5.6 0 0 1 .908 -3.051l.152 -.222l.122 -.163l-.045 -.196a5.2 5.2 0 0 1 .145 -2.642l.1 -.282l.106 -.253a1 1 0 0 1 .529 -.514l.144 -.047l.154 -.03z" />
    </svg>
  </a>

  <!-- YouTube -->
  <a
    href="https://youtube.com/coughynist"
    target="_blank"
    class="text-white dark:text-white hover:text-red-500 transition-all duration-300 hover:scale-150"
    aria-label="YouTube"
  >
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="currentColor"
    >
      <path d="M18 3a5 5 0 0 1 5 5v8a5 5 0 0 1 -5 5h-12a5 5 0 0 1 -5 -5v-8a5 5 0 0 1 5 -5zm-9 6v6a1 1 0 0 0 1.514 .857l5 -3a1 1 0 0 0 0 -1.714l-5 -3a1 1 0 0 0 -1.514 .857z" />
    </svg>
  </a>
    <!-- Telegram -->
    <a
      href="https://t.me/gardanravan"
      target="_blank"
      class="text-white dark:text-white hover:text-blue-400 transition-all duration-300 hover:scale-150"
      aria-label="Telegram"
    >
      <svg 
        width="24px" 
        height="24px" 
        version="1.1" 
        xmlns="http://www.w3.org/2000/svg" 
        xmlns:xlink="http://www.w3.org/1999/xlink" 
        xml:space="preserve" 
        style="fill-rule:evenodd;clip-rule:evenodd;stroke-linejoin:round;stroke-miterlimit:1.41421;"
      >
        <path 
          d="M18.384,22.779c0.322,0.228 0.737,0.285 1.107,0.145c0.37,-0.141 0.642,-0.457 0.724,-0.84c0.869,-4.084 2.977,-14.421 3.768,-18.136c0.06,-0.28 -0.04,-0.571 -0.26,-0.758c-0.22,-0.187 -0.525,-0.241 -0.797,-0.14c-4.193,1.552 -17.106,6.397 -22.384,8.35c-0.335,0.124 -0.553,0.446 -0.542,0.799c0.012,0.354 0.25,0.661 0.593,0.764c2.367,0.708 5.474,1.693 5.474,1.693c0,0 1.452,4.385 2.209,6.615c0.095,0.28 0.314,0.5 0.603,0.576c0.288,0.075 0.596,-0.004 0.811,-0.207c1.216,-1.148 3.096,-2.923 3.096,-2.923c0,0 3.572,2.619 5.598,4.062Zm-11.01,-8.677l1.679,5.538l0.373,-3.507c0,0 6.487,-5.851 10.185,-9.186c0.108,-0.098 0.123,-0.262 0.033,-0.377c-0.089,-0.115 -0.253,-0.142 -0.376,-0.064c-4.286,2.737 -11.894,7.596 -11.894,7.596Z"
          fill="currentColor"
        />
      </svg>
    </a>
  <!-- Instagram -->
  <a
    href="https://instagram.com/pdc.ali"
    target="_blank"
    class="group text-white dark:text-white transition-all duration-300 hover:scale-150"
    aria-label="Instagram"
  >
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      class="fill-current group-hover:fill-[url(#instagram-gradient)]"
    >
      <defs>
        <linearGradient id="instagram-gradient" x1="100%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#833ab4" />
          <stop offset="50%" stop-color="#fd1d1d" />
          <stop offset="100%" stop-color="#fcb045" />
        </linearGradient>
      </defs>
      <path d="M16 3a5 5 0 0 1 5 5v8a5 5 0 0 1 -5 5h-8a5 5 0 0 1 -5 -5v-8a5 5 0 0 1 5 -5zm-4 5a4 4 0 0 0 -3.995 3.8l-.005 .2a4 4 0 1 0 4 -4m4.5 -1.5a1 1 0 0 0 -.993 .883l-.007 .127a1 1 0 0 0 1.993 .117l.007 -.127a1 1 0 0 0 -1 -1" />
    </svg>
  </a>
</div>
<style>


</style>
```

---
### `components\UtilityBar.astro`
```astro
---
import ModeToggle from "./ModeToggle.astro";
import Hamburger from "./Hamburger.astro";
---

<div 
  id="utility-bar"
  data-utility-bar
  class="fixed top-3 right-8 z-80 rounded-full 
         flex items-center justify-center h-[3.1rem]
         transition-color-scale duration-500 ease-in-out group"
>
  <div
    id="utility-bg"
    data-utility-bg
    class="absolute left-1/2 -translate-x-1/2 rounded-full
           bg-white/10 group-hover:bg-white/30 dark:group-hover:bg-black/30
           backdrop-blur-xl shadow-lg shadow-black/10
           transition-all duration-200 ease-in-out
           opacity-100 w-32 h-full z-60"
  ></div>

  <div
    id="utility-content"
    data-utility-content
    class="relative z-80 flex items-center gap-2 px-4
           transition-all duration-500 ease-in-out"
  >
    <div
      id="mode-wrapper"
      data-mode-wrapper
      class="transition-transform duration-500 ease-in-out"
    >
      <ModeToggle />
    </div>

    <div id="menu-wrapper" data-hamburger>
      <Hamburger />
    </div>
  </div>
</div>

<style is:global>
  /* Utility BG fade/shift */
  #utility-bg.fade-out {
    opacity: 0;
  }

  #utility-bg.expanded {
    width: 5rem;
    transform: translateX(-5rem) scale(0.9);
  }

  @media (max-width: 600px) {
    #utility-bar {
      right: 1rem;
    }
  }
</style>

```

---
### `components\Welcome.astro`
```astro
---
import astroLogo from '../assets/astro.svg';
import background from '../assets/background.svg';
---

<div id="container">
	<img id="background" src={background.src} alt="" fetchpriority="high" />
	<main>
		<section id="hero">
			<a href="https://astro.build"
				><img src={astroLogo.src} width="115" height="48" alt="Astro Homepage" /></a
			>
			<h1>
				To get started, open the <code><pre>src/pages</pre></code> directory in your project.
			</h1>
			<section id="links">
				<a class="button" href="https://docs.astro.build">Read our docs</a>
				<a href="https://astro.build/chat"
					>Join our Discord <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 127.14 96.36"
						><path
							fill="currentColor"
							d="M107.7 8.07A105.15 105.15 0 0 0 81.47 0a72.06 72.06 0 0 0-3.36 6.83 97.68 97.68 0 0 0-29.11 0A72.37 72.37 0 0 0 45.64 0a105.89 105.89 0 0 0-26.25 8.09C2.79 32.65-1.71 56.6.54 80.21a105.73 105.73 0 0 0 32.17 16.15 77.7 77.7 0 0 0 6.89-11.11 68.42 68.42 0 0 1-10.85-5.18c.91-.66 1.8-1.34 2.66-2a75.57 75.57 0 0 0 64.32 0c.87.71 1.76 1.39 2.66 2a68.68 68.68 0 0 1-10.87 5.19 77 77 0 0 0 6.89 11.1 105.25 105.25 0 0 0 32.19-16.14c2.64-27.38-4.51-51.11-18.9-72.15ZM42.45 65.69C36.18 65.69 31 60 31 53s5-12.74 11.43-12.74S54 46 53.89 53s-5.05 12.69-11.44 12.69Zm42.24 0C78.41 65.69 73.25 60 73.25 53s5-12.74 11.44-12.74S96.23 46 96.12 53s-5.04 12.69-11.43 12.69Z"
						></path></svg
					>
				</a>
			</section>
		</section>
	</main>

	<a href="https://astro.build/blog/astro-5/" id="news" class="box">
		<svg width="32" height="32" fill="none" xmlns="http://www.w3.org/2000/svg"
			><path
				d="M24.667 12c1.333 1.414 2 3.192 2 5.334 0 4.62-4.934 5.7-7.334 12C18.444 28.567 18 27.456 18 26c0-4.642 6.667-7.053 6.667-14Zm-5.334-5.333c1.6 1.65 2.4 3.43 2.4 5.333 0 6.602-8.06 7.59-6.4 17.334C13.111 27.787 12 25.564 12 22.666c0-4.434 7.333-8 7.333-16Zm-6-5.333C15.111 3.555 16 5.556 16 7.333c0 8.333-11.333 10.962-5.333 22-3.488-.774-6-4-6-8 0-8.667 8.666-10 8.666-20Z"
				fill="#111827"></path></svg
		>
		<h2>What's New in Astro 5.0?</h2>
		<p>
			From content layers to server islands, click to learn more about the new features and
			improvements in Astro 5.0
		</p>
	</a>
</div>

<style>
	#background {
		position: fixed;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		z-index: -1;
		filter: blur(100px);
	}

	#container {
		font-family: Inter, Roboto, 'Helvetica Neue', 'Arial Nova', 'Nimbus Sans', Arial, sans-serif;
		height: 100%;
	}

	main {
		height: 100%;
		display: flex;
		justify-content: center;
	}

	#hero {
		display: flex;
		align-items: start;
		flex-direction: column;
		justify-content: center;
		padding: 16px;
	}

	h1 {
		font-size: 22px;
		margin-top: 0.25em;
	}

	#links {
		display: flex;
		gap: 16px;
	}

	#links a {
		display: flex;
		align-items: center;
		padding: 10px 12px;
		color: #111827;
		text-decoration: none;
		transition: color 0.2s;
	}

	#links a:hover {
		color: rgb(78, 80, 86);
	}

	#links a svg {
		height: 1em;
		margin-left: 8px;
	}

	#links a.button {
		color: white;
		background: linear-gradient(83.21deg, #3245ff 0%, #bc52ee 100%);
		box-shadow:
			inset 0 0 0 1px rgba(255, 255, 255, 0.12),
			inset 0 -2px 0 rgba(0, 0, 0, 0.24);
		border-radius: 10px;
	}

	#links a.button:hover {
		color: rgb(230, 230, 230);
		box-shadow: none;
	}

	pre {
		font-family:
			ui-monospace, 'Cascadia Code', 'Source Code Pro', Menlo, Consolas, 'DejaVu Sans Mono',
			monospace;
		font-weight: normal;
		background: linear-gradient(14deg, #d83333 0%, #f041ff 100%);
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
		background-clip: text;
		margin: 0;
	}

	h2 {
		margin: 0 0 1em;
		font-weight: normal;
		color: #111827;
		font-size: 20px;
	}

	p {
		color: #4b5563;
		font-size: 16px;
		line-height: 24px;
		letter-spacing: -0.006em;
		margin: 0;
	}

	code {
		display: inline-block;
		background:
			linear-gradient(66.77deg, #f3cddd 0%, #f5cee7 100%) padding-box,
			linear-gradient(155deg, #d83333 0%, #f041ff 18%, #f5cee7 45%) border-box;
		border-radius: 8px;
		border: 1px solid transparent;
		padding: 6px 8px;
	}

	.box {
		padding: 16px;
		background: rgba(255, 255, 255, 1);
		border-radius: 16px;
		border: 1px solid white;
	}

	#news {
		position: absolute;
		bottom: 16px;
		right: 16px;
		max-width: 300px;
		text-decoration: none;
		transition: background 0.2s;
		backdrop-filter: blur(50px);
	}

	#news:hover {
		background: rgba(255, 255, 255, 0.55);
	}

	@media screen and (max-height: 368px) {
		#news {
			display: none;
		}
	}

	@media screen and (max-width: 768px) {
		#container {
			display: flex;
			flex-direction: column;
		}

		#hero {
			display: block;
			padding-top: 10%;
		}

		#links {
			flex-wrap: wrap;
		}

		#links a.button {
			padding: 14px 18px;
		}

		#news {
			right: 16px;
			left: 16px;
			bottom: 2.5rem;
			max-width: 100%;
		}

		h1 {
			line-height: 1.5;
		}
	}
</style>

```

---
### `components\WikiTree.astro`
```astro
---
/**
 * Props:
 *   entries: wiki entries (English only)
 *   rootFolder: top-level folder under src/wiki (e.g. "Psychoactives" or "Psychoactive_Effects")
 */

const { entries, rootFolder } = Astro.props as {
  entries: any[];
  rootFolder: string;
};

type Node = {
  indexEntry: any | null;
  pages: any[];
  children: Record<string, Node>;
};

function normalizeName(str: string | null | undefined): string {
  if (!str) return "";
  return str
    .toLowerCase()
    .replace(/\.fa\.md$/, "")
    .replace(/\.fa$/, "")
    .replace(/\.md$/, "")
    .replace(/[_\-]+/g, " ")
    .trim();
}

function label(str: string): string {
  return str
    .replace(/[_\-]+/g, " ")
    .replace(/\b\w/g, (c) => c.toUpperCase());
}

function escapeHtml(str: string): string {
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

/** Build full unlimited-depth tree from filePath */
function buildTree(entries: any[]): Node {
  const root: Node = { indexEntry: null, pages: [], children: {} };

  for (const entry of entries) {
    const filePath: string = entry.filePath;
    if (!filePath) continue;

    const parts = filePath.split("/");

    // ["src","wiki","Psychoactives","Hallucinogens","Psychedelics",...,"dmt.md"]
    const wikiParts = parts.slice(2);
    if (wikiParts.length === 0) continue;

    const filename = wikiParts[wikiParts.length - 1]!;
    const baseName = filename.replace(/\.fa\.md$/, "").replace(/\.md$/, "");

    const folders = wikiParts.slice(0, -1); // folders only

    let node = root;
    for (const folder of folders) {
      if (!node.children[folder]) {
        node.children[folder] = {
          indexEntry: null,
          pages: [],
          children: {},
        };
      }
      node = node.children[folder];
    }

    const lastFolder = folders[folders.length - 1] ?? "";
    if (normalizeName(lastFolder) === normalizeName(baseName)) {
      // Folder index page: e.g. Psychoactives/Tryptamines/tryptamines.md
      node.indexEntry = entry;
    } else {
      // Regular article in this folder
      node.pages.push(entry);
    }
  }

  return root;
}

/** Sort pages and children recursively by title / key */
function sortTree(node: Node | undefined): void {
  if (!node) return;

  node.pages.sort((a, b) =>
    (a.data?.title ?? a.id).localeCompare(b.data?.title ?? b.id)
  );

  for (const child of Object.values(node.children)) {
    sortTree(child);
  }
}

const fullTree = buildTree(entries);

// Node representing the given root folder (e.g. "Psychoactives")
const rootNode: Node = fullTree.children[rootFolder] ?? fullTree;

sortTree(rootNode);

/** Render a subfolder (used INSIDE cards, not for the card itself) */
function renderSubfolder(
  name: string,
  node: Node,
  depth: number
): string {
  // depth 0 here = first level INSIDE the card
  const indentClass =
    depth === 0 ? "" : `ml-${Math.min(depth * 3, 12)} border-l pl-3`;

  const Tag =
    depth === 0 ? "h4" : depth === 1 ? "h5" : "h6";

  const headingClass =
    depth === 0
      ? "text-sm font-semibold mb-1"
      : "text-xs font-semibold mb-1";

  let html = `<section class="${indentClass} mb-2">`;

  const lbl = escapeHtml(label(name));

  // Subfolder heading (links to its index page if present)
  if (node.indexEntry) {
    html += `<${Tag} class="${headingClass}">
      <a href="/wiki/${node.indexEntry.id}" class="hover:underline underline-offset-2">${lbl}</a>
    </${Tag}>`;
  } else {
    html += `<${Tag} class="${headingClass}">${lbl}</${Tag}>`;
  }

  // Pages directly inside this folder
  if (node.pages.length > 0) {
    html += `<ul class="ml-4 space-y-0.5 text-sm">`;
    for (const page of node.pages) {
      const title = escapeHtml(page.data?.title ?? page.id);
      html += `<li>
        <a href="/wiki/${page.id}" class="hover:underline underline-offset-2 hover:opacity-80">
          ${title}
        </a>
      </li>`;
    }
    html += `</ul>`;
  }

  // Child folders
  const children = Object.entries(node.children) as [string, Node][];
  children.sort(([a], [b]) => a.localeCompare(b));

  for (const [childName, childNode] of children) {
    html += renderSubfolder(childName, childNode, depth + 1);
  }

  html += `</section>`;
  return html;
}

/** Render the INSIDE of a card: its pages + all subfolders */
function renderCardBody(node: Node): string {
  let html = "";

  // (1) Pages directly in this card's folder (excluding the index page)
  if (node.pages.length > 0) {
    html += `<ul class="space-y-0.5 text-sm mb-3">`;
    for (const page of node.pages) {
      const title = escapeHtml(page.data?.title ?? page.id);
      html += `<li>
        <a href="/wiki/${page.id}" class="hover:underline underline-offset-2 hover:opacity-80">
          ${title}
        </a>
      </li>`;
    }
    html += `</ul>`;
  }

  // (2) Subfolders inside this folder
  const children = Object.entries(node.children) as [string, Node][];
  children.sort(([a], [b]) => a.localeCompare(b));

  for (const [childName, childNode] of children) {
    html += renderSubfolder(childName, childNode, 0);
  }

  return html;
}

// Depth-1 children under the root folder become cards
const topCards = Object.entries(rootNode.children) as [string, Node][];
topCards.sort(([a], [b]) => a.localeCompare(b));
---

<!-- Responsive auto-fit card grid -->
<div
  class="grid gap-8"
  style="grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));"
>
  {topCards.map(([name, node]) => (
    <article
      class="rounded-2xl bg-white/10 dark:bg-white/5 border border-white/10 backdrop-blur-xl shadow-xl p-5"
    >
      <!-- Card title = folder name, linked to its index page if present -->
      <h3 class="text-lg font-semibold mb-3">
        {node.indexEntry ? (
          <a
            href={`/wiki/${node.indexEntry.id}`}
            class="hover:underline underline-offset-2 hover:opacity-80"
          >
            {label(name)}
          </a>
        ) : (
          label(name)
        )}
      </h3>

      <!-- Card content = pages + nested subfolders (NO duplicate main heading) -->
      <div
        class="space-y-2 text-sm"
        set:html={renderCardBody(node)}
      ></div>
    </article>
  ))}
</div>

```

---
### `data\nav.ts`
```ts
export const navLinks: [string, string][] = [
  ["Home", "/"],
  ["Blog", "/blog"],
  ["Literature", "/literature"],
  ["Projects", "/projects"],
  ["Research", "/research"],
  ["Partners", "/partners"],
  ["Wiki", "/wiki"],
  ["About", "/about"],
]as const;
 
export const wikiLinks: [string, string][] = [
  ["Psychoactives", "/wiki/psychoactives"],
  ["Effects", "/wiki/effects"],
  ["Interactions", "/wiki/interactions"],
  ["Harm Reduction", "/wiki/harm_reduction"],
  ["Reports", "/wiki/reports"],
  ["About", "/wiki/about"],
  ["Coughy.net", "/"],
]as const;
 
export const farLinks: [string, string][] = [
  ["خانه", "/fa/"],
  ["بلاگ", "/fa/blog"],
  ["داستان", "/fa/stories"],
  ["پروژه ها", "/fa/projects"],
  ["تحقیقات", "/fa/research"],
  ["شرکا", "/fa/partners"],
  ["ویکی", "/fa/wiki"],
  ["درباره", "/fa/about"],
]as const;
 
export const farWikiLinks: [string, string][] = [
  ["مواد", "/fa/wiki/substances"],
  ["تأثیرات", "/fa/wiki/effects"],
  ["تداخلات", "/fa/wiki/interactions"],
  ["کاهش آسیب", "/fa/wiki/harm_reduction"],
  ["گزارش‌ها", "/fa/wiki/reports"],
  ["درباره", "/fa/wiki/about"],
  ["کافی‌نت", "/fa/"],
]as const;
 


```

---
### `layouts\BaseLayout.astro`
```astro
---
import Background from "../components/Astrogen.astro";
import Header from "../components/Header.astro";
import SocialBar from "../components/SocialBar.astro";
import "../styles/global.css";


const {
  pageTitle,
  lang = "en",     // 'en' or 'fa'
  pageClass = "",  // optional page-specific classes
} = Astro.props;
---

<html lang={lang}  class="transition-none">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <slot name="head" />

    <!-- THEME: prevent FOUC -->
    <script is:inline>
      const saved = localStorage.getItem("theme");
      const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
      const isDark = saved === "dark" || (!saved && prefersDark);
      if (isDark) document.documentElement.classList.add("dark");
    </script>

    <!-- Auto font switch based on language -->
    {lang === "fa" ? (
      <link
        rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700&display=swap"
      />
    ) : (
      <link
        rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Noto+Serif&family=Noto+Sans+Symbols+2&display=swap"
      />
    )}

    <!-- Allow transitions only after page is ready -->
    <script is:inline>
      window.addEventListener("load", () => {
        document.documentElement.classList.remove("transition-none");
      });
    </script>
  </head>

  <body class={`min-h-screen ${lang === "fa" ? "font-[Vazirmatn]" : "font-[Noto_Serif]"} ${pageClass}`}>
    <Background />
    <Header lang={lang} />

    <!-- Main Page Container -->
    <main id="page-content" data-page-content class="relative z-10">
      {pageTitle && (
        <h1 class="text-4xl font-semibold mb-8 text-center"></h1>
      )}

      <slot />
    </main>

    <!-- Accessibility: inert when sidebar is open -->
    <script is:inline>
      document.addEventListener("DOMContentLoaded", () => {
        const content = document.getElementById("page-content");

        document.addEventListener("sidebar:open", () => {
          content.setAttribute("aria-hidden", "true");
          content.setAttribute("inert", "");
        });

        document.addEventListener("sidebar:close", () => {
          content.removeAttribute("aria-hidden");
          content.removeAttribute("inert");
        });
      });
    </script>

    <SocialBar lang={lang} />
  </body>
</html>

```

---
### `layouts\FictionLayout.astro`
```astro
---
import BaseLayout from "./BaseLayout.astro";
const { frontmatter } = Astro.props;
---

<BaseLayout>

  <div class="fiction-content fiction-wrapper mx-auto max-w-3xl px-6 py-12 mt-12">

      <!-- 📌 Breadcrumbs -->
    <nav class="text-sm mb-6 opacity-80 ">
      <a href="/stories" class="hover:underline">Stories</a>
      <span class="mx-2">/</span>
      <span>{frontmatter.title}</span>
    </nav>

    <!-- Title -->
    <h1 class="text-3xl font-semibold mb-4 tracking-tight align-middle">
      {frontmatter.title}
    </h1>

    <!-- Description -->
    {frontmatter.description && (
      <p class="opacity-70 mb-6">{frontmatter.description}</p>
    )}

    <!-- Date -->
    {frontmatter.published && (
      <p class="text-sm opacity-50 mb-10">
        {frontmatter.published.toLocaleDateString()}
      </p>
    )}

    <!-- Story Body -->
    <article
      class="prose dark:prose-invert max-w-none
             bg-black/10 dark:bg-white/5 backdrop-blur-xl
             rounded-xl p-6 sm:p-10 leading-relaxed"
    >
      <slot />
    </article>

  </div>

</BaseLayout>

<style is:global>
  /* Increase realism for fiction text */
  .fiction-wrapper .prose p {
    margin-top: 1.15rem;
    margin-bottom: 1.15rem;
    text-indent: 1.5rem;
  }

  /* Do not indent after headings */
  .fiction-wrapper .prose h1 + p,
  .fiction-wrapper .prose h2 + p {
    text-indent: 0;
  }

  /* Dialogue lines starting with “–” should NOT indent */
  .fiction-wrapper .prose p:has(> strong:first-child),
  .fiction-wrapper .prose p:has(> span:first-child),
  .fiction-wrapper .prose p:has(> em:first-child),
  .fiction-wrapper .prose p:where(:first-child) {
    text-indent: 0;
  }
  pre {
  background: transparent !important;
  padding: 0 !important;
  margin: 0 !important;
  border: none !important;
  box-shadow: none !important;
  font-family: ui-serif, Georgia, Cambria, "Times New Roman", serif !important;
  white-space: pre-wrap !important;
}
.fiction-content ul,
.fiction-content li {
  list-style: none !important;
  margin: 0 !important;
  padding: 0 !important;
  color: inherit !important;
}

.fiction-content ul li::marker {
  display: none !important;
}

</style>

```

---
### `layouts\FictionLayoutFa.astro`
```astro
---
import BaseLayout from "./BaseLayout.astro";
import { formatDate } from "../utils/formatDate";

const { frontmatter, lang = "fa" } = Astro.props;

// Jalali date
const jalaliDate = frontmatter.date
  ? formatDate(new Date(frontmatter.date), "fa")
  : null;
---

<BaseLayout lang="fa">

  <main class="px-6 py-20 max-w-3xl mx-auto direction-rtl text-right font-[Vazirmatn]">

    <!-- Breadcrumb -->
    <nav class="text-sm mb-6 opacity-70">
      <a href="/fa/stories" class="hover:underline">
        داستان‌ها
      </a>
      <span class="mx-2">/</span>
      <span>{frontmatter.title}</span>
    </nav>

    <!-- Title -->
    <h1 class="text-3xl font-bold mb-4 tracking-tight">
      {frontmatter.title}
    </h1>

    <!-- Description -->
    {frontmatter.description && (
      <p class="opacity-80 mb-4 leading-relaxed">
        {frontmatter.description}
      </p>
    )}

    <!-- Date -->
    {jalaliDate && (
      <p class="text-sm opacity-60 mb-4">تاریخ: {jalaliDate}</p>
    )}

    <!-- External publication link (optional) -->
    {frontmatter.link && (
      <a
        href={frontmatter.link}
        class="text-blue-400 underline text-sm mb-6 block"
      >
        لینک انتشار
      </a>
    )}

    <!-- PDF File (optional) -->
    {frontmatter.file && (
      <div class="my-6">
        <object
          data={`/stories-fa/${frontmatter.file}`}
          type="application/pdf"
          class="w-full h-[70vh] rounded-xl border border-white/20"
        >
          <div class="text-center text-blue-300">
            PDF قابل نمایش نیست.
            <a
              href={`/stories-fa/${frontmatter.file}`}
              class="underline ml-2"
            >
              دانلود فایل
            </a>
          </div>
        </object>
      </div>
    )}

    <!-- MAIN STORY CONTENT -->
    <article
      class="prose prose-invert max-w-none leading-[2.2] text-lg
             bg-black/10 dark:bg-white/5 backdrop-blur-xl
             rounded-xl p-6 sm:p-10"
    >
      <slot />
    </article>

  </main>

</BaseLayout>

<style is:global>
  .prose p {
    margin-top: 1.1rem;
    margin-bottom: 1.1rem;
  }

  /* Persian text tends to need slightly taller line height */
  .prose {
    line-height: 2.1;
    font-family: Vazirmatn, sans-serif;
  }

  /* Prevent indenting after headings for Persian */
  .prose h1 + p,
  .prose h2 + p {
    text-indent: 0;
  }
</style>

```

---
### `layouts\Layout.astro`
```astro
<!doctype html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width" />
		<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
		<meta name="generator" content={Astro.generator} />
		<title>Astro Basics</title>
	</head>
	<body>
		<slot />
	</body>
</html>

<style>
	html,
	body {
		margin: 0;
		width: 100%;
		height: 100%;
	}
</style>

```

---
### `layouts\LayoutWiki.astro`
```astro
---
import Background from "../components/Astrogen.astro";
import Header from "../components/HeaderWiki.astro";
import "../styles/global.css";
const {
  pageTitle,
  lang = "en",     // 'en' or 'fa'
  pageClass = "",  // optional page-specific classes
} = Astro.props;
---

<html lang={lang} class="transition-none">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <slot name="head" />

    <!-- Unicode-friendly fonts -->
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css2?family=Noto+Serif&family=Noto+Sans+Symbols+2&display=swap"
    />

    <!-- Pre-paint theme -->
    <script is:inline>
      const isDark = localStorage.theme === "dark"
        || (!("theme" in localStorage)
            && window.matchMedia("(prefers-color-scheme: dark)").matches);

      document.documentElement.classList.toggle("dark", isDark);
    </script>

    <!-- Remove transition lock -->
    <script is:inline>
      window.addEventListener("load", () => {
        document.documentElement.classList.remove("transition-none");
      });
    </script>
  </head>

  <body>
    <Background />
    <Header lang={lang}/>

  <main
    class={[
      "pt-20 pb-20",
      "text-neutral-800 dark:text-neutral-100 leading-relaxed",
      pageClass
    ].join(" ")}
  >
    <slot />
 </main>
  </body>
</html>

```

---
### `layouts\MarkdownPostLayout.astro`
```astro
---
import BaseLayout from './BaseLayout.astro';
const { frontmatter } = Astro.props;
---
<BaseLayout pageTitle={frontmatter.title}>
    <p>{frontmatter.pubDate.toLocaleDateString()}</p>
    <p><em>{frontmatter.description}</em></p>
    <p>Written by: {frontmatter.author}</p>
    <img src={frontmatter.image.url} width="300" alt={frontmatter.image.alt} />

  <div class="tags">
    {frontmatter.tags.map((tag: string) => (
      <p class="tag"><a href={`/tags/${tag}`}>{tag}</a></p>
    ))}
  </div>

  <slot />
</BaseLayout>
<style>
  a {
    color: #00539F;
  }

  .tags {
    display: flex;
    flex-wrap: wrap;
  }

  .tag {
    margin: 0.25em;
    border: dotted 1px #a1a1a1;
    border-radius: .5em;
    padding: .5em 1em;
    font-size: 1.15em;
    background-color: #F8FCFD;
  }
</style>
```

---
### `layouts\PoetryLayout.astro`
```astro
---
import BaseLayout from "./BaseLayout.astro";

const { frontmatter } = Astro.props;
---

<BaseLayout>



  <div class="poetry-wrapper mx-auto max-w-2xl px-6 mt-28 mb-24 text-center">
      <!-- 📌 Breadcrumbs -->
    <nav class="text-sm mb-6 opacity-80 ">
      <a href="/poems" class="hover:underline">Poems</a>
      <span class="mx-2">/</span>
      <span>{frontmatter.title}</span>
    </nav>
    <!-- Title -->
    <h1 class="text-4xl font-serif mb-2 tracking-tight">
      {frontmatter.title}
    </h1>

    <!-- Poet -->
    {frontmatter.poet && (
      <p class="text-lg opacity-70 italic mb-2">by {frontmatter.poet}</p>
    )}

    <!-- Date -->
    {frontmatter.date && (
      <p class="text-sm opacity-50 mb-6">{frontmatter.date}</p>
    )}


        
    <!-- Poem body -->
    <article class="poem-body leading-relaxed text-lg font-serif whitespace-pre-wrap">
      <slot />
        <!-- Optional Image -->
        {frontmatter.image && (
          frontmatter.image.endsWith(".mp4") ? (
            <video 
              src={frontmatter.image}
              autoplay
              loop
              muted
              playsinline
              class="mx-auto mb-10 rounded-lg shadow-md max-h-80 object-contain"
            ></video>
          ) : (
            <img
              src={frontmatter.image}
              alt={frontmatter.title}
              class="mx-auto mb-10 rounded-lg shadow-md max-h-80 object-contain"
            />
          )
        )}
        
    </article>
    

        <!-- Loyalty / Notes -->
    {frontmatter.loyalty && (
    <p
      class="text-xs italic opacity-50 mb-8 leading-relaxed 
             [&_a]:underline [&_a]:opacity-80 hover:[&_a]:opacity-100"
      set:html={frontmatter.loyalty}
    ></p>    )}



  </div>

</BaseLayout>

<style is:global>
  /* Soft vertical rhythm for poetry */
  .poem-body p {
    margin: 1rem 0;
  }

  /* Ensure line breaks inside markdown render as poetry */
  .poem-body {
    white-space: pre-wrap !important;
  }

  /* Optional gentle fade */
  .poetry-wrapper {
    animation: fadeIn 0.8s ease both;
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }
</style>

```

---
### `lib\utils.ts`
```ts
import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

```

---
### `pages\about.astro`
```astro
---
import BaseLayout from "../layouts/BaseLayout.astro";
---

<BaseLayout>

  <main class="px-[clamp(1rem,4vw,4rem)] py-24 
               text-neutral-800 dark:text-neutral-100
               max-w-4xl mx-auto leading-relaxed">

    <!-- Heading -->
    <h1 class="text-4xl font-bold mb-12 tracking-tight text-center">
      About Me
    </h1>

    <!-- Card -->
    <section
      class="rounded-3xl p-8 mb-20
             bg-white/10 dark:bg-black/20 backdrop-blur-xl
             border border-white/20 shadow-xl
             transition-all">

      <h2 class="text-2xl font-semibold mb-6">Hi, I’m Ali Ghorbani AKA “Coughy”</h2>

      <p class="mb-6">
        I write fiction, poetry, research papers, and develop experimental tools across
        philosophy, linguistics, computation, and consciousness studies.  
        My work spans many domains, but all share the same theme:
        <strong>breaking inherited structures</strong> — whether linguistic, conceptual, or computational — 
        to see what grows in the cracks.
      </p>

      <p class="mb-6">
        I explore intersections between human cognition, altered states, language, and
        machine intelligence. I also build software tools, write experimental poetry,
        and maintain <a href="/wiki" class="text-blue-600 dark:text-blue-400 underline">my online wiki</a>
        documenting altered states of consciousness.
      </p>

      <p class="mb-6">
        Some of my projects include:
      </p>

      <ul class="list-disc pl-6 space-y-2 mb-6">
        <li><strong>Contraculator</strong> — a philosophical numerical system.</li>
        <li><strong>Flatshot</strong> — flatten entire codebases for AI processing.</li>
        <li>
          <strong>Fa_Docs</strong> — a Persian typography extension for Google Docs.
        </li>
        <li>
          <strong>Enpsyclopedia</strong> — a conceptual database on consciousness.
        </li>
      </ul>

      <p class="mb-6">
        My work often mixes formal structure with surrealistic or playful elements.
        Whether in code or poetry, I focus on <strong>rewiring assumptions</strong> —
        seeing what happens when you loosen a system from its historical constraints.
      </p>

      <p class="opacity-70">
        If you'd like to collaborate, talk, or ask questions:
        you can find me on Twitter, GitHub, or Telegram.
      </p>

    </section>

    <!-- Optional Portrait / Photo Block 
    <section
      class="w-full rounded-3xl overflow-hidden 
             bg-white/10 dark:bg-black/20 backdrop-blur-xl
             border border-white/20 shadow-xl">
      <img 
        src="/images/profile-placeholder.jpg"
        alt="Ali Ghorbani"
        class="w-full h-80 object-cover opacity-90"
      />
    </section>-->

  </main>

</BaseLayout>

```

---
### `pages\animation.astro`
```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
const pageTitle = "Home Page";
---
<BaseLayout>
</BaseLayout>
```

---
### `pages\art.astro`
```astro

```

---
### `pages\blog.astro`
```astro
---
import { getCollection } from "astro:content";
import BaseLayout from "../layouts/BaseLayout.astro";
import BlogPost from "../components/BlogPost.astro";

const pageTitle = "My Astro Learning Blog";
const allPosts = await getCollection("blog");
---

<BaseLayout>
  <section class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-16 text-white">
    <header class="mb-10 text-center">
      <h1 class="text-4xl font-extrabold tracking-tight mb-3 bg-clip-text text-transparent bg-linear-to-r from-blue-400 to-purple-500">
        {pageTitle}
      </h1>
      <p class="text-lg text-white/80">
        This is where I’ll share posts about my journey learning Astro.
      </p>
    </header>

    <ul class="space-y-6">
      {
        allPosts.map((post) => (
          <li
            class="p-6 bg-white/10 border border-white/20 backdrop-blur-md rounded-2xl shadow-md hover:bg-white/15 transition-all duration-300 ease-in-out"
          >
            <BlogPost
              url={`/posts/${post.id}/`}
              title={post.data.title}
            />
          </li>
        ))
      }
    </ul>
  </section>
</BaseLayout>

```

---
### `pages\index.astro`
```astro
---
import BaseLayout from "../layouts/BaseLayout.astro";
---

<BaseLayout>

<main class="relative text-neutral-800 dark:text-neutral-100">

  <!-- ================================
       Background subtle animation
  ================================= -->
  <div class="pointer-events-none fixed inset-0 z-0 opacity-50">
    <div class="absolute inset-0 bg-linear-to-br from-purple-500/10 via-blue-500/10 to-pink-500/10 blur-3xl animate-pulse-slow"></div>
  </div>

  <!-- ================================
       HERO SECTION
  ================================= -->
  <section class="relative z-10 flex flex-col items-center justify-center 
                  text-center pt-48 pb-32 px-4">

    <h1 class="text-6xl md:text-7xl font-semibold tracking-tight mb-6 drop-shadow-lg">
      coughy<span class="opacity-50 bg-linear-to-r from-blue-500 to-purple-500 bg-clip-text text-transparent">.</span>net
    </h1>


    <p class="text-xl md:text-2xl opacity-80 max-w-2xl leading-relaxed">
      Fiction · Research · Consciousness · Tools  
    </p>
  </section>


  <!-- ================================
       GRID OF THREE PORTAL SECTIONS
  ================================= -->
  <section class="relative z-10 max-w-7xl mx-auto px-6 pb-32">

    <div class="grid gap-10 
                md:grid-cols-2 
                lg:grid-cols-3">

      <!-- Fiction & Poetry -->
      <a href="/literature"
         class="group rounded-3xl p-8 bg-white/10 dark:bg-black/20
                border border-white/20 backdrop-blur-xl shadow-lg
                hover:bg-white/20 dark:hover:bg-black/30
                hover:-translate-y-1 hover:shadow-2xl
                transition-all duration-500 cursor-pointer">
        
        <h2 class="text-2xl font-semibold mb-4">Fiction & Poetry</h2>

        <p class="opacity-80 leading-relaxed">
          Stories, Poems, and poetic explorations.
        </p>

        <div class="mt-6 text-blue-300 opacity-0 group-hover:opacity-100
                    transition-all">Explore →</div>
      </a>


      <!-- Projects & Tools -->
      <a href="/projects"
         class="group rounded-3xl p-8 bg-white/10 dark:bg-black/20
                border border-white/20 backdrop-blur-xl shadow-lg
                hover:bg-white/20 dark:hover:bg-black/30
                hover:-translate-y-1 hover:shadow-2xl
                transition-all duration-500 cursor-pointer">
        
        <h2 class="text-2xl font-semibold mb-4">Projects & Tools</h2>

        <p class="opacity-80 leading-relaxed">
          Software, experiments, and philosophical tools.
        </p>

        <div class="mt-6 text-blue-300 opacity-0 group-hover:opacity-100
                    transition-all">Explore →</div>
      </a>


      <!-- Research & Ideas -->
      <a href="/research"
         class="group rounded-3xl p-8 bg-white/10 dark:bg-black/20
                border border-white/20 backdrop-blur-xl shadow-lg
                hover:bg-white/20 dark:hover:bg-black/30
                hover:-translate-y-1 hover:shadow-2xl
                transition-all duration-500 cursor-pointer">
        
        <h2 class="text-2xl font-semibold mb-4">Research & Ideas</h2>

        <p class="opacity-80 leading-relaxed">
          Papers, studies, and consciousness analysis—mapping inner worlds
          with structured insight.
        </p>

        <div class="mt-6 text-blue-300 opacity-0 group-hover:opacity-100 
                    transition-all">Explore →</div>
      </a>

    </div>
  </section>


  <!-- ================================
       ROTATING QUOTE BLOCK
       “Breaking inherited structures to see what grows in the cracks.”
  ================================= -->
  <section class="relative z-10 pb-32 px-6 flex justify-center back">
    <blockquote
      class="max-w-3xl text-center text-xl md:text-2xl font-light
             opacity-80 leading-relaxed italic"
    >
      To be honest, I don't fully understand what coughy.net is all about.
    </blockquote>
  </section>

</main>

</BaseLayout>

<style is:global>
  @keyframes pulse-slow {
    0% { opacity: 0.3; transform: scale(1); }
    50% { opacity: 0.6; transform: scale(1.05); }
    100% { opacity: 0.3; transform: scale(1); }
  }
</style>

```

---
### `pages\LightMeNow.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Hue Light</title>
  <style>
    html, body {
      margin: 0;
      height: 100%;
      width: 100%;
      background-color: hsl(0, 100%, 50%);
      overflow: hidden;
    }

    #controls {
      position: fixed;
      bottom: 2%;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      align-items: center;
      gap: 10px;
      background: rgba(0, 0, 0, 0.4);
      padding: 6px 12px;
      border-radius: 10px;
      backdrop-filter: blur(6px);
    }

    input[type="range"] {
      width: 100px;
      appearance: none;
      background: transparent;
      cursor: pointer;
    }

    input[type="range"]::-webkit-slider-runnable-track {
      height: 6px;
      background: linear-gradient(to right,
        hsl(0, 100%, 50%), hsl(60, 100%, 50%),
        hsl(120, 100%, 50%), hsl(180, 100%, 50%),
        hsl(240, 100%, 50%), hsl(300, 100%, 50%), hsl(360, 100%, 50%)
      );
      border-radius: 3px;
    }

    input[type="range"]::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: white;
      border: 1px solid #000;
      margin-top: -3px;
    }

    button {
      background: rgba(255, 255, 255, 0.2);
      color: white;
      border: 1px solid #ccc;
      border-radius: 6px;
      padding: 4px 10px;
      cursor: pointer;
      font-size: 0.9em;
    }

    button:hover {
      background: rgba(255, 255, 255, 0.3);
    }
  </style>
</head>
<body>
  <div id="controls">
    <input type="range" id="hue" min="0" max="360" value="0" />
    <button id="animate">▶</button>
    <input type="range" id="speed" min="1" max="100" value="30" />
  </div>

  <script>
    const hue = document.getElementById("hue");
    const speed = document.getElementById("speed");
    const animateBtn = document.getElementById("animate");

    let animation = null;
    let hueValue = 0;

    function updateColor() {
      document.body.style.backgroundColor = `hsl(${hueValue}, 100%, 50%)`;
    }

    hue.addEventListener("input", () => {
      hueValue = parseInt(hue.value);
      updateColor();
    });

    animateBtn.addEventListener("click", () => {
      if (animation) {
        cancelAnimationFrame(animation);
        animation = null;
        animateBtn.textContent = "▶";
      } else {
        animateBtn.textContent = "⏸";
        animateLoop();
      }
    });

    function animateLoop() {
      hueValue = (hueValue + speed.value / 50) % 360;
      hue.value = hueValue;
      updateColor();
      animation = requestAnimationFrame(animateLoop);
    }

    updateColor();
  </script>
</body>
</html>

```

---
### `pages\partners.astro`
```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
const pageTitle = "Home Page";
---
<BaseLayout>
</BaseLayout>
```

---
### `pages\projects.astro`
```astro
---
import BaseLayout from "../layouts/BaseLayout.astro";

const projects = [
  {
    title: "Contraculator",
    description:
      "A philosophical calculator free from most evolutionary assumptions. You must first construct its numeric system from scratch in order to use it.",
    github: "https://github.com/wr3yth/Contraculator",
    demo: "https://wr3yth.github.io/Contraculator/"
  },

  {
    title: "Flatshot",
    description:
      "Feed entire projects into LLMs without mess. Flatshot flattens any project into a single machine/human-readable file, ignoring irrelevant data.",
    github: "https://github.com/wr3yth/Flatshot"
  },

  {
    title: "🇮🇷 Fa_Docs | گوگل فاکس",
    description:
      "A Google Docs add-on that brings advanced Persian (Farsi) typography & numbering features — fully RTL-compatible.",
    link: "https://workspace.google.com/marketplace/app/farsi_tools/xxxxxxxx"
  },

  {
    title: "Enpsyclopedia of Altered States of Consciousness",
    description:
      "My ongoing documenting of altered states of consciousness, phenomenology, and psychedelic cognition.",
    link: "/wiki"
  },
      {
    title: "LightMeNow",
    description: "web based RGB screen lighting.",
    github: "https://github.com/wr3yth/LightMeNow",
    demo: "/LightMeNow.html"
  },
];
---

<BaseLayout>
  <main class="w-full px-[clamp(1rem,4vw,4rem)] py-24 
               text-neutral-800 dark:text-neutral-100">

    <h1 class="text-4xl font-bold text-center mb-16 tracking-tight">
      My Projects
    </h1>

    <div
      class="grid gap-10 
             sm:grid-cols-2 
             lg:grid-cols-3 
             xl:grid-cols-4 
             mx-auto max-w-[2000px]"
    >
      {projects.map((p) => (
        <div
          class="rounded-3xl p-6 
                 bg-white/30 dark:bg-black/20 backdrop-blur-xl
                 border border-white/20 shadow-lg
                 transition-all duration-500 
                 hover:bg-white/20 dark:hover:bg-black/30
                 hover:-translate-y-1 hover:shadow-2xl
                 flex flex-col justify-between"
        >
          <div>
            <h2 class="text-xl font-semibold mb-3">{p.title}</h2>
            <p class="text-[0.95rem] opacity-90 leading-relaxed mb-6">
              {p.description}
            </p>
          </div>

          <div class="mt-auto flex flex-wrap gap-3">

            {p.link && (
              <a
                href={p.link}
                class="px-4 py-2 rounded-full text-sm font-medium
                       bg-blue-500/20 hover:bg-blue-500/30
                       dark:bg-blue-500/30 dark:hover:bg-blue-500/40
                       border border-blue-400/40
                       transition-all"
                target="_blank"
              >
                Link
              </a>
            )}

            {p.github && (
              <a
                href={p.github}
                class="px-4 py-2 rounded-full text-sm font-medium
                       bg-gray-500/20 hover:bg-gray-500/30
                       dark:bg-gray-500/30 dark:hover:bg-gray-500/40
                       border border-gray-400/40
                       transition-all"
                target="_blank"
              >
                GitHub
              </a>
            )}

            {p.demo && (
              <a
                href={p.demo}
                class="px-4 py-2 rounded-full text-sm font-medium
                       bg-purple-500/20 hover:bg-purple-500/30
                       dark:bg-purple-500/30 dark:hover:bg-purple-500/40
                       border border-purple-400/40
                       transition-all"
                target="_blank"
              >
                Live Demo
              </a>
            )}

          </div>
        </div>
      ))}
    </div>

  </main>
</BaseLayout>

```

---
### `pages\rss.xml.js`
```js
import rss from '@astrojs/rss';

import { getCollection } from 'astro:content';

export async function GET(context) {
  const posts = await getCollection("blog");
  return rss({
    title: 'Astro Learner | Blog',
    description: 'My journey learning Astro',
    site: 'https://coughy.net',
    items: posts.map((post) => ({
      title: post.data.title,
      pubDate: post.data.pubDate,
      description: post.data.description,
      link: `/posts/${post.id}/`,
    })),
    customData: `<language>en-us</language>`,
  })
}
```

---
### `poems\Sum Things Up.md`
```md
---
title: "Sum Things Up"
poet: "Coughy"
date: "11 Nov 2025"
loyalty: 'Inspired by a poem known as Bokonim, by <a href="https://ekhtesari.com" target="_blank">Fatehem Ekhtesari</a>'
image: "/public/images/sum.png"
---
<pre>
   W
           ∑ things ⇧
 O
S
</pre>



  


Eeny, meeny, miney, moe! hands out, it's your turn! 
Big, bad, you’re wolf now! Let’s play some "wild" thing

Way past the backyards, houses and barnyards
No time for check things: heads up! just "run" thing

No phone, no backpacks, chase me like wolf packs
Don’t eat me just yet... play me like a “prey” thing

Lure me through sub-ways, slip out of sightses
come hide in lush here, hush… feel our 'this' thing

Your taste lingers on, teeth on my tongue
Heart-rate is punching, chewed up like 'pun' thing

waiting for a bus, with no extra fuss
Door slides to the left, climb up for "ride" thing

Tough seats, our soft ass, rear-view is dim glass
let nerves be nervous, restless for "wait" thing

got "nowhere" from "where?", “what now?” we're here
Less light at evening, trains are on "rail" thing


"two" with no tickets, destined to do tricks
hums syncs with rail sound, makes it like a “song” thing 


Pick some full pockets, don't wake them "up" thing
slip through their shadow, they will miss"Not" thing

Back into the crowds, city light and crows
Freeways and fast lanes, make haste on “walk” thing

Thin way through cars, no red/green lights 
Steps are predestined, death can be a "will" thing

Stay close and keep right, don't lose my sight 
No rush, no reason, we’re down for a 'late' thing

Sandwiched by hunger, devoured by the burger
lunching and dining, fold'em as "one" thing

Night seeps in slowly, darkness glow coldly
Crawl back to the shelter, warm me with a "hug" thing

moon shines on “lust” thing, "no one but us" thing
Life can be dealt with, but "fuck" makes it "fun" thing

you touch my back now, whisper me "some"-thing:
-my turn is over, wolf up, do a "what?" thing
      
```

---
### `poems\Violent Bloom.md`
```md
---
title: "Violent Bloom"
poet: "Coughy"
date: "20 Oct 2024"
image: "/public/gifs/bloom.mp4"
loyalty: 'gif made by <a href="https://www.reddit.com/user/StingrayZ" target="_blank">StingrayZ</a>'
---

Violets are red, and Roses are blue
Life can be violent, yet flowers get through
Unleash your petals, get injured by thorns
When pain is built up, just try shifting hue

      
```

---
### `stories\cry_as_punishment.md`
```md
---
title: "Cry as Punishment"
description: "(English version not published)"
category: "flash fiction"
---






The moment I opened the door, I couldn’t believe my eyes.
 My whole world collapsed upon my head within seconds.  
 Never ... ever... in a million years did I expect something like that from Tyler and Olivia.  
 And there they were: those filthy scumbags, standing frozen, staring back at me like deers in headlights.

God, I wish I hadn’t seen them.  
And the worst part? My dad saw it too.

I don’t remember how we got into the car.  
 One moment we were living the moment of truth—one that nearly gave my father a stroke—and the next, we were driving.  
 I splashed some water on my face using the little sink inside the dashboard.  
 Still stunned. Still spinning. My lungs felt crushed. I couldn’t even look dad in the eyes.

He was more rattled than I was—still hadn’t processed what we saw.  
 After a long, sick silence, he turned to me and growled:

-  “This what you wanted? Huh? Is *this* what you wanted? I told you they’re not our kind. Rotten, sleazy fucks.”

I couldn’t take it anymore. I broke.  
 Tears burst out like a cracked pipe.

I had trusted Tyler and Olivia with all my heart.  
 We were just a normal little three-way family.  
 I never thought it would end up like this.

- “Maybe… just maybe, we could give them another cha—”  
-  “Shut. Your. God. Fucking. Damn. Mouth. I don’t want to hear a single word.”  
- “But they—”  
-  “Aaagh god. now you tryna defend a lowlife cuck and a shameless bitch? you could've married better people Sarah... I knew they were not decent since folks. I knew it.” 

Every time I blinked, the scene came back.  
 Sharp. Vivid. Unshakable.

When we pulled up to the house, Dad hung the car beside the house on the car-hanger and we climbed out.  
 Mr. Dickson, our overly cheerful neighbor, was walking over.

-  “Not a word in front of him. Capiche?

Dad muttered through his teeth.

I nodded. “Okay.”

Mr. Dickson said Hi and made out with dad. I reluctantly took down his pants and sucked him off as a sign of respect.

 He seemed satisfied, placed a hand gently on my head, fingers grazing my scalp, and asked with false concern:

-  “Something bothering you sweetheart?”

I didn’t reply.  
 Just covered my eyes with my elbow, pushed open the front door through tears, and brushed past Mom—who was carrying a plate of rice.  
 I went straight to my room and locked the door behind.  
 Sat down to keep on crying.

A little later, I heard the door slam.  
 Then the shouting began.

I clamped both hands over my ears, but could still hear everything.

-  “What happened, Clint? What’s wrong with Sarah? Did something happen?”  
-  “What do you *think* happened? That fucking bastard… in his own fucking house.”  
- “In his own house *what*? Just say it.”  
- “they were…”

The sound of the plate of rice falling and shattering, *split my chest open.*

-  “No. No. No. I don’t believe it. I just can’t.”  
- “Sarah opened the door. We saw everything.”  
- “You’re lying.”  
- “I wish I was. But it’s true — the guy was fucking his own wife. In their own fucking house.”

The end.
```

---
### `stories\make love, not with eggs.md`
```md
---
title: "make love, not with eggs"
description: "A love story about ordinary fish - (not published)"
---


          
          
  
    
      
       






Most of the time, it's like… I don't know. It's like there's this thick, black cloud covering everything. Like we see the world, but we don't really see the world, you know?  
We're all just stumbling around. Directionless.No sense of meaning.No sense of purpose. I know that might sound super depressing, but honestly, I think it's a good thing. Because it makes us appreciate the other times.  
Those brief, transcendent moments when the lights flicker on, the black cloud parts, and you see the world for what it really is.

     - Oh…

And suddenly there's meaning. Suddenly there's purpose.

     - So, uh, do you… Oh, shit. Shit. Shit, shit, shit.

If you're lucky, you'll experience this once in your lifetime.

     - Oops! 
Goddamn, that was…

     - That was smooth.  
     - wait, what?

For me… So smooth… It happened three times.  
The **first** was the day I met her.

     - Uh, Sorry for the eggs.  
     - It’s okay. Happens to all females.  
     - so… wanna try them or?

And the **second** one… was the day I ate her.

She had been avoiding me for days, maybe weeks. I lost track of time in the chase, in the ache of wanting something I couldn’t have. Then, suddenly, she stopped running. I found her hovering near a fallen branch, her gills flaring, her body still.

    - You don’t swim with me anymore.

    - Maybe I’m tired.

    - Of me?

    - Of everything.

She flicked her tail—not for me, but to go ahead, like she was already somewhere else. And yet, for the first time, she didn’t try to disappear. She swam slowly, deliberately, as if waiting to see if I would follow.

And I did.

I trailed her through the water, watching the way she moved her taled ass. She wasn’t running. Nor she was hiding. But something in her seemed… resigned. I wanted to reach out, to press against her side, to make her *feel* something—anything—but all I could do was stay close, my shadow slipping over hers in the dim light.

    - Why are you doing this?

    - Doing what?

    - This. Following me. Chasing me. Why don’t you do what everybody else does?

She turned to face me then, and for this time, I saw a different kind of exhaustion in her eyes.

    - Because I fucking love you.

She let out a sharp exhale, something between a laugh and a sigh.

    - Me? For what?

    - I don’t know.

    - Don’t I leave enough eggs for you? Just do your thing like everybody else. It’s the way it has been forever.

    - Now you’re starting to sound like everybody else.

    - Maybe I *am* like everybody else. *Maybe you’re* the one with the problem.

Her voice cut through the water, sharp and cold.

    - Just don’t talk to me anymore. Iwish I never laid eggs while you were around. just Have fun with the eggs—mine or any other one’s eggs—but don’t creep me out following my tailed ass everywhere. 

   - is that it? You want me to get laid over anybody’s dirty eggs and get drowned by a meaningless lust and pleasure on top of that slimey goo and let myself go? 

She turned away, clearly offended. Swam forward. And this time, she wasn’t waiting for me to follow.

But I did.

I don’t know why. Maybe I had to apologize to change her mind. Maybe I wanted her to take back what she said. Maybe I wanted to understand why she looked at me like that—like I was something she didn’t recognize. But the thing is: I really did mean what I actually said. No regrets. maybe I was just ready to let go and do what others do. Just fucking colds eggs, or better to say: jerking off to eggs to make them fertile to reproduce what evolution has destined.

But I kept following.

Not beside her, not like before. This time, I stayed back, drifting just far enough to keep her butt in sight without making her turn and snap at me again. She didn’t look back. Maybe she thought I’d finally given up. Maybe she wanted to believe that.

But I hadn’t.

She moved like she always did—fluid, effortless, her silver-speckled tail cutting through the water like a ribbon unraveling into the dark. It was hypnotic. The slow flicks, the slight curves, her butthole, the way the currents shaped themselves behinf her ass. I had spent so long wanting her, chasing her, aching for the moments she let me be near, and now… now I was invisible.

And somehow, that made it easier.

I let myself enjoy it. The sight of her tail ahead of me, the shimmer of her scales catching faint light from the surface. The way the water bent around her body, parting gently before closing in again, like it belonged to her. Also she was pooping out eggs and feces off his anus from time to time. But since that moment, I didn’t keep myself from having a bit of pleasure while swimming through her excrement eggs. Her eggs smelled like her body.

I could have stayed like that forever.

But then—

Something shifted.

A pulse, deep inside me. Not a thought, not a feeling—something older, something nameless, something I couldn’t stop even if I tried.

I got wildly turned on. 

My body moved before I even knew what I was doing.

One second, I was following her ass. The next, I was trying to rip her body off part by part.

And she—

She didn’t see it coming.

I felt her before I even understood. The familiar shape, the fins, the soft press of her against the roof of my mouth. She struggled, but gave up. Every single one of  her body folding into the dark.

And then—

For the second time in my life, I felt a joyful enlightenment. While she was dead and ready to be eaten. Also the thirt time this happened was when I pooped her out and had a moment of clarity while contemplating about the philosophy of love. Flowing out smoothly from my anus.

                                    The end
```

---
### `stories-fa\bedoone_khodahafezi.md`
```md
---
title: "بدون خداحافظی"
description: "منتشر شده در جلد دوم کتاب «فاطمه فاطمه است» - صفحه‌ی ۱۰۲"

published: true
date: "2025-01-01"

file: "/pdf/bedoone_khodahafezi.pdf"
link: "https://example.com/fateme_fateme_ast"
image: "/images/bedoone_khodahafezi.jpg"
---

```

---
### `stories-fa\khianat_va_mokafat.md`
```md
---
title: "خیانت و مکافات"
description: "منتشر شده در ویژه‌نامه‌ی طنز مجله‌ی مستقل ادبیات ایران - صفحه‌ی ۱۱۶"

published: true
date: "2025-01-01"

file: "/pdf/bedoone_khodahafezi.pdf"
link: "https://example.com/fateme_fateme_ast"
image: "/images/Cry As Punishment Fa.jpg"
---

          
  
    
      
       






Most of the time, it's like… I don't know. It's like there's this thick, black cloud covering everything. Like we see the world, but we don't really see the world, you know?  
We're all just stumbling around. Directionless.No sense of meaning.No sense of purpose. I know that might sound super depressing, but honestly, I think it's a good thing. Because it makes us appreciate the other times.  
Those brief, transcendent moments when the lights flicker on, the black cloud parts, and you see the world for what it really is.

     - Oh…

And suddenly there's meaning. Suddenly there's purpose.

     - So, uh, do you… Oh, shit. Shit. Shit, shit, shit.

If you're lucky, you'll experience this once in your lifetime.

     - Oops! 
Goddamn, that was…

     - That was smooth.  
     - wait, what?

For me… So smooth… It happened three times.  
The **first** was the day I met her.

     - Uh, Sorry for the eggs.  
     - It’s okay. Happens to all females.  
     - so… wanna try them or?

And the **second** one… was the day I ate her.

She had been avoiding me for days, maybe weeks. I lost track of time in the chase, in the ache of wanting something I couldn’t have. Then, suddenly, she stopped running. I found her hovering near a fallen branch, her gills flaring, her body still.

    - You don’t swim with me anymore.

    - Maybe I’m tired.

    - Of me?

    - Of everything.

She flicked her tail—not for me, but to go ahead, like she was already somewhere else. And yet, for the first time, she didn’t try to disappear. She swam slowly, deliberately, as if waiting to see if I would follow.

And I did.

I trailed her through the water, watching the way she moved her taled ass. She wasn’t running. Nor she was hiding. But something in her seemed… resigned. I wanted to reach out, to press against her side, to make her *feel* something—anything—but all I could do was stay close, my shadow slipping over hers in the dim light.

    - Why are you doing this?

    - Doing what?

    - This. Following me. Chasing me. Why don’t you do what everybody else does?

She turned to face me then, and for this time, I saw a different kind of exhaustion in her eyes.

    - Because I fucking love you.

She let out a sharp exhale, something between a laugh and a sigh.

    - Me? For what?

    - I don’t know.

    - Don’t I leave enough eggs for you? Just do your thing like everybody else. It’s the way it has been forever.

    - Now you’re starting to sound like everybody else.

    - Maybe I *am* like everybody else. *Maybe you’re* the one with the problem.

Her voice cut through the water, sharp and cold.

    - Just don’t talk to me anymore. Iwish I never laid eggs while you were around. just Have fun with the eggs—mine or any other one’s eggs—but don’t creep me out following my tailed ass everywhere. 

   - is that it? You want me to get laid over anybody’s dirty eggs and get drowned by a meaningless lust and pleasure on top of that slimey goo and let myself go? 

She turned away, clearly offended. Swam forward. And this time, she wasn’t waiting for me to follow.

But I did.

I don’t know why. Maybe I had to apologize to change her mind. Maybe I wanted her to take back what she said. Maybe I wanted to understand why she looked at me like that—like I was something she didn’t recognize. But the thing is: I really did mean what I actually said. No regrets. maybe I was just ready to let go and do what others do. Just fucking colds eggs, or better to say: jerking off to eggs to make them fertile to reproduce what evolution has destined.

But I kept following.

Not beside her, not like before. This time, I stayed back, drifting just far enough to keep her butt in sight without making her turn and snap at me again. She didn’t look back. Maybe she thought I’d finally given up. Maybe she wanted to believe that.

But I hadn’t.

She moved like she always did—fluid, effortless, her silver-speckled tail cutting through the water like a ribbon unraveling into the dark. It was hypnotic. The slow flicks, the slight curves, her butthole, the way the currents shaped themselves behinf her ass. I had spent so long wanting her, chasing her, aching for the moments she let me be near, and now… now I was invisible.

And somehow, that made it easier.

I let myself enjoy it. The sight of her tail ahead of me, the shimmer of her scales catching faint light from the surface. The way the water bent around her body, parting gently before closing in again, like it belonged to her. Also she was pooping out eggs and feces off his anus from time to time. But since that moment, I didn’t keep myself from having a bit of pleasure while swimming through her excrement eggs. Her eggs smelled like her body.

I could have stayed like that forever.

But then—

Something shifted.

A pulse, deep inside me. Not a thought, not a feeling—something older, something nameless, something I couldn’t stop even if I tried.

I got wildly turned on. 

My body moved before I even knew what I was doing.

One second, I was following her ass. The next, I was trying to rip her body off part by part.

And she—

She didn’t see it coming.

I felt her before I even understood. The familiar shape, the fins, the soft press of her against the roof of my mouth. She struggled, but gave up. Every single one of  her body folding into the dark.

And then—

For the second time in my life, I felt a joyful enlightenment. While she was dead and ready to be eaten. Also the thirt time this happened was when I pooped her out and had a moment of clarity while contemplating about the philosophy of love. Flowing out smoothly from my anus.

                                    The end
```

---
### `stories-fa\tasmim_baraye_cobra_11.md`
```md
---
title: "تصمیم برای کبری ۱۱"
description: "منتشر شده در  در کتاب همسایه ۳ -  صفحه‌ی ۳۱۳"

published: true
date: "2025-01-01"

file: "/pdf/bedoone_khodahafezi.pdf"
link: "https://example.com/fateme_fateme_ast"
image: "/images/tasmim 11.jpg" 
---

          
  






Most of the time, it's like… I don't know. It's like there's this thick, black cloud covering everything. Like we see the world, but we don't really see the world, you know?  
We're all just stumbling around. Directionless.No sense of meaning.No sense of purpose. I know that might sound super depressing, but honestly, I think it's a good thing. Because it makes us appreciate the other times.  
Those brief, transcendent moments when the lights flicker on, the black cloud parts, and you see the world for what it really is.

     - Oh…

And suddenly there's meaning. Suddenly there's purpose.

     - So, uh, do you… Oh, shit. Shit. Shit, shit, shit.

If you're lucky, you'll experience this once in your lifetime.

     - Oops! 
Goddamn, that was…

     - That was smooth.  
     - wait, what?

For me… So smooth… It happened three times.  
The **first** was the day I met her.

     - Uh, Sorry for the eggs.  
     - It’s okay. Happens to all females.  
     - so… wanna try them or?

And the **second** one… was the day I ate her.

She had been avoiding me for days, maybe weeks. I lost track of time in the chase, in the ache of wanting something I couldn’t have. Then, suddenly, she stopped running. I found her hovering near a fallen branch, her gills flaring, her body still.

    - You don’t swim with me anymore.

    - Maybe I’m tired.

    - Of me?

    - Of everything.

She flicked her tail—not for me, but to go ahead, like she was already somewhere else. And yet, for the first time, she didn’t try to disappear. She swam slowly, deliberately, as if waiting to see if I would follow.

And I did.

I trailed her through the water, watching the way she moved her taled ass. She wasn’t running. Nor she was hiding. But something in her seemed… resigned. I wanted to reach out, to press against her side, to make her *feel* something—anything—but all I could do was stay close, my shadow slipping over hers in the dim light.

    - Why are you doing this?

    - Doing what?

    - This. Following me. Chasing me. Why don’t you do what everybody else does?

She turned to face me then, and for this time, I saw a different kind of exhaustion in her eyes.

    - Because I fucking love you.

She let out a sharp exhale, something between a laugh and a sigh.

    - Me? For what?

    - I don’t know.

    - Don’t I leave enough eggs for you? Just do your thing like everybody else. It’s the way it has been forever.

    - Now you’re starting to sound like everybody else.

    - Maybe I *am* like everybody else. *Maybe you’re* the one with the problem.

Her voice cut through the water, sharp and cold.

    - Just don’t talk to me anymore. Iwish I never laid eggs while you were around. just Have fun with the eggs—mine or any other one’s eggs—but don’t creep me out following my tailed ass everywhere. 

   - is that it? You want me to get laid over anybody’s dirty eggs and get drowned by a meaningless lust and pleasure on top of that slimey goo and let myself go? 

She turned away, clearly offended. Swam forward. And this time, she wasn’t waiting for me to follow.

But I did.

I don’t know why. Maybe I had to apologize to change her mind. Maybe I wanted her to take back what she said. Maybe I wanted to understand why she looked at me like that—like I was something she didn’t recognize. But the thing is: I really did mean what I actually said. No regrets. maybe I was just ready to let go and do what others do. Just fucking colds eggs, or better to say: jerking off to eggs to make them fertile to reproduce what evolution has destined.

But I kept following.

Not beside her, not like before. This time, I stayed back, drifting just far enough to keep her butt in sight without making her turn and snap at me again. She didn’t look back. Maybe she thought I’d finally given up. Maybe she wanted to believe that.

But I hadn’t.

She moved like she always did—fluid, effortless, her silver-speckled tail cutting through the water like a ribbon unraveling into the dark. It was hypnotic. The slow flicks, the slight curves, her butthole, the way the currents shaped themselves behinf her ass. I had spent so long wanting her, chasing her, aching for the moments she let me be near, and now… now I was invisible.

And somehow, that made it easier.

I let myself enjoy it. The sight of her tail ahead of me, the shimmer of her scales catching faint light from the surface. The way the water bent around her body, parting gently before closing in again, like it belonged to her. Also she was pooping out eggs and feces off his anus from time to time. But since that moment, I didn’t keep myself from having a bit of pleasure while swimming through her excrement eggs. Her eggs smelled like her body.

I could have stayed like that forever.

But then—

Something shifted.

A pulse, deep inside me. Not a thought, not a feeling—something older, something nameless, something I couldn’t stop even if I tried.

I got wildly turned on. 

My body moved before I even knew what I was doing.

One second, I was following her ass. The next, I was trying to rip her body off part by part.

And she—

She didn’t see it coming.

I felt her before I even understood. The familiar shape, the fins, the soft press of her against the roof of my mouth. She struggled, but gave up. Every single one of  her body folding into the dark.

And then—

For the second time in my life, I felt a joyful enlightenment. While she was dead and ready to be eaten. Also the thirt time this happened was when I pooped her out and had a moment of clarity while contemplating about the philosophy of love. Flowing out smoothly from my anus.

                                    The end
```

---
### `stories-fa\vincenzo.md`
```md
---
title: "vincenzo"
description: "منتشر نشده - پیش‌نویس"

published: false
date: "2025-01-01"

file: "/pdf/vincenzo.pdf"
link: "https://example.com/fateme_fateme_ast"
image: "/images/vincenzo.png" 
---

          
  
```

---
### `stories-fa\اثاثیاست یک دست میز و صندلی نگران.md`
```md
---
title: "اثاثیاست یک دست میز و صندلی نگران"
description: "منتشر نشده - پیش‌نویس"

published: false
date: "2025-01-01"

file: "/pdf/اثاثیاست یک دست میز و صندلی نگران.pdf"

image: "/images/اثاثیاست یک دست میز و صندلی نگران.png" 
---

          
  
```

---
### `stories-fa\محل تبلیغات شما.md`
```md
---
title: "محل تبلیغات شما"
description: "منتشر نشده - پیش‌نویس"

published: false
date: "2025-01-01"

file: "/pdf/محل تبلیغات شما.pdf"
link: "https://example.com/fateme_fateme_ast"
image: "/images/محل تبلیغات شما.png" 
---

          
  
```

---
### `styles\global.css`
```css
/* -------------------------------------------------
   Tailwind Base Imports
------------------------------------------------- */
@import "tailwindcss";
@import "tw-animate-css";

/* -------------------------------------------------
   Light/Dark Variant Definition
------------------------------------------------- */
@custom-variant dark (&:is(.dark *));

/* -------------------------------------------------
   Theme Tokens (Tailwind v4 @theme)
------------------------------------------------- */
@theme {
  /* Background / Foreground */
  --color-background: rgb(var(--background));
  --color-foreground: rgb(var(--foreground));

  /* Main UI Colors */
  --color-primary: rgb(var(--primary));
  --color-primary-foreground: rgb(var(--primary-foreground));
  --color-secondary: rgb(var(--secondary));
  --color-secondary-foreground: rgb(var(--secondary-foreground));

  /* Borders / Inputs */
  --color-border: rgb(var(--border));
  --color-input: rgb(var(--input));

  /* Misc */
  --radius: 0.625rem;
}

/* -------------------------------------------------
   Light Theme
------------------------------------------------- */
:root {
  --background: 255 255 255;
  --foreground: 17 17 17;

  --primary: 90 106 255;
  --primary-foreground: 255 255 255;

  --secondary: 230 230 230;
  --secondary-foreground: 17 17 17;

  --border: 220 220 220;
  --input: 230 230 230;
}

/* -------------------------------------------------
   Dark Theme
------------------------------------------------- */
.dark {
  --background: 18 18 18;
  --foreground: 235 235 235;

  --primary: 150 170 255;
  --primary-foreground: 18 18 18;

  --secondary: 60 60 60;
  --secondary-foreground: 235 235 235;

  --border: 80 80 80;
  --input: 100 100 100;
}

/* -------------------------------------------------
   Base Layer
------------------------------------------------- */
@layer base {
  *, *::before, *::after {
    border-color: var(--color-border);
  }

  body {
    background-color: var(--color-background);
    color: var(--color-foreground);
  }
}

/* -------------------------------------------------
   Fix for Astro Code Blocks
------------------------------------------------- */
.astro-code {
  color: inherit !important;
}


```

---
### `types\wiki.ts`
```ts
export type WikiEntry = {
  id: string;
  data: { title: string };
  filePath: string;
};

export type TreeNode = {
  indexEntry: WikiEntry | null;
  pages: WikiEntry[];
  children: Map<string, TreeNode>;
};

```

---
### `utils\formatDate.ts`
```ts
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

```

---
### `wiki\Neurotransmitters\acetylcholine.fa.md`
```md
---
title: 'Acetylcholine'
slug: "acetylcholine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Acetylcholine

_Page coming soon._

```

---
### `wiki\Neurotransmitters\acetylcholine.md`
```md
---
title: 'Acetylcholine'
slug: "acetylcholine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Acetylcholine

_Page coming soon._

```

---
### `wiki\Neurotransmitters\amino-acids.fa.md`
```md
---
title: 'Amino acids'
slug: "amino-acids"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Amino acids

_Page coming soon._

```

---
### `wiki\Neurotransmitters\amino-acids.md`
```md
---
title: 'Amino acids'
slug: "amino-acids"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Amino acids

_Page coming soon._

```

---
### `wiki\Neurotransmitters\aminobutyric-acid.fa.md`
```md
---
title: 'γ-Aminobutyric acid'
slug: "aminobutyric-acid"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# γ-Aminobutyric acid

_Page coming soon._

```

---
### `wiki\Neurotransmitters\aminobutyric-acid.md`
```md
---
title: 'γ-Aminobutyric acid'
slug: "aminobutyric-acid"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# γ-Aminobutyric acid

_Page coming soon._

```

---
### `wiki\Neurotransmitters\catecholamines.fa.md`
```md
---
title: 'Catecholamines'
slug: "catecholamines"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Catecholamines

_Page coming soon._

```

---
### `wiki\Neurotransmitters\catecholamines.md`
```md
---
title: 'Catecholamines'
slug: "catecholamines"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Catecholamines

_Page coming soon._

```

---
### `wiki\Neurotransmitters\dopamine.fa.md`
```md
---
title: 'Dopamine'
slug: "dopamine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Dopamine

_Page coming soon._

```

---
### `wiki\Neurotransmitters\dopamine.md`
```md
---
title: 'Dopamine'
slug: "dopamine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Dopamine

_Page coming soon._

```

---
### `wiki\Neurotransmitters\epinephrine.fa.md`
```md
---
title: 'Epinephrine'
slug: "epinephrine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Epinephrine

_Page coming soon._

```

---
### `wiki\Neurotransmitters\epinephrine.md`
```md
---
title: 'Epinephrine'
slug: "epinephrine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Epinephrine

_Page coming soon._

```

---
### `wiki\Neurotransmitters\histamine.fa.md`
```md
---
title: 'Histamine'
slug: "histamine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Histamine

_Page coming soon._

```

---
### `wiki\Neurotransmitters\histamine.md`
```md
---
title: 'Histamine'
slug: "histamine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Histamine

_Page coming soon._

```

---
### `wiki\Neurotransmitters\l-glutamate.fa.md`
```md
---
title: 'L-Glutamate'
slug: "l-glutamate"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# L-Glutamate

_Page coming soon._

```

---
### `wiki\Neurotransmitters\l-glutamate.md`
```md
---
title: 'L-Glutamate'
slug: "l-glutamate"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# L-Glutamate

_Page coming soon._

```

---
### `wiki\Neurotransmitters\melatonin.fa.md`
```md
---
title: 'Melatonin'
slug: "melatonin"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Melatonin

_Page coming soon._

```

---
### `wiki\Neurotransmitters\melatonin.md`
```md
---
title: 'Melatonin'
slug: "melatonin"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Melatonin

_Page coming soon._

```

---
### `wiki\Neurotransmitters\monoamines.fa.md`
```md
---
title: 'Monoamines'
slug: "monoamines"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Monoamines

_Page coming soon._

```

---
### `wiki\Neurotransmitters\monoamines.md`
```md
---
title: 'Monoamines'
slug: "monoamines"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Monoamines

_Page coming soon._

```

---
### `wiki\Neurotransmitters\neurotransmitters.fa.md`
```md
---
title: 'Neurotransmitters'
slug: "neurotransmitters"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Neurotransmitters

_Page coming soon._

```

---
### `wiki\Neurotransmitters\neurotransmitters.md`
```md
---
title: 'Neurotransmitters'
slug: "neurotransmitters"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Neurotransmitters

_Page coming soon._

```

---
### `wiki\Neurotransmitters\norepinephrine.fa.md`
```md
---
title: 'Norepinephrine'
slug: "norepinephrine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Norepinephrine

_Page coming soon._

```

---
### `wiki\Neurotransmitters\norepinephrine.md`
```md
---
title: 'Norepinephrine'
slug: "norepinephrine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Norepinephrine

_Page coming soon._

```

---
### `wiki\Neurotransmitters\other.fa.md`
```md
---
title: 'Other'
slug: "other"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Other

_Page coming soon._

```

---
### `wiki\Neurotransmitters\other.md`
```md
---
title: 'Other'
slug: "other"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Other

_Page coming soon._

```

---
### `wiki\Neurotransmitters\peptides.fa.md`
```md
---
title: 'Peptides'
slug: "peptides"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Peptides

_Page coming soon._

```

---
### `wiki\Neurotransmitters\peptides.md`
```md
---
title: 'Peptides'
slug: "peptides"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Peptides

_Page coming soon._

```

---
### `wiki\Neurotransmitters\phenethylamine.fa.md`
```md
---
title: 'Phenethylamine'
slug: "phenethylamine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Phenethylamine

_Page coming soon._

```

---
### `wiki\Neurotransmitters\phenethylamine.md`
```md
---
title: 'Phenethylamine'
slug: "phenethylamine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Phenethylamine

_Page coming soon._

```

---
### `wiki\Neurotransmitters\phenethylamines.fa.md`
```md
---
title: 'Phenethylamines'
slug: "phenethylamines"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Phenethylamines

_Page coming soon._

```

---
### `wiki\Neurotransmitters\phenethylamines.md`
```md
---
title: 'Phenethylamines'
slug: "phenethylamines"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Phenethylamines

_Page coming soon._

```

---
### `wiki\Neurotransmitters\semax.fa.md`
```md
---
title: 'Semax'
slug: "semax"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Semax

_Page coming soon._

```

---
### `wiki\Neurotransmitters\semax.md`
```md
---
title: 'Semax'
slug: "semax"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Semax

_Page coming soon._

```

---
### `wiki\Neurotransmitters\serotonin.fa.md`
```md
---
title: 'Serotonin'
slug: "serotonin"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Serotonin

_Page coming soon._

```

---
### `wiki\Neurotransmitters\serotonin.md`
```md
---
title: 'Serotonin'
slug: "serotonin"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Serotonin

_Page coming soon._

```

---
### `wiki\Neurotransmitters\trace-amines.fa.md`
```md
---
title: 'Trace amines'
slug: "trace-amines"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Trace amines

_Page coming soon._

```

---
### `wiki\Neurotransmitters\trace-amines.md`
```md
---
title: 'Trace amines'
slug: "trace-amines"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Trace amines

_Page coming soon._

```

---
### `wiki\Neurotransmitters\tryptamine.fa.md`
```md
---
title: 'Tryptamine'
slug: "tryptamine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Tryptamine

_Page coming soon._

```

---
### `wiki\Neurotransmitters\tryptamine.md`
```md
---
title: 'Tryptamine'
slug: "tryptamine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Tryptamine

_Page coming soon._

```

---
### `wiki\Psychoactives\index.md`
```md
---
title: 'Psychoactives'
slug: "psychoactives"
lang: "en"
category: ''
weight: 1000
template: "wiki"
summary: ''
---

# Substances

_Page coming soon._

```

---
### `wiki\Psychoactives\Psychoactives.fa.md`
```md
---
title: 'Psychoactives'
slug: "psychoactives"
lang: "en"
category: ''
weight: 1000
template: "wiki"
summary: ''
---

# Substances

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Psychoactive_effects.fa.md`
```md
---
title: 'Effects'
slug: "effects"
lang: "en"
category: ''
weight: 1000
template: "wiki"
summary: ''
---

# Effects

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Psychoactive_effects.md`
```md
---
title: 'Effects'
slug: "effects"
lang: "en"
category: ''
weight: 1000
template: "wiki"
summary: ''
---

# Effects

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\addiction-suppression.fa.md`
```md
---
title: 'Addiction suppression'
slug: "addiction-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Addiction suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\addiction-suppression.md`
```md
---
title: 'Addiction suppression'
slug: "addiction-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Addiction suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\amnesia copy.md`
```md
---
title: 'Amnesia'
slug: "amnesia"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Amnesia

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\amnesia.fa copy.md`
```md
---
title: 'Amnesia'
slug: "amnesia"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Amnesia

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\amnesia.fa.md`
```md
---
title: 'Amnesia'
slug: "amnesia"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Amnesia

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\amnesia.md`
```md
---
title: 'Amnesia'
slug: "amnesia"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Amnesia

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\analysis-depression.fa.md`
```md
---
title: 'Analysis depression'
slug: "analysis-depression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Analysis depression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\analysis-depression.md`
```md
---
title: 'Analysis depression'
slug: "analysis-depression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Analysis depression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\analysis-enhancement.fa.md`
```md
---
title: 'Analysis enhancement'
slug: "analysis-enhancement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Analysis enhancement

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\analysis-enhancement.md`
```md
---
title: 'Analysis enhancement'
slug: "analysis-enhancement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Analysis enhancement

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\anhedonia.fa.md`
```md
---
title: 'Anhedonia'
slug: "anhedonia"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Anhedonia

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\anhedonia.md`
```md
---
title: 'Anhedonia'
slug: "anhedonia"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Anhedonia

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\anxiety-suppression.fa.md`
```md
---
title: 'Anxiety suppression'
slug: "anxiety-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Anxiety suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\anxiety-suppression.md`
```md
---
title: 'Anxiety suppression'
slug: "anxiety-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Anxiety suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\anxiety.fa.md`
```md
---
title: 'Anxiety'
slug: "anxiety"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Anxiety

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\anxiety.md`
```md
---
title: 'Anxiety'
slug: "anxiety"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Anxiety

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\atemporality.fa.md`
```md
---
title: 'Atemporality'
slug: "atemporality"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Atemporality

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\atemporality.md`
```md
---
title: 'Atemporality'
slug: "atemporality"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Atemporality

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\catharsis.fa.md`
```md
---
title: 'Catharsis'
slug: "catharsis"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Catharsis

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\catharsis.md`
```md
---
title: 'Catharsis'
slug: "catharsis"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Catharsis

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\cognitive-dysphoria.fa.md`
```md
---
title: 'Cognitive dysphoria'
slug: "cognitive-dysphoria"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cognitive dysphoria

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\cognitive-dysphoria.md`
```md
---
title: 'Cognitive dysphoria'
slug: "cognitive-dysphoria"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cognitive dysphoria

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\cognitive-effects.fa.md`
```md
---
title: 'Cognitive_effects'
slug: "cognitive-effects"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cognitive_effects

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\cognitive-effects.md`
```md
---
title: 'Cognitive_effects'
slug: "cognitive-effects"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cognitive_effects

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\cognitive-euphoria.fa.md`
```md
---
title: 'Cognitive euphoria'
slug: "cognitive-euphoria"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cognitive euphoria

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\cognitive-euphoria.md`
```md
---
title: 'Cognitive euphoria'
slug: "cognitive-euphoria"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cognitive euphoria

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\cognitive-fatigue.fa.md`
```md
---
title: 'Cognitive fatigue'
slug: "cognitive-fatigue"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cognitive fatigue

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\cognitive-fatigue.md`
```md
---
title: 'Cognitive fatigue'
slug: "cognitive-fatigue"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cognitive fatigue

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\Cognitive_effects.fa.md`
```md
---
title: 'Cognitive_effects'
slug: "Cognitive_effects"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cognitive_effects

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\Cognitive_effects.md`
```md
---
title: 'Cognitive_effects'
slug: "Cognitive_effects"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cognitive_effects

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\compulsive-redosing.fa.md`
```md
---
title: 'Compulsive redosing'
slug: "compulsive-redosing"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Compulsive redosing

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\compulsive-redosing.md`
```md
---
title: 'Compulsive redosing'
slug: "compulsive-redosing"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Compulsive redosing

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\conceptual-thinking.fa.md`
```md
---
title: 'Conceptual thinking'
slug: "conceptual-thinking"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Conceptual thinking

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\conceptual-thinking.md`
```md
---
title: 'Conceptual thinking'
slug: "conceptual-thinking"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Conceptual thinking

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\confusion.fa.md`
```md
---
title: 'Confusion'
slug: "confusion"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Confusion

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\confusion.md`
```md
---
title: 'Confusion'
slug: "confusion"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Confusion

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\creativity-depression.fa.md`
```md
---
title: 'Creativity depression'
slug: "creativity-depression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Creativity depression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\creativity-depression.md`
```md
---
title: 'Creativity depression'
slug: "creativity-depression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Creativity depression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\creativity-enhancement.fa.md`
```md
---
title: 'Creativity enhancement'
slug: "creativity-enhancement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Creativity enhancement

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\creativity-enhancement.md`
```md
---
title: 'Creativity enhancement'
slug: "creativity-enhancement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Creativity enhancement

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\delirium.fa.md`
```md
---
title: 'Delirium'
slug: "delirium"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Delirium

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\delirium.md`
```md
---
title: 'Delirium'
slug: "delirium"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Delirium

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\delusions.fa.md`
```md
---
title: 'Delusions'
slug: "delusions"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Delusions

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\delusions.md`
```md
---
title: 'Delusions'
slug: "delusions"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Delusions

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\depersonalization.fa.md`
```md
---
title: 'Depersonalization'
slug: "depersonalization"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Depersonalization

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\depersonalization.md`
```md
---
title: 'Depersonalization'
slug: "depersonalization"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Depersonalization

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\depression-reduction.fa.md`
```md
---
title: 'Depression reduction'
slug: "depression-reduction"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Depression reduction

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\depression-reduction.md`
```md
---
title: 'Depression reduction'
slug: "depression-reduction"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Depression reduction

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\depression.fa.md`
```md
---
title: 'Depression'
slug: "depression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Depression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\depression.md`
```md
---
title: 'Depression'
slug: "depression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Depression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\depressions.fa.md`
```md
---
title: 'Depressions'
slug: "depressions"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Depressions

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\depressions.md`
```md
---
title: 'Depressions'
slug: "depressions"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Depressions

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\derealization.fa.md`
```md
---
title: 'Derealization'
slug: "derealization"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Derealization

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\derealization.md`
```md
---
title: 'Derealization'
slug: "derealization"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Derealization

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\disinhibition.fa.md`
```md
---
title: 'Disinhibition'
slug: "disinhibition"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Disinhibition

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\disinhibition.md`
```md
---
title: 'Disinhibition'
slug: "disinhibition"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Disinhibition

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\dream-potentiation.fa.md`
```md
---
title: 'Dream potentiation'
slug: "dream-potentiation"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Dream potentiation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\dream-potentiation.md`
```md
---
title: 'Dream potentiation'
slug: "dream-potentiation"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Dream potentiation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\dream-suppression.fa.md`
```md
---
title: 'Dream suppression'
slug: "dream-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Dream suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\dream-suppression.md`
```md
---
title: 'Dream suppression'
slug: "dream-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Dream suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\ego-dissolution.fa.md`
```md
---
title: 'Ego dissolution'
slug: "ego-dissolution"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Ego dissolution

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\ego-dissolution.md`
```md
---
title: 'Ego dissolution'
slug: "ego-dissolution"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Ego dissolution

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\ego-inflation.fa.md`
```md
---
title: 'Ego inflation'
slug: "ego-inflation"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Ego inflation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\ego-inflation.md`
```md
---
title: 'Ego inflation'
slug: "ego-inflation"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Ego inflation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\ego-replacement.fa.md`
```md
---
title: 'Ego replacement'
slug: "ego-replacement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Ego replacement

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\ego-replacement.md`
```md
---
title: 'Ego replacement'
slug: "ego-replacement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Ego replacement

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\emotion-intensification.fa.md`
```md
---
title: 'Emotion intensification'
slug: "emotion-intensification"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Emotion intensification

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\emotion-intensification.md`
```md
---
title: 'Emotion intensification'
slug: "emotion-intensification"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Emotion intensification

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\emotion-suppression.fa.md`
```md
---
title: 'Emotion suppression'
slug: "emotion-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Emotion suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\emotion-suppression.md`
```md
---
title: 'Emotion suppression'
slug: "emotion-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Emotion suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\empathy-affection-and-sociability-enhancement.fa.md`
```md
---
title: 'Empathy, affection, and sociability enhancement'
slug: "empathy-affection-and-sociability-enhancement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Empathy, affection, and sociability enhancement

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\empathy-affection-and-sociability-enhancement.md`
```md
---
title: 'Empathy, affection, and sociability enhancement'
slug: "empathy-affection-and-sociability-enhancement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Empathy, affection, and sociability enhancement

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\enhancements.fa.md`
```md
---
title: 'Enhancements'
slug: "enhancements"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Enhancements

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\enhancements.md`
```md
---
title: 'Enhancements'
slug: "enhancements"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Enhancements

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\euthymia.fa.md`
```md
---
title: 'Euthymia'
slug: "euthymia"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Euthymia

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\euthymia.md`
```md
---
title: 'Euthymia'
slug: "euthymia"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Euthymia

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\existential-self-realization.fa.md`
```md
---
title: 'Existential self-realization'
slug: "existential-self-realization"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Existential self-realization

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\existential-self-realization.md`
```md
---
title: 'Existential self-realization'
slug: "existential-self-realization"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Existential self-realization

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\feelings-of-impending-doom.fa.md`
```md
---
title: 'Feelings of impending doom'
slug: "feelings-of-impending-doom"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Feelings of impending doom

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\feelings-of-impending-doom.md`
```md
---
title: 'Feelings of impending doom'
slug: "feelings-of-impending-doom"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Feelings of impending doom

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\focus-intensification.fa.md`
```md
---
title: 'Focus intensification'
slug: "focus-intensification"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Focus intensification

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\focus-intensification.md`
```md
---
title: 'Focus intensification'
slug: "focus-intensification"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Focus intensification

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\focus-suppression.fa.md`
```md
---
title: 'Focus suppression'
slug: "focus-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Focus suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\focus-suppression.md`
```md
---
title: 'Focus suppression'
slug: "focus-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Focus suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\glossolalia.fa.md`
```md
---
title: 'Glossolalia'
slug: "glossolalia"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Glossolalia

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\glossolalia.md`
```md
---
title: 'Glossolalia'
slug: "glossolalia"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Glossolalia

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\identity-alteration.fa.md`
```md
---
title: 'Identity alteration'
slug: "identity-alteration"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Identity alteration

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\identity-alteration.md`
```md
---
title: 'Identity alteration'
slug: "identity-alteration"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Identity alteration

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\immersion-intensification.fa.md`
```md
---
title: 'Immersion intensification'
slug: "immersion-intensification"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Immersion intensification

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\immersion-intensification.md`
```md
---
title: 'Immersion intensification'
slug: "immersion-intensification"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Immersion intensification

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\increased-introspection.fa.md`
```md
---
title: 'Increased introspection'
slug: "increased-introspection"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased introspection

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\increased-introspection.md`
```md
---
title: 'Increased introspection'
slug: "increased-introspection"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased introspection

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\increased-music-appreciation.fa.md`
```md
---
title: 'Increased music appreciation'
slug: "increased-music-appreciation"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased music appreciation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\increased-music-appreciation.md`
```md
---
title: 'Increased music appreciation'
slug: "increased-music-appreciation"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased music appreciation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\increased-sense-of-humor.fa.md`
```md
---
title: 'Increased sense of humor'
slug: "increased-sense-of-humor"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased sense of humor

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\increased-sense-of-humor.md`
```md
---
title: 'Increased sense of humor'
slug: "increased-sense-of-humor"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased sense of humor

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\intensifications.fa.md`
```md
---
title: 'Intensifications'
slug: "intensifications"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Intensifications

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\intensifications.md`
```md
---
title: 'Intensifications'
slug: "intensifications"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Intensifications

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\irritability.fa.md`
```md
---
title: 'Irritability'
slug: "irritability"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Irritability

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\irritability.md`
```md
---
title: 'Irritability'
slug: "irritability"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Irritability

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\language-depression.fa.md`
```md
---
title: 'Language depression'
slug: "language-depression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Language depression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\language-depression.md`
```md
---
title: 'Language depression'
slug: "language-depression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Language depression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\mania.fa.md`
```md
---
title: 'Mania'
slug: "mania"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Mania

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\mania.md`
```md
---
title: 'Mania'
slug: "mania"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Mania

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\memory-enhancement.fa.md`
```md
---
title: 'Memory enhancement'
slug: "memory-enhancement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Memory enhancement

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\memory-enhancement.md`
```md
---
title: 'Memory enhancement'
slug: "memory-enhancement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Memory enhancement

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\memory-suppression.fa.md`
```md
---
title: 'Memory suppression'
slug: "memory-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Memory suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\memory-suppression.md`
```md
---
title: 'Memory suppression'
slug: "memory-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Memory suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\mindfulness.fa.md`
```md
---
title: 'Mindfulness'
slug: "mindfulness"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Mindfulness

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\mindfulness.md`
```md
---
title: 'Mindfulness'
slug: "mindfulness"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Mindfulness

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\motivation-depression.fa.md`
```md
---
title: 'Motivation depression'
slug: "motivation-depression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Motivation depression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\motivation-depression.md`
```md
---
title: 'Motivation depression'
slug: "motivation-depression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Motivation depression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\motivation-enhancement.fa.md`
```md
---
title: 'Motivation enhancement'
slug: "motivation-enhancement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Motivation enhancement

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\motivation-enhancement.md`
```md
---
title: 'Motivation enhancement'
slug: "motivation-enhancement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Motivation enhancement

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\multiple-thought-streams.fa.md`
```md
---
title: 'Multiple thought streams'
slug: "multiple-thought-streams"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Multiple thought streams

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\multiple-thought-streams.md`
```md
---
title: 'Multiple thought streams'
slug: "multiple-thought-streams"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Multiple thought streams

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\no-umbrella-reviews-done-below-this-line.fa.md`
```md
---
title: 'No umbrella reviews done below this line'
slug: "no-umbrella-reviews-done-below-this-line"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# No umbrella reviews done below this line

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\no-umbrella-reviews-done-below-this-line.md`
```md
---
title: 'No umbrella reviews done below this line'
slug: "no-umbrella-reviews-done-below-this-line"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# No umbrella reviews done below this line

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\novel.fa.md`
```md
---
title: 'Novel'
slug: "novel"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Novel

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\novel.md`
```md
---
title: 'Novel'
slug: "novel"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Novel

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\novelty-enhancement.fa.md`
```md
---
title: 'Novelty enhancement'
slug: "novelty-enhancement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Novelty enhancement

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\novelty-enhancement.md`
```md
---
title: 'Novelty enhancement'
slug: "novelty-enhancement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Novelty enhancement

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\panic-attack.fa.md`
```md
---
title: 'Panic attack'
slug: "panic-attack"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Panic attack

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\panic-attack.md`
```md
---
title: 'Panic attack'
slug: "panic-attack"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Panic attack

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\paranoia.fa.md`
```md
---
title: 'Paranoia'
slug: "paranoia"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Paranoia

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\paranoia.md`
```md
---
title: 'Paranoia'
slug: "paranoia"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Paranoia

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\perceived-exposure-to-inner-mechanics-of-consciousness.fa.md`
```md
---
title: 'Perceived exposure to inner mechanics of consciousness'
slug: "perceived-exposure-to-inner-mechanics-of-consciousness"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perceived exposure to inner mechanics of consciousness

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\perceived-exposure-to-inner-mechanics-of-consciousness.md`
```md
---
title: 'Perceived exposure to inner mechanics of consciousness'
slug: "perceived-exposure-to-inner-mechanics-of-consciousness"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perceived exposure to inner mechanics of consciousness

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\perception-of-eternalism.fa.md`
```md
---
title: 'Perception of eternalism'
slug: "perception-of-eternalism"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perception of eternalism

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\perception-of-eternalism.md`
```md
---
title: 'Perception of eternalism'
slug: "perception-of-eternalism"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perception of eternalism

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\perception-of-interdependent-opposites.fa.md`
```md
---
title: 'Perception of interdependent opposites'
slug: "perception-of-interdependent-opposites"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perception of interdependent opposites

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\perception-of-interdependent-opposites.md`
```md
---
title: 'Perception of interdependent opposites'
slug: "perception-of-interdependent-opposites"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perception of interdependent opposites

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\perception-of-predeterminism.fa.md`
```md
---
title: 'Perception of predeterminism'
slug: "perception-of-predeterminism"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perception of predeterminism

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\perception-of-predeterminism.md`
```md
---
title: 'Perception of predeterminism'
slug: "perception-of-predeterminism"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perception of predeterminism

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\perception-of-self-design.fa.md`
```md
---
title: 'Perception of self-design'
slug: "perception-of-self-design"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perception of self-design

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\perception-of-self-design.md`
```md
---
title: 'Perception of self-design'
slug: "perception-of-self-design"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perception of self-design

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\personal-bias-suppression.fa.md`
```md
---
title: 'Personal bias suppression'
slug: "personal-bias-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Personal bias suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\personal-bias-suppression.md`
```md
---
title: 'Personal bias suppression'
slug: "personal-bias-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Personal bias suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\personal-meaning-intensification.fa.md`
```md
---
title: 'Personal meaning intensification'
slug: "personal-meaning-intensification"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Personal meaning intensification

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\personal-meaning-intensification.md`
```md
---
title: 'Personal meaning intensification'
slug: "personal-meaning-intensification"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Personal meaning intensification

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\personality-regression.fa.md`
```md
---
title: 'Personality regression'
slug: "personality-regression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Personality regression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\personality-regression.md`
```md
---
title: 'Personality regression'
slug: "personality-regression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Personality regression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\psychological.fa.md`
```md
---
title: 'Psychological'
slug: "psychological"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Psychological

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\psychological.md`
```md
---
title: 'Psychological'
slug: "psychological"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Psychological

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\psychosis.fa.md`
```md
---
title: 'Psychosis'
slug: "psychosis"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Psychosis

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\psychosis.md`
```md
---
title: 'Psychosis'
slug: "psychosis"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Psychosis

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\rejuvenation.fa.md`
```md
---
title: 'Rejuvenation'
slug: "rejuvenation"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Rejuvenation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\rejuvenation.md`
```md
---
title: 'Rejuvenation'
slug: "rejuvenation"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Rejuvenation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\simultaneous-emotions.fa.md`
```md
---
title: 'Simultaneous emotions'
slug: "simultaneous-emotions"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Simultaneous emotions

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\simultaneous-emotions.md`
```md
---
title: 'Simultaneous emotions'
slug: "simultaneous-emotions"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Simultaneous emotions

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\sleepiness.fa.md`
```md
---
title: 'Sleepiness'
slug: "sleepiness"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Sleepiness

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\sleepiness.md`
```md
---
title: 'Sleepiness'
slug: "sleepiness"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Sleepiness

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\sociability-depression.fa.md`
```md
---
title: 'Sociability depression'
slug: "sociability-depression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Sociability depression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\sociability-depression.md`
```md
---
title: 'Sociability depression'
slug: "sociability-depression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Sociability depression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\spirituality-intensification.fa.md`
```md
---
title: 'Spirituality intensification'
slug: "spirituality-intensification"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Spirituality intensification

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\spirituality-intensification.md`
```md
---
title: 'Spirituality intensification'
slug: "spirituality-intensification"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Spirituality intensification

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\suggestibility-intensification.fa.md`
```md
---
title: 'Suggestibility intensification'
slug: "suggestibility-intensification"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Suggestibility intensification

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\suggestibility-intensification.md`
```md
---
title: 'Suggestibility intensification'
slug: "suggestibility-intensification"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Suggestibility intensification

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\suggestibility-suppression.fa.md`
```md
---
title: 'Suggestibility suppression'
slug: "suggestibility-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Suggestibility suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\suggestibility-suppression.md`
```md
---
title: 'Suggestibility suppression'
slug: "suggestibility-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Suggestibility suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\suicidal-ideation.fa.md`
```md
---
title: 'Suicidal ideation'
slug: "suicidal-ideation"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Suicidal ideation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\suicidal-ideation.md`
```md
---
title: 'Suicidal ideation'
slug: "suicidal-ideation"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Suicidal ideation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\thought-acceleration.fa.md`
```md
---
title: 'Thought acceleration'
slug: "thought-acceleration"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Thought acceleration

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\thought-acceleration.md`
```md
---
title: 'Thought acceleration'
slug: "thought-acceleration"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Thought acceleration

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\thought-connectivity.fa.md`
```md
---
title: 'Thought connectivity'
slug: "thought-connectivity"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Thought connectivity

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\thought-connectivity.md`
```md
---
title: 'Thought connectivity'
slug: "thought-connectivity"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Thought connectivity

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\thought-deceleration.fa.md`
```md
---
title: 'Thought deceleration'
slug: "thought-deceleration"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Thought deceleration

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\thought-deceleration.md`
```md
---
title: 'Thought deceleration'
slug: "thought-deceleration"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Thought deceleration

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\thought-disorganization.fa.md`
```md
---
title: 'Thought disorganization'
slug: "thought-disorganization"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Thought disorganization

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\thought-disorganization.md`
```md
---
title: 'Thought disorganization'
slug: "thought-disorganization"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Thought disorganization

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\thought-loop.fa.md`
```md
---
title: 'Thought loop'
slug: "thought-loop"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Thought loop

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\thought-loop.md`
```md
---
title: 'Thought loop'
slug: "thought-loop"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Thought loop

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\thought-organization.fa.md`
```md
---
title: 'Thought organization'
slug: "thought-organization"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Thought organization

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\thought-organization.md`
```md
---
title: 'Thought organization'
slug: "thought-organization"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Thought organization

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\time-compression.fa.md`
```md
---
title: 'Time compression'
slug: "time-compression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Time compression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\time-compression.md`
```md
---
title: 'Time compression'
slug: "time-compression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Time compression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\time-dilation.fa.md`
```md
---
title: 'Time dilation'
slug: "time-dilation"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Time dilation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\time-dilation.md`
```md
---
title: 'Time dilation'
slug: "time-dilation"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Time dilation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\time-distortion.fa.md`
```md
---
title: 'Time distortion'
slug: "time-distortion"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Time distortion

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\time-distortion.md`
```md
---
title: 'Time distortion'
slug: "time-distortion"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Time distortion

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\time-reversal.fa.md`
```md
---
title: 'Time reversal'
slug: "time-reversal"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Time reversal

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\time-reversal.md`
```md
---
title: 'Time reversal'
slug: "time-reversal"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Time reversal

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\transpersonal.fa.md`
```md
---
title: 'Transpersonal'
slug: "transpersonal"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Transpersonal

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\transpersonal.md`
```md
---
title: 'Transpersonal'
slug: "transpersonal"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Transpersonal

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\unity-and-interconnectedness.fa.md`
```md
---
title: "Unity and interconnectedness"
slug: "unity-and-interconnectedness"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Unity and interconnectedness

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\unity-and-interconnectedness.md`
```md
---
title: "Unity and interconnectedness"
slug: "unity-and-interconnectedness"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Unity and interconnectedness

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\wakefulness copy.md`
```md
---
title: 'Wakefulness'
slug: "wakefulness"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Wakefulness

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\wakefulness.fa copy.md`
```md
---
title: 'Wakefulness'
slug: "wakefulness"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Wakefulness

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\wakefulness.fa.md`
```md
---
title: "Wakefulness"
slug: "wakefulness"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Wakefulness

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\wakefulness.md`
```md
---
title: "Wakefulness"
slug: "wakefulness"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Wakefulness

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\alterations.fa.md`
```md
---
title: 'Alterations'
slug: "alterations"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Alterations

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\alterations.md`
```md
---
title: 'Alterations'
slug: "alterations"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Alterations

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\amplifications.fa.md`
```md
---
title: 'Amplifications'
slug: "amplifications"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Amplifications

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\amplifications.md`
```md
---
title: 'Amplifications'
slug: "amplifications"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Amplifications

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\appetite-intensification.fa.md`
```md
---
title: 'Appetite intensification'
slug: "appetite-intensification"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Appetite intensification

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\appetite-intensification.md`
```md
---
title: 'Appetite intensification'
slug: "appetite-intensification"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Appetite intensification

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\appetite-suppression.fa.md`
```md
---
title: 'Appetite suppression'
slug: "appetite-suppression"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Appetite suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\appetite-suppression.md`
```md
---
title: 'Appetite suppression'
slug: "appetite-suppression"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Appetite suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\bodily-control-enhancement.fa.md`
```md
---
title: 'Bodily control enhancement'
slug: "bodily-control-enhancement"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Bodily control enhancement

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\bodily-control-enhancement.md`
```md
---
title: 'Bodily control enhancement'
slug: "bodily-control-enhancement"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Bodily control enhancement

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\body-odor-alteration.fa.md`
```md
---
title: 'Body odor alteration'
slug: "body-odor-alteration"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Body odor alteration

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\body-odor-alteration.md`
```md
---
title: 'Body odor alteration'
slug: "body-odor-alteration"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Body odor alteration

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\bronchodilation.fa.md`
```md
---
title: 'Bronchodilation'
slug: "bronchodilation"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Bronchodilation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\bronchodilation.md`
```md
---
title: 'Bronchodilation'
slug: "bronchodilation"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Bronchodilation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\changes-in-felt-bodily-form.fa.md`
```md
---
title: 'Changes in felt bodily form'
slug: "changes-in-felt-bodily-form"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Changes in felt bodily form

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\changes-in-felt-bodily-form.md`
```md
---
title: 'Changes in felt bodily form'
slug: "changes-in-felt-bodily-form"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Changes in felt bodily form

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\changes-in-felt-gravity.fa.md`
```md
---
title: 'Changes in felt gravity'
slug: "changes-in-felt-gravity"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Changes in felt gravity

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\changes-in-felt-gravity.md`
```md
---
title: 'Changes in felt gravity'
slug: "changes-in-felt-gravity"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Changes in felt gravity

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\cough-suppression.fa.md`
```md
---
title: 'Cough suppression'
slug: "cough-suppression"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cough suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\cough-suppression.md`
```md
---
title: 'Cough suppression'
slug: "cough-suppression"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cough suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\decreased-libido.fa.md`
```md
---
title: 'Decreased libido'
slug: "decreased-libido"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Decreased libido

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\decreased-libido.md`
```md
---
title: 'Decreased libido'
slug: "decreased-libido"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Decreased libido

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\excessive-yawning.fa.md`
```md
---
title: 'Excessive yawning'
slug: "excessive-yawning"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Excessive yawning

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\excessive-yawning.md`
```md
---
title: 'Excessive yawning'
slug: "excessive-yawning"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Excessive yawning

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\increased-libido.fa.md`
```md
---
title: 'Increased libido'
slug: "increased-libido"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased libido

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\increased-libido.md`
```md
---
title: 'Increased libido'
slug: "increased-libido"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased libido

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\increased-respiration.fa.md`
```md
---
title: 'Increased respiration'
slug: "increased-respiration"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased respiration

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\increased-respiration.md`
```md
---
title: 'Increased respiration'
slug: "increased-respiration"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased respiration

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\increased-salivation.fa.md`
```md
---
title: 'Increased salivation'
slug: "increased-salivation"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased salivation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\increased-salivation.md`
```md
---
title: 'Increased salivation'
slug: "increased-salivation"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased salivation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\laughter-fits.fa.md`
```md
---
title: 'Laughter fits'
slug: "laughter-fits"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Laughter fits

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\laughter-fits.md`
```md
---
title: 'Laughter fits'
slug: "laughter-fits"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Laughter fits

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\motor-control-loss.fa.md`
```md
---
title: 'Motor control loss'
slug: "motor-control-loss"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Motor control loss

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\motor-control-loss.md`
```md
---
title: 'Motor control loss'
slug: "motor-control-loss"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Motor control loss

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\mouth-numbing.fa.md`
```md
---
title: 'Mouth numbing'
slug: "mouth-numbing"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Mouth numbing

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\mouth-numbing.md`
```md
---
title: 'Mouth numbing'
slug: "mouth-numbing"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Mouth numbing

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\muscle-relaxation.fa.md`
```md
---
title: 'Muscle relaxation'
slug: "muscle-relaxation"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Muscle relaxation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\muscle-relaxation.md`
```md
---
title: 'Muscle relaxation'
slug: "muscle-relaxation"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Muscle relaxation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\nausea-suppression.fa.md`
```md
---
title: 'Nausea suppression'
slug: "nausea-suppression"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Nausea suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\nausea-suppression.md`
```md
---
title: 'Nausea suppression'
slug: "nausea-suppression"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Nausea suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\orgasm-depression.fa.md`
```md
---
title: 'Orgasm depression'
slug: "orgasm-depression"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Orgasm depression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\orgasm-depression.md`
```md
---
title: 'Orgasm depression'
slug: "orgasm-depression"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Orgasm depression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\pain-relief.fa.md`
```md
---
title: 'Pain relief'
slug: "pain-relief"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Pain relief

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\pain-relief.md`
```md
---
title: 'Pain relief'
slug: "pain-relief"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Pain relief

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\perception-of-bodily-heaviness.fa.md`
```md
---
title: 'Perception of bodily heaviness'
slug: "perception-of-bodily-heaviness"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perception of bodily heaviness

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\perception-of-bodily-heaviness.md`
```md
---
title: 'Perception of bodily heaviness'
slug: "perception-of-bodily-heaviness"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perception of bodily heaviness

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\perception-of-bodily-lightness.fa.md`
```md
---
title: 'Perception of bodily lightness'
slug: "perception-of-bodily-lightness"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perception of bodily lightness

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\perception-of-bodily-lightness.md`
```md
---
title: 'Perception of bodily lightness'
slug: "perception-of-bodily-lightness"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perception of bodily lightness

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\physical-autonomy.fa.md`
```md
---
title: 'Physical autonomy'
slug: "physical-autonomy"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Physical autonomy

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\physical-autonomy.md`
```md
---
title: 'Physical autonomy'
slug: "physical-autonomy"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Physical autonomy

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\physical-effects.fa.md`
```md
---
title: 'Physical_effects'
slug: "physical-effects"
lang: "fa"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Physical_effects

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\physical-effects.md`
```md
---
title: 'Physical_effects'
slug: "physical-effects"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Physical_effects

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\physical-euphoria.fa.md`
```md
---
title: 'Physical euphoria'
slug: "physical-euphoria"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Physical euphoria

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\physical-euphoria.md`
```md
---
title: 'Physical euphoria'
slug: "physical-euphoria"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Physical euphoria

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\pupil-constriction.fa.md`
```md
---
title: 'Pupil constriction'
slug: "pupil-constriction"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Pupil constriction

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\pupil-constriction.md`
```md
---
title: 'Pupil constriction'
slug: "pupil-constriction"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Pupil constriction

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\pupil-dilation.fa.md`
```md
---
title: 'Pupil dilation'
slug: "pupil-dilation"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Pupil dilation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\pupil-dilation.md`
```md
---
title: 'Pupil dilation'
slug: "pupil-dilation"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Pupil dilation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\sedation.fa.md`
```md
---
title: 'Sedation'
slug: "sedation"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Sedation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\sedation.md`
```md
---
title: 'Sedation'
slug: "sedation"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Sedation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\seizure-suppression.fa.md`
```md
---
title: 'Seizure suppression'
slug: "seizure-suppression"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Seizure suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\seizure-suppression.md`
```md
---
title: 'Seizure suppression'
slug: "seizure-suppression"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Seizure suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\stamina-intensification.fa.md`
```md
---
title: 'Stamina intensification'
slug: "stamina-intensification"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Stamina intensification

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\stamina-intensification.md`
```md
---
title: 'Stamina intensification'
slug: "stamina-intensification"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Stamina intensification

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\stimulation.fa.md`
```md
---
title: 'Stimulation'
slug: "stimulation"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Stimulation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\stimulation.md`
```md
---
title: 'Stimulation'
slug: "stimulation"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Stimulation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\suppressions.fa.md`
```md
---
title: 'Suppressions'
slug: "suppressions"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Suppressions

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\suppressions.md`
```md
---
title: 'Suppressions'
slug: "suppressions"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Suppressions

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Sensory_effects.fa.md`
```md
---
title: "Sensory_effects"
slug: "sensory_effects"
lang: "en"
category: "Sensory_effects"
weight: 1000
template: "wiki"
summary: ''
---

# Sensory_effects

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Sensory_effects.md`
```md
---
title: "Sensory_effects"
slug: "sensory_effects"
lang: "en"
category: "Sensory_effects"
weight: 1000
template: "wiki"
summary: ''
---

# Sensory_effects

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Auditory_effects\auditory-acuity-enhancement.fa.md`
```md
---
title: 'Auditory acuity enhancement'
slug: "auditory-acuity-enhancement"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Auditory acuity enhancement

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Auditory_effects\auditory-acuity-enhancement.md`
```md
---
title: 'Auditory acuity enhancement'
slug: "auditory-acuity-enhancement"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Auditory acuity enhancement

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Auditory_effects\auditory-acuity-suppression.fa.md`
```md
---
title: 'Auditory acuity suppression'
slug: "auditory-acuity-suppression"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Auditory acuity suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Auditory_effects\auditory-acuity-suppression.md`
```md
---
title: 'Auditory acuity suppression'
slug: "auditory-acuity-suppression"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Auditory acuity suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Auditory_effects\auditory-distortion.fa.md`
```md
---
title: 'Auditory distortion'
slug: "auditory-distortion"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Auditory distortion

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Auditory_effects\auditory-distortion.md`
```md
---
title: 'Auditory distortion'
slug: "auditory-distortion"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Auditory distortion

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Auditory_effects\auditory-effects.fa.md`
```md
---
title: 'Auditory_effects'
slug: "auditory-effects"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Auditory_effects

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Auditory_effects\auditory-effects.md`
```md
---
title: 'Auditory_effects'
slug: "auditory-effects"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Auditory_effects

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Auditory_effects\auditory-hallucination.fa.md`
```md
---
title: 'Auditory hallucination'
slug: "auditory-hallucination"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Auditory hallucination

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Auditory_effects\auditory-hallucination.md`
```md
---
title: 'Auditory hallucination'
slug: "auditory-hallucination"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Auditory hallucination

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Auditory_effects\auditory-misinterpretation.fa.md`
```md
---
title: 'Auditory misinterpretation'
slug: "auditory-misinterpretation"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Auditory misinterpretation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Auditory_effects\auditory-misinterpretation.md`
```md
---
title: 'Auditory misinterpretation'
slug: "auditory-misinterpretation"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Auditory misinterpretation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Auditory_effects\autonomous-voice-communication.fa.md`
```md
---
title: 'Autonomous voice communication'
slug: "autonomous-voice-communication"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Autonomous voice communication

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Auditory_effects\autonomous-voice-communication.md`
```md
---
title: 'Autonomous voice communication'
slug: "autonomous-voice-communication"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Autonomous voice communication

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Auditory_effects\external-auditory-hallucination.fa.md`
```md
---
title: 'External auditory hallucination'
slug: "external-auditory-hallucination"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# External auditory hallucination

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Auditory_effects\external-auditory-hallucination.md`
```md
---
title: 'External auditory hallucination'
slug: "external-auditory-hallucination"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# External auditory hallucination

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Auditory_effects\internal-auditory-hallucination.fa.md`
```md
---
title: 'Internal auditory hallucination'
slug: "internal-auditory-hallucination"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Internal auditory hallucination

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Auditory_effects\internal-auditory-hallucination.md`
```md
---
title: 'Internal auditory hallucination'
slug: "internal-auditory-hallucination"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Internal auditory hallucination

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Auditory_effects\temporal-scaling.fa.md`
```md
---
title: 'Temporal scaling'
slug: "temporal-scaling"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Temporal scaling

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Auditory_effects\temporal-scaling.md`
```md
---
title: 'Temporal scaling'
slug: "temporal-scaling"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Temporal scaling

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Multisensory_effects\anticipatory-response.fa.md`
```md
---
title: 'Anticipatory response'
slug: "anticipatory-response"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Anticipatory response

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Multisensory_effects\anticipatory-response.md`
```md
---
title: 'Anticipatory response'
slug: "anticipatory-response"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Anticipatory response

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Multisensory_effects\component-controllability.fa.md`
```md
---
title: 'Component controllability'
slug: "component-controllability"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Component controllability

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Multisensory_effects\component-controllability.md`
```md
---
title: 'Component controllability'
slug: "component-controllability"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Component controllability

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Multisensory_effects\dosage-independent-intensity.fa.md`
```md
---
title: 'Dosage independent intensity'
slug: "dosage-independent-intensity"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Dosage independent intensity

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Multisensory_effects\dosage-independent-intensity.md`
```md
---
title: 'Dosage independent intensity'
slug: "dosage-independent-intensity"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Dosage independent intensity

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Multisensory_effects\machinescapes.fa.md`
```md
---
title: 'Machinescapes'
slug: "machinescapes"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Machinescapes

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Multisensory_effects\machinescapes.md`
```md
---
title: 'Machinescapes'
slug: "machinescapes"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Machinescapes

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Multisensory_effects\memory-replays.fa.md`
```md
---
title: 'Memory replays'
slug: "memory-replays"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Memory replays

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Multisensory_effects\memory-replays.md`
```md
---
title: 'Memory replays'
slug: "memory-replays"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Memory replays

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Multisensory_effects\multisensory-effects.fa.md`
```md
---
title: 'Multisensory_effects'
slug: "multisensory-effects"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Multisensory_effects

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Multisensory_effects\multisensory-effects.md`
```md
---
title: 'Multisensory_effects'
slug: "multisensory-effects"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Multisensory_effects

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Multisensory_effects\scenarios-and-plots.fa.md`
```md
---
title: 'Scenarios and plots'
slug: "scenarios-and-plots"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Scenarios and plots

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Multisensory_effects\scenarios-and-plots.md`
```md
---
title: 'Scenarios and plots'
slug: "scenarios-and-plots"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Scenarios and plots

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Multisensory_effects\spatial-disorientation.fa.md`
```md
---
title: 'Spatial disorientation'
slug: "spatial-disorientation"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Spatial disorientation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Multisensory_effects\spatial-disorientation.md`
```md
---
title: 'Spatial disorientation'
slug: "spatial-disorientation"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Spatial disorientation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Multisensory_effects\spontaneous-physical-movements.fa.md`
```md
---
title: 'Spontaneous physical movements'
slug: "spontaneous-physical-movements"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Spontaneous physical movements

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Multisensory_effects\spontaneous-physical-movements.md`
```md
---
title: 'Spontaneous physical movements'
slug: "spontaneous-physical-movements"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Spontaneous physical movements

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Multisensory_effects\synaesthesia.fa.md`
```md
---
title: 'Synaesthesia'
slug: "synaesthesia"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Synaesthesia

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Multisensory_effects\synaesthesia.md`
```md
---
title: 'Synaesthesia'
slug: "synaesthesia"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Synaesthesia

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Tactile_effects\spontaneous-bodily-sensations.fa.md`
```md
---
title: 'Spontaneous bodily sensations'
slug: "spontaneous-bodily-sensations"
lang: "en"
category: 'Tactile_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Spontaneous bodily sensations

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Tactile_effects\spontaneous-bodily-sensations.md`
```md
---
title: 'Spontaneous bodily sensations'
slug: "spontaneous-bodily-sensations"
lang: "en"
category: 'Tactile_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Spontaneous bodily sensations

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Tactile_effects\tactile-effects.fa.md`
```md
---
title: 'Tactile_effects'
slug: "tactile-effects"
lang: "en"
category: 'Tactile_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Tactile_effects

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Tactile_effects\tactile-effects.md`
```md
---
title: 'Tactile_effects'
slug: "tactile-effects"
lang: "en"
category: 'Tactile_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Tactile_effects

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Tactile_effects\tactile-hallucination.fa.md`
```md
---
title: 'Tactile hallucination'
slug: "tactile-hallucination"
lang: "en"
category: 'Tactile_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Tactile hallucination

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Tactile_effects\tactile-hallucination.md`
```md
---
title: 'Tactile hallucination'
slug: "tactile-hallucination"
lang: "en"
category: 'Tactile_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Tactile hallucination

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Tactile_effects\tactile-intensification.fa.md`
```md
---
title: 'Tactile intensification'
slug: "tactile-intensification"
lang: "en"
category: 'Tactile_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Tactile intensification

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Tactile_effects\tactile-intensification.md`
```md
---
title: 'Tactile intensification'
slug: "tactile-intensification"
lang: "en"
category: 'Tactile_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Tactile intensification

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Tactile_effects\tactile-suppression.fa.md`
```md
---
title: 'Tactile suppression'
slug: "tactile-suppression"
lang: "en"
category: 'Tactile_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Tactile suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Tactile_effects\tactile-suppression.md`
```md
---
title: 'Tactile suppression'
slug: "tactile-suppression"
lang: "en"
category: 'Tactile_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Tactile suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\8a-perceived-exposure-to-semantic-concept-network.fa.md`
```md
---
title: '8A - Perceived exposure to semantic concept network'
slug: "8a-perceived-exposure-to-semantic-concept-network"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# 8A - Perceived exposure to semantic concept network

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\8a-perceived-exposure-to-semantic-concept-network.md`
```md
---
title: '8A - Perceived exposure to semantic concept network'
slug: "8a-perceived-exposure-to-semantic-concept-network"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# 8A - Perceived exposure to semantic concept network

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\8b-perceived-exposure-to-inner-mechanics-of-consciousness.fa.md`
```md
---
title: '8B - Perceived exposure to inner mechanics of consciousness'
slug: "8b-perceived-exposure-to-inner-mechanics-of-consciousness"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# 8B - Perceived exposure to inner mechanics of consciousness

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\8b-perceived-exposure-to-inner-mechanics-of-consciousness.md`
```md
---
title: '8B - Perceived exposure to inner mechanics of consciousness'
slug: "8b-perceived-exposure-to-inner-mechanics-of-consciousness"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# 8B - Perceived exposure to inner mechanics of consciousness

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\after-images.fa.md`
```md
---
title: 'After images'
slug: "after-images"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# After images

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\after-images.md`
```md
---
title: 'After images'
slug: "after-images"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# After images

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\autonomous-entity.fa.md`
```md
---
title: 'Autonomous entity'
slug: "autonomous-entity"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Autonomous entity

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\autonomous-entity.md`
```md
---
title: 'Autonomous entity'
slug: "autonomous-entity"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Autonomous entity

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\breathing.fa.md`
```md
---
title: 'Breathing'
slug: "breathing"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Breathing

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\breathing.md`
```md
---
title: 'Breathing'
slug: "breathing"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Breathing

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\brightness-alteration.fa.md`
```md
---
title: 'Brightness alteration'
slug: "brightness-alteration"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Brightness alteration

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\brightness-alteration.md`
```md
---
title: 'Brightness alteration'
slug: "brightness-alteration"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Brightness alteration

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\color-depression.fa.md`
```md
---
title: 'Color depression'
slug: "color-depression"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Color depression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\color-depression.md`
```md
---
title: 'Color depression'
slug: "color-depression"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Color depression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\color-enhancement.fa.md`
```md
---
title: 'Color enhancement'
slug: "color-enhancement"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Color enhancement

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\color-enhancement.md`
```md
---
title: 'Color enhancement'
slug: "color-enhancement"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Color enhancement

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\color-replacement.fa.md`
```md
---
title: 'Color replacement'
slug: "color-replacement"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Color replacement

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\color-replacement.md`
```md
---
title: 'Color replacement'
slug: "color-replacement"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Color replacement

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\color-shifting.fa.md`
```md
---
title: 'Color shifting'
slug: "color-shifting"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Color shifting

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\color-shifting.md`
```md
---
title: 'Color shifting'
slug: "color-shifting"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Color shifting

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\color-tinting.fa.md`
```md
---
title: 'Color tinting'
slug: "color-tinting"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Color tinting

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\color-tinting.md`
```md
---
title: 'Color tinting'
slug: "color-tinting"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Color tinting

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\depth-perception-distortions.fa.md`
```md
---
title: 'Depth perception distortions'
slug: "depth-perception-distortions"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Depth perception distortions

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\depth-perception-distortions.md`
```md
---
title: 'Depth perception distortions'
slug: "depth-perception-distortions"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Depth perception distortions

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\diffraction.fa.md`
```md
---
title: 'Diffraction'
slug: "diffraction"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Diffraction

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\diffraction.md`
```md
---
title: 'Diffraction'
slug: "diffraction"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Diffraction

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\distortions.fa.md`
```md
---
title: 'Distortions'
slug: "distortions"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Distortions

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\distortions.md`
```md
---
title: 'Distortions'
slug: "distortions"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Distortions

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\double-vision.fa.md`
```md
---
title: 'Double vision'
slug: "double-vision"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Double vision

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\double-vision.md`
```md
---
title: 'Double vision'
slug: "double-vision"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Double vision

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\drifting.fa.md`
```md
---
title: 'Drifting'
slug: "drifting"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Drifting

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\drifting.md`
```md
---
title: 'Drifting'
slug: "drifting"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Drifting

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\environmental-cubism.fa.md`
```md
---
title: 'Environmental cubism'
slug: "environmental-cubism"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Environmental cubism

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\environmental-cubism.md`
```md
---
title: 'Environmental cubism'
slug: "environmental-cubism"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Environmental cubism

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\environmental-orbism.fa.md`
```md
---
title: 'Environmental orbism'
slug: "environmental-orbism"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Environmental orbism

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\environmental-orbism.md`
```md
---
title: 'Environmental orbism'
slug: "environmental-orbism"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Environmental orbism

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\environmental-patterning.fa.md`
```md
---
title: 'Environmental patterning'
slug: "environmental-patterning"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Environmental patterning

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\environmental-patterning.md`
```md
---
title: 'Environmental patterning'
slug: "environmental-patterning"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Environmental patterning

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\external-hallucination.fa.md`
```md
---
title: 'External hallucination'
slug: "external-hallucination"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# External hallucination

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\external-hallucination.md`
```md
---
title: 'External hallucination'
slug: "external-hallucination"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# External hallucination

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\flowing.fa.md`
```md
---
title: 'Flowing'
slug: "flowing"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Flowing

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\flowing.md`
```md
---
title: 'Flowing'
slug: "flowing"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Flowing

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\geometry.fa.md`
```md
---
title: 'Geometry'
slug: "geometry"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Geometry

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\geometry.md`
```md
---
title: 'Geometry'
slug: "geometry"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Geometry

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\hallucinatory-states.fa.md`
```md
---
title: 'Hallucinatory states'
slug: "hallucinatory-states"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Hallucinatory states

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\hallucinatory-states.md`
```md
---
title: 'Hallucinatory states'
slug: "hallucinatory-states"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Hallucinatory states

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\internal-hallucination.fa.md`
```md
---
title: 'Internal hallucination'
slug: "internal-hallucination"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Internal hallucination

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\internal-hallucination.md`
```md
---
title: 'Internal hallucination'
slug: "internal-hallucination"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Internal hallucination

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\magnification.fa.md`
```md
---
title: 'Magnification'
slug: "magnification"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Magnification

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\magnification.md`
```md
---
title: 'Magnification'
slug: "magnification"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Magnification

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\melting.fa.md`
```md
---
title: 'Melting'
slug: "melting"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Melting

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\melting.md`
```md
---
title: 'Melting'
slug: "melting"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Melting

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\morphing.fa.md`
```md
---
title: 'Morphing'
slug: "morphing"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Morphing

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\morphing.md`
```md
---
title: 'Morphing'
slug: "morphing"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Morphing

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\object-activation.fa.md`
```md
---
title: 'Object activation'
slug: "object-activation"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Object activation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\object-activation.md`
```md
---
title: 'Object activation'
slug: "object-activation"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Object activation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\object-alteration.fa.md`
```md
---
title: 'Object alteration'
slug: "object-alteration"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Object alteration

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\object-alteration.md`
```md
---
title: 'Object alteration'
slug: "object-alteration"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Object alteration

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\pattern-recognition-enhancement.fa.md`
```md
---
title: 'Pattern recognition enhancement'
slug: "pattern-recognition-enhancement"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Pattern recognition enhancement

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\pattern-recognition-enhancement.md`
```md
---
title: 'Pattern recognition enhancement'
slug: "pattern-recognition-enhancement"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Pattern recognition enhancement

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\pattern-recognition-suppression.fa.md`
```md
---
title: 'Pattern recognition suppression'
slug: "pattern-recognition-suppression"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Pattern recognition suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\pattern-recognition-suppression.md`
```md
---
title: 'Pattern recognition suppression'
slug: "pattern-recognition-suppression"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Pattern recognition suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\peripheral-information-misinterpretation.fa.md`
```md
---
title: 'Peripheral information misinterpretation'
slug: "peripheral-information-misinterpretation"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Peripheral information misinterpretation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\peripheral-information-misinterpretation.md`
```md
---
title: 'Peripheral information misinterpretation'
slug: "peripheral-information-misinterpretation"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Peripheral information misinterpretation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\perspective-distortion.fa.md`
```md
---
title: 'Perspective distortion'
slug: "perspective-distortion"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perspective distortion

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\perspective-distortion.md`
```md
---
title: 'Perspective distortion'
slug: "perspective-distortion"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perspective distortion

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\perspective-hallucination.fa.md`
```md
---
title: 'Perspective hallucination'
slug: "perspective-hallucination"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perspective hallucination

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\perspective-hallucination.md`
```md
---
title: 'Perspective hallucination'
slug: "perspective-hallucination"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perspective hallucination

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\recursion.fa.md`
```md
---
title: 'Recursion'
slug: "recursion"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Recursion

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\recursion.md`
```md
---
title: 'Recursion'
slug: "recursion"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Recursion

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\scenery-slicing.fa.md`
```md
---
title: 'Scenery slicing'
slug: "scenery-slicing"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Scenery slicing

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\scenery-slicing.md`
```md
---
title: 'Scenery slicing'
slug: "scenery-slicing"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Scenery slicing

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\settings-sceneries-and-landscapes.fa.md`
```md
---
title: 'Settings, sceneries, and landscapes'
slug: "settings-sceneries-and-landscapes"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Settings, sceneries, and landscapes

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\settings-sceneries-and-landscapes.md`
```md
---
title: 'Settings, sceneries, and landscapes'
slug: "settings-sceneries-and-landscapes"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Settings, sceneries, and landscapes

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\shadow-people.fa.md`
```md
---
title: 'Shadow people'
slug: "shadow-people"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Shadow people

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\shadow-people.md`
```md
---
title: 'Shadow people'
slug: "shadow-people"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Shadow people

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\symmetrical-texture-repetition.fa.md`
```md
---
title: 'Symmetrical texture repetition'
slug: "symmetrical-texture-repetition"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Symmetrical texture repetition

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\symmetrical-texture-repetition.md`
```md
---
title: 'Symmetrical texture repetition'
slug: "symmetrical-texture-repetition"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Symmetrical texture repetition

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\texture-liquidation.fa.md`
```md
---
title: 'Texture liquidation'
slug: "texture-liquidation"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Texture liquidation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\texture-liquidation.md`
```md
---
title: 'Texture liquidation'
slug: "texture-liquidation"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Texture liquidation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\tracers.fa.md`
```md
---
title: 'Tracers'
slug: "tracers"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Tracers

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\tracers.md`
```md
---
title: 'Tracers'
slug: "tracers"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Tracers

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\transformations.fa.md`
```md
---
title: 'Transformations'
slug: "transformations"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Transformations

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\transformations.md`
```md
---
title: 'Transformations'
slug: "transformations"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Transformations

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\unspeakable-horrors.fa.md`
```md
---
title: 'Unspeakable horrors'
slug: "unspeakable-horrors"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Unspeakable horrors

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\unspeakable-horrors.md`
```md
---
title: 'Unspeakable horrors'
slug: "unspeakable-horrors"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Unspeakable horrors

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\visual-acuity-enhancement.fa.md`
```md
---
title: 'Visual acuity enhancement'
slug: "visual-acuity-enhancement"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual acuity enhancement

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\visual-acuity-enhancement.md`
```md
---
title: 'Visual acuity enhancement'
slug: "visual-acuity-enhancement"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual acuity enhancement

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\visual-acuity-suppression.fa.md`
```md
---
title: 'Visual acuity suppression'
slug: "visual-acuity-suppression"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual acuity suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\visual-acuity-suppression.md`
```md
---
title: 'Visual acuity suppression'
slug: "visual-acuity-suppression"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual acuity suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\visual-effects.fa.md`
```md
---
title: 'Visual_effects'
slug: "visual-effects"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual_effects

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\visual-effects.md`
```md
---
title: 'Visual_effects'
slug: "visual-effects"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual_effects

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\visual-flipping.fa.md`
```md
---
title: 'Visual flipping'
slug: "visual-flipping"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual flipping

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\visual-flipping.md`
```md
---
title: 'Visual flipping'
slug: "visual-flipping"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual flipping

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\visual-haze.fa.md`
```md
---
title: 'Visual haze'
slug: "visual-haze"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual haze

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\visual-haze.md`
```md
---
title: 'Visual haze'
slug: "visual-haze"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual haze

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\visual-processing-acceleration.fa.md`
```md
---
title: 'Visual processing acceleration'
slug: "visual-processing-acceleration"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual processing acceleration

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\visual-processing-acceleration.md`
```md
---
title: 'Visual processing acceleration'
slug: "visual-processing-acceleration"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual processing acceleration

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\visual-processing-deceleration.fa.md`
```md
---
title: 'Visual processing deceleration'
slug: "visual-processing-deceleration"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual processing deceleration

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\visual-processing-deceleration.md`
```md
---
title: 'Visual processing deceleration'
slug: "visual-processing-deceleration"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual processing deceleration

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\visual-stretching.fa.md`
```md
---
title: 'Visual stretching'
slug: "visual-stretching"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual stretching

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Sensory_effects\Visual_effects\visual-stretching.md`
```md
---
title: 'Visual stretching'
slug: "visual-stretching"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual stretching

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Gustatory_and_olfactory_effects\gustatory-and-olfactory-effects.fa.md`
```md
---
title: 'Gustatory_and_olfactory_effects'
slug: "gustatory-and-olfactory-effects"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Gustatory_and_olfactory_effects

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Gustatory_and_olfactory_effects\gustatory-and-olfactory-effects.md`
```md
---
title: 'Gustatory_and_olfactory_effects'
slug: "gustatory-and-olfactory-effects"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Gustatory_and_olfactory_effects

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Gustatory_and_olfactory_effects\gustatory-depression.fa.md`
```md
---
title: 'Gustatory depression'
slug: "gustatory-depression"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Gustatory depression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Gustatory_and_olfactory_effects\gustatory-depression.md`
```md
---
title: 'Gustatory depression'
slug: "gustatory-depression"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Gustatory depression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Gustatory_and_olfactory_effects\gustatory-hallucination.fa.md`
```md
---
title: 'Gustatory hallucination'
slug: "gustatory-hallucination"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Gustatory hallucination

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Gustatory_and_olfactory_effects\gustatory-hallucination.md`
```md
---
title: 'Gustatory hallucination'
slug: "gustatory-hallucination"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Gustatory hallucination

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Gustatory_and_olfactory_effects\gustatory-intensification.fa.md`
```md
---
title: 'Gustatory intensification'
slug: "gustatory-intensification"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Gustatory intensification

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Gustatory_and_olfactory_effects\gustatory-intensification.md`
```md
---
title: 'Gustatory intensification'
slug: "gustatory-intensification"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Gustatory intensification

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Gustatory_and_olfactory_effects\olfactory-depression.fa.md`
```md
---
title: 'Olfactory depression'
slug: "olfactory-depression"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Olfactory depression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Gustatory_and_olfactory_effects\olfactory-depression.md`
```md
---
title: 'Olfactory depression'
slug: "olfactory-depression"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Olfactory depression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Gustatory_and_olfactory_effects\olfactory-hallucination.fa.md`
```md
---
title: 'Olfactory hallucination'
slug: "olfactory-hallucination"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Olfactory hallucination

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Gustatory_and_olfactory_effects\olfactory-hallucination.md`
```md
---
title: 'Olfactory hallucination'
slug: "olfactory-hallucination"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Olfactory hallucination

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Gustatory_and_olfactory_effects\olfactory-intensification.fa.md`
```md
---
title: 'Olfactory intensification'
slug: "olfactory-intensification"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Olfactory intensification

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Gustatory_and_olfactory_effects\olfactory-intensification.md`
```md
---
title: 'Olfactory intensification'
slug: "olfactory-intensification"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Olfactory intensification

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\abnormal-heartbeat.fa.md`
```md
---
title: 'Abnormal heartbeat'
slug: "abnormal-heartbeat"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Abnormal heartbeat

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\abnormal-heartbeat.md`
```md
---
title: 'Abnormal heartbeat'
slug: "abnormal-heartbeat"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Abnormal heartbeat

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\back-pain.fa.md`
```md
---
title: 'Back pain'
slug: "back-pain"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Back pain

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\back-pain.md`
```md
---
title: 'Back pain'
slug: "back-pain"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Back pain

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\bodily-pressures.fa.md`
```md
---
title: 'Bodily pressures'
slug: "bodily-pressures"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Bodily pressures

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\bodily-pressures.md`
```md
---
title: 'Bodily pressures'
slug: "bodily-pressures"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Bodily pressures

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\bodily.fa.md`
```md
---
title: 'Bodily'
slug: "bodily"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Bodily

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\bodily.md`
```md
---
title: 'Bodily'
slug: "bodily"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Bodily

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\brain-zaps.fa.md`
```md
---
title: 'Brain zaps'
slug: "brain-zaps"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Brain zaps

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\brain-zaps.md`
```md
---
title: 'Brain zaps'
slug: "brain-zaps"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Brain zaps

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\cardiovascular.fa.md`
```md
---
title: 'Cardiovascular'
slug: "cardiovascular"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cardiovascular

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\cardiovascular.md`
```md
---
title: 'Cardiovascular'
slug: "cardiovascular"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cardiovascular

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\cerebrovascular.fa.md`
```md
---
title: 'Cerebrovascular'
slug: "cerebrovascular"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cerebrovascular

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\cerebrovascular.md`
```md
---
title: 'Cerebrovascular'
slug: "cerebrovascular"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cerebrovascular

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\constipation.fa.md`
```md
---
title: 'Constipation'
slug: "constipation"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Constipation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\constipation.md`
```md
---
title: 'Constipation'
slug: "constipation"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Constipation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\decreased-blood-pressure.fa.md`
```md
---
title: 'Decreased blood pressure'
slug: "decreased-blood-pressure"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Decreased blood pressure

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\decreased-blood-pressure.md`
```md
---
title: 'Decreased blood pressure'
slug: "decreased-blood-pressure"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Decreased blood pressure

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\decreased-heart-rate.fa.md`
```md
---
title: 'Decreased heart rate'
slug: "decreased-heart-rate"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Decreased heart rate

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\decreased-heart-rate.md`
```md
---
title: 'Decreased heart rate'
slug: "decreased-heart-rate"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Decreased heart rate

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\dehydration.fa.md`
```md
---
title: 'Dehydration'
slug: "dehydration"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Dehydration

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\dehydration.md`
```md
---
title: 'Dehydration'
slug: "dehydration"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Dehydration

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\diarrhea.fa.md`
```md
---
title: 'Diarrhea'
slug: "diarrhea"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Diarrhea

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\diarrhea.md`
```md
---
title: 'Diarrhea'
slug: "diarrhea"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Diarrhea

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\difficulty-urinating.fa.md`
```md
---
title: 'Difficulty urinating'
slug: "difficulty-urinating"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Difficulty urinating

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\difficulty-urinating.md`
```md
---
title: 'Difficulty urinating'
slug: "difficulty-urinating"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Difficulty urinating

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\dizziness.fa.md`
```md
---
title: 'Dizziness'
slug: "dizziness"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Dizziness

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\dizziness.md`
```md
---
title: 'Dizziness'
slug: "dizziness"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Dizziness

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\dry-mouth.fa.md`
```md
---
title: 'Dry mouth'
slug: "dry-mouth"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Dry mouth

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\dry-mouth.md`
```md
---
title: 'Dry mouth'
slug: "dry-mouth"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Dry mouth

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\frequent-urination.fa.md`
```md
---
title: 'Frequent urination'
slug: "frequent-urination"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Frequent urination

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\frequent-urination.md`
```md
---
title: 'Frequent urination'
slug: "frequent-urination"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Frequent urination

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\headache.fa.md`
```md
---
title: 'Headache'
slug: "headache"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Headache

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\headache.md`
```md
---
title: 'Headache'
slug: "headache"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Headache

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\increased-blood-pressure.fa.md`
```md
---
title: 'Increased blood pressure'
slug: "increased-blood-pressure"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased blood pressure

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\increased-blood-pressure.md`
```md
---
title: 'Increased blood pressure'
slug: "increased-blood-pressure"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased blood pressure

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\increased-bodily-temperature.fa.md`
```md
---
title: 'Increased bodily temperature'
slug: "increased-bodily-temperature"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased bodily temperature

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\increased-bodily-temperature.md`
```md
---
title: 'Increased bodily temperature'
slug: "increased-bodily-temperature"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased bodily temperature

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\increased-heart-rate.fa.md`
```md
---
title: 'Increased heart rate'
slug: "increased-heart-rate"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased heart rate

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\increased-heart-rate.md`
```md
---
title: 'Increased heart rate'
slug: "increased-heart-rate"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased heart rate

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\increased-perspiration.fa.md`
```md
---
title: 'Increased perspiration'
slug: "increased-perspiration"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased perspiration

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\increased-perspiration.md`
```md
---
title: 'Increased perspiration'
slug: "increased-perspiration"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased perspiration

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\increased-phlegm-production.fa.md`
```md
---
title: 'Increased phlegm production'
slug: "increased-phlegm-production"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased phlegm production

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\increased-phlegm-production.md`
```md
---
title: 'Increased phlegm production'
slug: "increased-phlegm-production"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased phlegm production

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\itchiness.fa.md`
```md
---
title: 'Itchiness'
slug: "itchiness"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Itchiness

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\itchiness.md`
```md
---
title: 'Itchiness'
slug: "itchiness"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Itchiness

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\muscle-contractions.fa.md`
```md
---
title: 'Muscle contractions'
slug: "muscle-contractions"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Muscle contractions

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\muscle-contractions.md`
```md
---
title: 'Muscle contractions'
slug: "muscle-contractions"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Muscle contractions

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\muscle-cramps.fa.md`
```md
---
title: 'Muscle cramps'
slug: "muscle-cramps"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Muscle cramps

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\muscle-cramps.md`
```md
---
title: 'Muscle cramps'
slug: "muscle-cramps"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Muscle cramps

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\muscle-tension.fa.md`
```md
---
title: 'Muscle tension'
slug: "muscle-tension"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Muscle tension

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\muscle-tension.md`
```md
---
title: 'Muscle tension'
slug: "muscle-tension"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Muscle tension

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\muscle-twitching.fa.md`
```md
---
title: 'Muscle twitching'
slug: "muscle-twitching"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Muscle twitching

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\muscle-twitching.md`
```md
---
title: 'Muscle twitching'
slug: "muscle-twitching"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Muscle twitching

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\nausea.fa.md`
```md
---
title: 'Nausea'
slug: "nausea"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Nausea

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\nausea.md`
```md
---
title: 'Nausea'
slug: "nausea"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Nausea

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\optical-sliding.fa.md`
```md
---
title: 'Optical sliding'
slug: "optical-sliding"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Optical sliding

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\optical-sliding.md`
```md
---
title: 'Optical sliding'
slug: "optical-sliding"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Optical sliding

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\photophobia.fa.md`
```md
---
title: 'Photophobia'
slug: "photophobia"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Photophobia

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\photophobia.md`
```md
---
title: 'Photophobia'
slug: "photophobia"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Photophobia

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\physical-fatigue.fa.md`
```md
---
title: 'Physical fatigue'
slug: "physical-fatigue"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Physical fatigue

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\physical-fatigue.md`
```md
---
title: 'Physical fatigue'
slug: "physical-fatigue"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Physical fatigue

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\respiratory-depression.fa.md`
```md
---
title: 'Respiratory depression'
slug: "respiratory-depression"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Respiratory depression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\respiratory-depression.md`
```md
---
title: 'Respiratory depression'
slug: "respiratory-depression"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Respiratory depression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\restless-legs.fa.md`
```md
---
title: 'Restless legs'
slug: "restless-legs"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Restless legs

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\restless-legs.md`
```md
---
title: 'Restless legs'
slug: "restless-legs"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Restless legs

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\runny-nose.fa.md`
```md
---
title: 'Runny nose'
slug: "runny-nose"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Runny nose

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\runny-nose.md`
```md
---
title: 'Runny nose'
slug: "runny-nose"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Runny nose

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\seizure.fa.md`
```md
---
title: 'Seizure'
slug: "seizure"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Seizure

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\seizure.md`
```md
---
title: 'Seizure'
slug: "seizure"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Seizure

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\skin-flushing.fa.md`
```md
---
title: 'Skin flushing'
slug: "skin-flushing"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Skin flushing

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\skin-flushing.md`
```md
---
title: 'Skin flushing'
slug: "skin-flushing"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Skin flushing

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\stomach-bloating.fa.md`
```md
---
title: 'Stomach bloating'
slug: "stomach-bloating"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Stomach bloating

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\stomach-bloating.md`
```md
---
title: 'Stomach bloating'
slug: "stomach-bloating"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Stomach bloating

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\stomach-cramp.fa.md`
```md
---
title: 'Stomach cramp'
slug: "stomach-cramp"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Stomach cramp

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\stomach-cramp.md`
```md
---
title: 'Stomach cramp'
slug: "stomach-cramp"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Stomach cramp

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\teeth-grinding.fa.md`
```md
---
title: 'Teeth grinding'
slug: "teeth-grinding"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Teeth grinding

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\teeth-grinding.md`
```md
---
title: 'Teeth grinding'
slug: "teeth-grinding"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Teeth grinding

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\temperature-regulation-suppression.fa.md`
```md
---
title: 'Temperature regulation suppression'
slug: "temperature-regulation-suppression"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Temperature regulation suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\temperature-regulation-suppression.md`
```md
---
title: 'Temperature regulation suppression'
slug: "temperature-regulation-suppression"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Temperature regulation suppression

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\temporary-erectile-dysfunction.fa.md`
```md
---
title: 'Temporary erectile dysfunction'
slug: "temporary-erectile-dysfunction"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Temporary erectile dysfunction

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\temporary-erectile-dysfunction.md`
```md
---
title: 'Temporary erectile dysfunction'
slug: "temporary-erectile-dysfunction"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Temporary erectile dysfunction

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\uncomfortable-physical-effects.fa.md`
```md
---
title: 'Uncomfortable physical effects'
slug: "uncomfortable-physical-effects"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Uncomfortable physical effects

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\uncomfortable-physical-effects.md`
```md
---
title: 'Uncomfortable physical effects'
slug: "uncomfortable-physical-effects"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Uncomfortable physical effects

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\vasoconstriction.fa.md`
```md
---
title: 'Vasoconstriction'
slug: "vasoconstriction"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Vasoconstriction

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\vasoconstriction.md`
```md
---
title: 'Vasoconstriction'
slug: "vasoconstriction"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Vasoconstriction

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\vasodilation.fa.md`
```md
---
title: 'Vasodilation'
slug: "vasodilation"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Vasodilation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\vasodilation.md`
```md
---
title: 'Vasodilation'
slug: "vasodilation"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Vasodilation

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\vibrating-vision.fa.md`
```md
---
title: 'Vibrating vision'
slug: "vibrating-vision"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Vibrating vision

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\vibrating-vision.md`
```md
---
title: 'Vibrating vision'
slug: "vibrating-vision"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Vibrating vision

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\vomiting.fa.md`
```md
---
title: 'Vomiting'
slug: "vomiting"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Vomiting

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\vomiting.md`
```md
---
title: 'Vomiting'
slug: "vomiting"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Vomiting

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\wate.fa.md`
```md
---
title: 'Wate'
slug: "wate"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Wate

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Physical_effects\Uncomfortable physical effects\wate.md`
```md
---
title: 'Wate'
slug: "wate"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Wate

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\Disconnective_effects\cognitive-disconnection.fa.md`
```md
---
title: 'Cognitive disconnection'
slug: "cognitive-disconnection"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cognitive disconnection

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\Disconnective_effects\cognitive-disconnection.md`
```md
---
title: 'Cognitive disconnection'
slug: "cognitive-disconnection"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cognitive disconnection

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\Disconnective_effects\detachment-plateaus.fa.md`
```md
---
title: 'Detachment plateaus'
slug: "detachment-plateaus"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Detachment plateaus

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\Disconnective_effects\detachment-plateaus.md`
```md
---
title: 'Detachment plateaus'
slug: "detachment-plateaus"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Detachment plateaus

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\Disconnective_effects\disconnective-effects.fa.md`
```md
---
title: 'Disconnective_effects'
slug: "disconnective-effects"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Disconnective_effects

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\Disconnective_effects\disconnective-effects.md`
```md
---
title: 'Disconnective_effects'
slug: "disconnective-effects"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Disconnective_effects

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\Disconnective_effects\dj-vu.fa.md`
```md
---
title: 'Déjà vu'
slug: "dj-vu"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Déjà vu

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\Disconnective_effects\dj-vu.md`
```md
---
title: 'Déjà vu'
slug: "dj-vu"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Déjà vu

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\Disconnective_effects\holes-spaces-and-voids.fa.md`
```md
---
title: 'Holes, spaces and voids'
slug: "holes-spaces-and-voids"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Holes, spaces and voids

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\Disconnective_effects\holes-spaces-and-voids.md`
```md
---
title: 'Holes, spaces and voids'
slug: "holes-spaces-and-voids"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Holes, spaces and voids

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\Disconnective_effects\physical-disconnection.fa.md`
```md
---
title: 'Physical disconnection'
slug: "physical-disconnection"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Physical disconnection

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\Disconnective_effects\physical-disconnection.md`
```md
---
title: 'Physical disconnection'
slug: "physical-disconnection"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Physical disconnection

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\Disconnective_effects\structures.fa.md`
```md
---
title: "Structures"
slug: "structures"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Structures

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\Disconnective_effects\structures.md`
```md
---
title: 'Structures'
slug: "structures"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Structures

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\Disconnective_effects\visual-disconnection.fa.md`
```md
---
title: 'Visual disconnection'
slug: "visual-disconnection"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual disconnection

_Page coming soon._

```

---
### `wiki\Psychoactive_Effects\Cognitive_effects\Disconnective_effects\visual-disconnection.md`
```md
---
title: 'Visual disconnection'
slug: "visual-disconnection"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual disconnection

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\14-butanediol.fa.md`
```md
---
title: '1,4-Butanediol'
slug: "14-butanediol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# 1,4-Butanediol

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\14-butanediol.md`
```md
---
title: '1,4-Butanediol'
slug: "14-butanediol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# 1,4-Butanediol

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\2-methyl-2-butanol.fa.md`
```md
---
title: '2-Methyl-2-butanol'
slug: "2-methyl-2-butanol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# 2-Methyl-2-butanol

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\2-methyl-2-butanol.md`
```md
---
title: '2-Methyl-2-butanol'
slug: "2-methyl-2-butanol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# 2-Methyl-2-butanol

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\7-hydroxymitragynine.fa.md`
```md
---
title: '7-Hydroxymitragynine'
slug: "7-hydroxymitragynine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# 7-Hydroxymitragynine

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\7-hydroxymitragynine.md`
```md
---
title: '7-Hydroxymitragynine'
slug: "7-hydroxymitragynine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# 7-Hydroxymitragynine

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\acetylfentanyl.fa.md`
```md
---
title: 'Acetylfentanyl'
slug: "acetylfentanyl"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Acetylfentanyl

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\acetylfentanyl.md`
```md
---
title: 'Acetylfentanyl'
slug: "acetylfentanyl"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Acetylfentanyl

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\alcohol.fa.md`
```md
---
title: 'Alcohol'
slug: "alcohol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Alcohol

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\alcohol.md`
```md
---
title: 'Alcohol'
slug: "alcohol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Alcohol

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\alcohols.fa.md`
```md
---
title: 'Alcohols'
slug: "alcohols"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Alcohols

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\alcohols.md`
```md
---
title: 'Alcohols'
slug: "alcohols"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Alcohols

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\alprazolam.fa.md`
```md
---
title: 'Alprazolam'
slug: "alprazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Alprazolam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\alprazolam.md`
```md
---
title: 'Alprazolam'
slug: "alprazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Alprazolam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\baclofen.fa.md`
```md
---
title: 'Baclofen'
slug: "baclofen"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Baclofen

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\baclofen.md`
```md
---
title: 'Baclofen'
slug: "baclofen"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Baclofen

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\barbiturates.fa.md`
```md
---
title: 'Barbiturates'
slug: "barbiturates"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Barbiturates

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\barbiturates.md`
```md
---
title: 'Barbiturates'
slug: "barbiturates"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Barbiturates

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\benzodiazepines.fa.md`
```md
---
title: 'Benzodiazepines'
slug: "benzodiazepines"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Benzodiazepines

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\benzodiazepines.md`
```md
---
title: 'Benzodiazepines'
slug: "benzodiazepines"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Benzodiazepines

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\bromazepam.fa.md`
```md
---
title: 'Bromazepam'
slug: "bromazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Bromazepam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\bromazepam.md`
```md
---
title: 'Bromazepam'
slug: "bromazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Bromazepam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\buprenorphine.fa.md`
```md
---
title: 'Buprenorphine'
slug: "buprenorphine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Buprenorphine

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\buprenorphine.md`
```md
---
title: 'Buprenorphine'
slug: "buprenorphine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Buprenorphine

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\carisoprodol.fa.md`
```md
---
title: 'Carisoprodol'
slug: "carisoprodol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Carisoprodol

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\carisoprodol.md`
```md
---
title: 'Carisoprodol'
slug: "carisoprodol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Carisoprodol

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\clonazepam.fa.md`
```md
---
title: 'Clonazepam'
slug: "clonazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Clonazepam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\clonazepam.md`
```md
---
title: 'Clonazepam'
slug: "clonazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Clonazepam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\clonazolam.fa.md`
```md
---
title: 'Clonazolam'
slug: "clonazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Clonazolam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\clonazolam.md`
```md
---
title: 'Clonazolam'
slug: "clonazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Clonazolam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\clonidine.fa.md`
```md
---
title: 'Clonidine'
slug: "clonidine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Clonidine

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\clonidine.md`
```md
---
title: 'Clonidine'
slug: "clonidine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Clonidine

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\codeine.fa.md`
```md
---
title: 'Codeine'
slug: "codeine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Codeine

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\codeine.md`
```md
---
title: 'Codeine'
slug: "codeine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Codeine

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\depressants.fa.md`
```md
---
title: 'Depressants'
slug: "depressants"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Depressants

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\depressants.md`
```md
---
title: 'Depressants'
slug: "depressants"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Depressants

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\deschloroetizolam.fa.md`
```md
---
title: 'Deschloroetizolam'
slug: "deschloroetizolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Deschloroetizolam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\deschloroetizolam.md`
```md
---
title: 'Deschloroetizolam'
slug: "deschloroetizolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Deschloroetizolam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\desomorphine.fa.md`
```md
---
title: 'Desomorphine'
slug: "desomorphine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Desomorphine

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\desomorphine.md`
```md
---
title: 'Desomorphine'
slug: "desomorphine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Desomorphine

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\dextropropoxyphene.fa.md`
```md
---
title: 'Dextropropoxyphene'
slug: "dextropropoxyphene"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Dextropropoxyphene

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\dextropropoxyphene.md`
```md
---
title: 'Dextropropoxyphene'
slug: "dextropropoxyphene"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Dextropropoxyphene

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\diacetylmorphine.fa.md`
```md
---
title: 'Diacetylmorphine'
slug: "diacetylmorphine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Diacetylmorphine

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\diacetylmorphine.md`
```md
---
title: 'Diacetylmorphine'
slug: "diacetylmorphine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Diacetylmorphine

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\diazepam.fa.md`
```md
---
title: 'Diazepam'
slug: "diazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Diazepam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\diazepam.md`
```md
---
title: 'Diazepam'
slug: "diazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Diazepam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\diclazepam.fa.md`
```md
---
title: 'Diclazepam'
slug: "diclazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Diclazepam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\diclazepam.md`
```md
---
title: 'Diclazepam'
slug: "diclazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Diclazepam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\dihydrocodeine.fa.md`
```md
---
title: 'Dihydrocodeine'
slug: "dihydrocodeine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Dihydrocodeine

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\dihydrocodeine.md`
```md
---
title: 'Dihydrocodeine'
slug: "dihydrocodeine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Dihydrocodeine

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\diphenhydramine.fa.md`
```md
---
title: 'Diphenhydramine'
slug: "diphenhydramine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Diphenhydramine

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\diphenhydramine.md`
```md
---
title: 'Diphenhydramine'
slug: "diphenhydramine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Diphenhydramine

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\eszopiclone.fa.md`
```md
---
title: 'Eszopiclone'
slug: "eszopiclone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Eszopiclone

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\eszopiclone.md`
```md
---
title: 'Eszopiclone'
slug: "eszopiclone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Eszopiclone

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\ethylmorphine.fa.md`
```md
---
title: 'Ethylmorphine'
slug: "ethylmorphine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Ethylmorphine

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\ethylmorphine.md`
```md
---
title: 'Ethylmorphine'
slug: "ethylmorphine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Ethylmorphine

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\etizolam.fa.md`
```md
---
title: 'Etizolam'
slug: "etizolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Etizolam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\etizolam.md`
```md
---
title: 'Etizolam'
slug: "etizolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Etizolam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\f-phenibut.fa.md`
```md
---
title: 'F-Phenibut'
slug: "f-phenibut"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# F-Phenibut

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\f-phenibut.md`
```md
---
title: 'F-Phenibut'
slug: "f-phenibut"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# F-Phenibut

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\fentanyl.fa.md`
```md
---
title: 'Fentanyl'
slug: "fentanyl"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Fentanyl

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\fentanyl.md`
```md
---
title: 'Fentanyl'
slug: "fentanyl"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Fentanyl

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\flualprazolam.fa.md`
```md
---
title: 'Flualprazolam'
slug: "flualprazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Flualprazolam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\flualprazolam.md`
```md
---
title: 'Flualprazolam'
slug: "flualprazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Flualprazolam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\flubromazepam.fa.md`
```md
---
title: 'Flubromazepam'
slug: "flubromazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Flubromazepam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\flubromazepam.md`
```md
---
title: 'Flubromazepam'
slug: "flubromazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Flubromazepam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\flubromazolam.fa.md`
```md
---
title: 'Flubromazolam'
slug: "flubromazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Flubromazolam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\flubromazolam.md`
```md
---
title: 'Flubromazolam'
slug: "flubromazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Flubromazolam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\flunitrazepam.fa.md`
```md
---
title: 'Flunitrazepam'
slug: "flunitrazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Flunitrazepam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\flunitrazepam.md`
```md
---
title: 'Flunitrazepam'
slug: "flunitrazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Flunitrazepam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\flunitrazolam.fa.md`
```md
---
title: 'Flunitrazolam'
slug: "flunitrazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Flunitrazolam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\flunitrazolam.md`
```md
---
title: 'Flunitrazolam'
slug: "flunitrazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Flunitrazolam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\gabaa-1-agonists.fa.md`
```md
---
title: 'GABAA-α1 agonists'
slug: "gabaa-1-agonists"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# GABAA-α1 agonists

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\gabaa-1-agonists.md`
```md
---
title: 'GABAA-α1 agonists'
slug: "gabaa-1-agonists"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# GABAA-α1 agonists

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\gabapentin.fa.md`
```md
---
title: 'Gabapentin'
slug: "gabapentin"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Gabapentin

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\gabapentin.md`
```md
---
title: 'Gabapentin'
slug: "gabapentin"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Gabapentin

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\gabapentinoids.fa.md`
```md
---
title: 'Gabapentinoids'
slug: "gabapentinoids"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Gabapentinoids

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\gabapentinoids.md`
```md
---
title: 'Gabapentinoids'
slug: "gabapentinoids"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Gabapentinoids

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\gaboxadol.fa.md`
```md
---
title: 'Gaboxadol'
slug: "gaboxadol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Gaboxadol

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\gaboxadol.md`
```md
---
title: 'Gaboxadol'
slug: "gaboxadol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Gaboxadol

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\gbl.fa.md`
```md
---
title: 'GBL'
slug: "gbl"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# GBL

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\gbl.md`
```md
---
title: 'GBL'
slug: "gbl"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# GBL

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\ghb.fa.md`
```md
---
title: 'GHB'
slug: "ghb"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# GHB

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\ghb.md`
```md
---
title: 'GHB'
slug: "ghb"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# GHB

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\hydrocodone.fa.md`
```md
---
title: 'Hydrocodone'
slug: "hydrocodone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Hydrocodone

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\hydrocodone.md`
```md
---
title: 'Hydrocodone'
slug: "hydrocodone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Hydrocodone

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\hydromorphone.fa.md`
```md
---
title: 'Hydromorphone'
slug: "hydromorphone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Hydromorphone

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\hydromorphone.md`
```md
---
title: 'Hydromorphone'
slug: "hydromorphone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Hydromorphone

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\ibotenic-acid.fa.md`
```md
---
title: 'Ibotenic acid'
slug: "ibotenic-acid"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Ibotenic acid

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\ibotenic-acid.md`
```md
---
title: 'Ibotenic acid'
slug: "ibotenic-acid"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Ibotenic acid

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\kava.fa.md`
```md
---
title: 'Kava'
slug: "kava"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Kava

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\kava.md`
```md
---
title: 'Kava'
slug: "kava"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Kava

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\kratom.fa.md`
```md
---
title: 'Kratom'
slug: "kratom"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Kratom

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\kratom.md`
```md
---
title: 'Kratom'
slug: "kratom"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Kratom

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\lorazepam.fa.md`
```md
---
title: 'Lorazepam'
slug: "lorazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Lorazepam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\lorazepam.md`
```md
---
title: 'Lorazepam'
slug: "lorazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Lorazepam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\lormetazepam.fa.md`
```md
---
title: 'Lormetazepam'
slug: "lormetazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Lormetazepam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\lormetazepam.md`
```md
---
title: 'Lormetazepam'
slug: "lormetazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Lormetazepam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\methadone.fa.md`
```md
---
title: 'Methadone'
slug: "methadone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Methadone

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\methadone.md`
```md
---
title: 'Methadone'
slug: "methadone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Methadone

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\methaqualone.fa.md`
```md
---
title: 'Methaqualone'
slug: "methaqualone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Methaqualone

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\methaqualone.md`
```md
---
title: 'Methaqualone'
slug: "methaqualone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Methaqualone

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\metizolam.fa.md`
```md
---
title: 'Metizolam'
slug: "metizolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Metizolam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\metizolam.md`
```md
---
title: 'Metizolam'
slug: "metizolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Metizolam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\midazolam.fa.md`
```md
---
title: 'Midazolam'
slug: "midazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Midazolam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\midazolam.md`
```md
---
title: 'Midazolam'
slug: "midazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Midazolam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\mirtazapine.fa.md`
```md
---
title: 'Mirtazapine'
slug: "mirtazapine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Mirtazapine

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\mirtazapine.md`
```md
---
title: 'Mirtazapine'
slug: "mirtazapine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Mirtazapine

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\morphine.fa.md`
```md
---
title: 'Morphine'
slug: "morphine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Morphine

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\morphine.md`
```md
---
title: 'Morphine'
slug: "morphine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Morphine

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\muscimol.fa.md`
```md
---
title: 'Muscimol'
slug: "muscimol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Muscimol

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\muscimol.md`
```md
---
title: 'Muscimol'
slug: "muscimol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Muscimol

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\nifoxipam.fa.md`
```md
---
title: 'Nifoxipam'
slug: "nifoxipam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Nifoxipam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\nifoxipam.md`
```md
---
title: 'Nifoxipam'
slug: "nifoxipam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Nifoxipam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\nitromethaqualone.fa.md`
```md
---
title: 'Nitromethaqualone'
slug: "nitromethaqualone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Nitromethaqualone

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\nitromethaqualone.md`
```md
---
title: 'Nitromethaqualone'
slug: "nitromethaqualone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Nitromethaqualone

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\o-desmethyltramadol.fa.md`
```md
---
title: 'O-Desmethyltramadol'
slug: "o-desmethyltramadol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# O-Desmethyltramadol

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\o-desmethyltramadol.md`
```md
---
title: 'O-Desmethyltramadol'
slug: "o-desmethyltramadol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# O-Desmethyltramadol

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\opioids.fa.md`
```md
---
title: 'Opioids'
slug: "opioids"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Opioids

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\opioids.md`
```md
---
title: 'Opioids'
slug: "opioids"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Opioids

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\other-gabaergics.fa.md`
```md
---
title: 'Other GABAergics'
slug: "other-gabaergics"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Other GABAergics

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\other-gabaergics.md`
```md
---
title: 'Other GABAergics'
slug: "other-gabaergics"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Other GABAergics

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\oxycodone.fa.md`
```md
---
title: 'Oxycodone'
slug: "oxycodone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Oxycodone

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\oxycodone.md`
```md
---
title: 'Oxycodone'
slug: "oxycodone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Oxycodone

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\oxymorphone.fa.md`
```md
---
title: 'Oxymorphone'
slug: "oxymorphone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Oxymorphone

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\oxymorphone.md`
```md
---
title: 'Oxymorphone'
slug: "oxymorphone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Oxymorphone

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\pentobarbital.fa.md`
```md
---
title: 'Pentobarbital'
slug: "pentobarbital"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Pentobarbital

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\pentobarbital.md`
```md
---
title: 'Pentobarbital'
slug: "pentobarbital"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Pentobarbital

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\pethidine.fa.md`
```md
---
title: 'Pethidine'
slug: "pethidine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Pethidine

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\pethidine.md`
```md
---
title: 'Pethidine'
slug: "pethidine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Pethidine

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\phenibut.fa.md`
```md
---
title: 'Phenibut'
slug: "phenibut"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Phenibut

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\phenibut.md`
```md
---
title: 'Phenibut'
slug: "phenibut"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Phenibut

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\phenobarbital.fa.md`
```md
---
title: 'Phenobarbital'
slug: "phenobarbital"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Phenobarbital

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\phenobarbital.md`
```md
---
title: 'Phenobarbital'
slug: "phenobarbital"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Phenobarbital

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\pregabalin.fa.md`
```md
---
title: 'Pregabalin'
slug: "pregabalin"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Pregabalin

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\pregabalin.md`
```md
---
title: 'Pregabalin'
slug: "pregabalin"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Pregabalin

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\pyrazolam.fa.md`
```md
---
title: 'Pyrazolam'
slug: "pyrazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Pyrazolam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\pyrazolam.md`
```md
---
title: 'Pyrazolam'
slug: "pyrazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Pyrazolam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\secobarbital.fa.md`
```md
---
title: 'Secobarbital'
slug: "secobarbital"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Secobarbital

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\secobarbital.md`
```md
---
title: 'Secobarbital'
slug: "secobarbital"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Secobarbital

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\sufentanil.fa.md`
```md
---
title: 'Sufentanil'
slug: "sufentanil"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Sufentanil

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\sufentanil.md`
```md
---
title: 'Sufentanil'
slug: "sufentanil"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Sufentanil

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\tapentadol.fa.md`
```md
---
title: 'Tapentadol'
slug: "tapentadol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Tapentadol

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\tapentadol.md`
```md
---
title: 'Tapentadol'
slug: "tapentadol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Tapentadol

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\temazepam.fa.md`
```md
---
title: 'Temazepam'
slug: "temazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Temazepam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\temazepam.md`
```md
---
title: 'Temazepam'
slug: "temazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Temazepam

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\thienodiazepines.fa.md`
```md
---
title: 'Thienodiazepines'
slug: "thienodiazepines"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Thienodiazepines

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\thienodiazepines.md`
```md
---
title: 'Thienodiazepines'
slug: "thienodiazepines"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Thienodiazepines

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\tizanidine.fa.md`
```md
---
title: 'Tizanidine'
slug: "tizanidine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Tizanidine

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\tizanidine.md`
```md
---
title: 'Tizanidine'
slug: "tizanidine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Tizanidine

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\tramadol.fa.md`
```md
---
title: 'Tramadol'
slug: "tramadol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Tramadol

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\tramadol.md`
```md
---
title: 'Tramadol'
slug: "tramadol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Tramadol

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\u-47700.fa.md`
```md
---
title: 'U-47700'
slug: "u-47700"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# U-47700

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\u-47700.md`
```md
---
title: 'U-47700'
slug: "u-47700"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# U-47700

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\zolpidem.fa.md`
```md
---
title: 'Zolpidem'
slug: "zolpidem"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Zolpidem

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\zolpidem.md`
```md
---
title: 'Zolpidem'
slug: "zolpidem"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Zolpidem

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\zopiclone.fa.md`
```md
---
title: 'Zopiclone'
slug: "zopiclone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Zopiclone

_Page coming soon._

```

---
### `wiki\Psychoactives\Depressants\zopiclone.md`
```md
---
title: 'Zopiclone'
slug: "zopiclone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Zopiclone

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\acacia-confusa.fa.md`
```md
---
title: 'Acacia confusa'
slug: "acacia-confusa"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Acacia confusa

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\acacia-confusa.md`
```md
---
title: 'Acacia confusa'
slug: "acacia-confusa"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Acacia confusa

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\amanita-muscaria.fa.md`
```md
---
title: 'Amanita muscaria'
slug: "amanita-muscaria"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Amanita muscaria

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\amanita-muscaria.md`
```md
---
title: 'Amanita muscaria'
slug: "amanita-muscaria"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Amanita muscaria

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\argyreia-nervosa.fa.md`
```md
---
title: 'Argyreia nervosa'
slug: "argyreia-nervosa"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Argyreia nervosa

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\argyreia-nervosa.md`
```md
---
title: 'Argyreia nervosa'
slug: "argyreia-nervosa"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Argyreia nervosa

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\banisteriopsis-caapi.fa.md`
```md
---
title: 'Banisteriopsis caapi'
slug: "banisteriopsis-caapi"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Banisteriopsis caapi

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\banisteriopsis-caapi.md`
```md
---
title: 'Banisteriopsis caapi'
slug: "banisteriopsis-caapi"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Banisteriopsis caapi

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\blue-lotus.fa.md`
```md
---
title: 'Blue Lotus'
slug: "blue-lotus"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Blue Lotus

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\blue-lotus.md`
```md
---
title: 'Blue Lotus'
slug: "blue-lotus"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Blue Lotus

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\cannabis.fa.md`
```md
---
title: 'Cannabis'
slug: "cannabis"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Cannabis

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\cannabis.md`
```md
---
title: 'Cannabis'
slug: "cannabis"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Cannabis

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\datura.fa.md`
```md
---
title: 'Datura'
slug: "datura"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Datura

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\datura.md`
```md
---
title: 'Datura'
slug: "datura"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Datura

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\entheogens.fa.md`
```md
---
title: 'Entheogens'
slug: "entheogens"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Entheogens

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\entheogens.md`
```md
---
title: 'Entheogens'
slug: "entheogens"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Entheogens

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\iboga.fa.md`
```md
---
title: 'Iboga'
slug: "iboga"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Iboga

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\iboga.md`
```md
---
title: 'Iboga'
slug: "iboga"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Iboga

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\ipomoea-tricolor.fa.md`
```md
---
title: 'Ipomoea tricolor'
slug: "ipomoea-tricolor"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Ipomoea tricolor

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\ipomoea-tricolor.md`
```md
---
title: 'Ipomoea tricolor'
slug: "ipomoea-tricolor"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Ipomoea tricolor

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\mimosa-hostilis.fa.md`
```md
---
title: 'Mimosa hostilis'
slug: "mimosa-hostilis"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Mimosa hostilis

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\mimosa-hostilis.md`
```md
---
title: 'Mimosa hostilis'
slug: "mimosa-hostilis"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Mimosa hostilis

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\nicotiana.fa.md`
```md
---
title: 'Nicotiana'
slug: "nicotiana"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Nicotiana

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\nicotiana.md`
```md
---
title: 'Nicotiana'
slug: "nicotiana"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Nicotiana

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\peyote.fa.md`
```md
---
title: 'Peyote'
slug: "peyote"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Peyote

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\peyote.md`
```md
---
title: 'Peyote'
slug: "peyote"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Peyote

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\psilocybin-mushrooms.fa.md`
```md
---
title: 'Psilocybin mushrooms'
slug: "psilocybin-mushrooms"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Psilocybin mushrooms

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\psilocybin-mushrooms.md`
```md
---
title: 'Psilocybin mushrooms'
slug: "psilocybin-mushrooms"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Psilocybin mushrooms

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\salvia-divinorum.fa.md`
```md
---
title: 'Salvia divinorum'
slug: "salvia-divinorum"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Salvia divinorum

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\salvia-divinorum.md`
```md
---
title: 'Salvia divinorum'
slug: "salvia-divinorum"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Salvia divinorum

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\san-pedro.fa.md`
```md
---
title: 'San Pedro'
slug: "san-pedro"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# San Pedro

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\san-pedro.md`
```md
---
title: 'San Pedro'
slug: "san-pedro"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# San Pedro

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\syrian-rue.fa.md`
```md
---
title: 'Syrian rue'
slug: "syrian-rue"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Syrian rue

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\syrian-rue.md`
```md
---
title: 'Syrian rue'
slug: "syrian-rue"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Syrian rue

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\yopo.fa.md`
```md
---
title: 'Yopo'
slug: "yopo"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Yopo

_Page coming soon._

```

---
### `wiki\Psychoactives\Entheogens\yopo.md`
```md
---
title: 'Yopo'
slug: "yopo"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Yopo

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\hallucinogens.fa.md`
```md
---
title: 'hallucinogens'
slug: "hallucinogens"
lang: "en"
category: 'hallucinogens'
weight: 1000
template: "wiki"
summary: ''
---
```

---
### `wiki\Psychoactives\Hallucinogens\hallucinogens.md`
```md
---
title: 'hallucinogens'
slug: "hallucinogens"
lang: "en"
category: 'hallucinogens'
weight: 1000
template: "wiki"
summary: ''
---
```

---
### `wiki\Psychoactives\Miscellaneous\5-hydroxytryptophan.fa.md`
```md
---
title: '5-Hydroxytryptophan'
slug: "5-hydroxytryptophan"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# 5-Hydroxytryptophan

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\5-hydroxytryptophan.md`
```md
---
title: '5-Hydroxytryptophan'
slug: "5-hydroxytryptophan"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# 5-Hydroxytryptophan

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\acetylcholine-boosters.fa.md`
```md
---
title: 'Acetylcholine boosters'
slug: "acetylcholine-boosters"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Acetylcholine boosters

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\acetylcholine-boosters.md`
```md
---
title: 'Acetylcholine boosters'
slug: "acetylcholine-boosters"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Acetylcholine boosters

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\acetylcholinesterase-inhibitors.fa.md`
```md
---
title: 'Acetylcholinesterase inhibitors'
slug: "acetylcholinesterase-inhibitors"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Acetylcholinesterase inhibitors

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\acetylcholinesterase-inhibitors.md`
```md
---
title: 'Acetylcholinesterase inhibitors'
slug: "acetylcholinesterase-inhibitors"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Acetylcholinesterase inhibitors

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\alkyl-nitrites.fa.md`
```md
---
title: 'Alkyl nitrites'
slug: "alkyl-nitrites"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Alkyl nitrites

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\alkyl-nitrites.md`
```md
---
title: 'Alkyl nitrites'
slug: "alkyl-nitrites"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Alkyl nitrites

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\amyl-nitrite.fa.md`
```md
---
title: 'Amyl nitrite'
slug: "amyl-nitrite"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Amyl nitrite

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\amyl-nitrite.md`
```md
---
title: 'Amyl nitrite'
slug: "amyl-nitrite"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Amyl nitrite

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\ayahuasca.fa.md`
```md
---
title: 'Ayahuasca'
slug: "ayahuasca"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Ayahuasca

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\ayahuasca.md`
```md
---
title: 'Ayahuasca'
slug: "ayahuasca"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Ayahuasca

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\calea-ternifolia.fa.md`
```md
---
title: 'Calea ternifolia'
slug: "calea-ternifolia"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Calea ternifolia

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\calea-ternifolia.md`
```md
---
title: 'Calea ternifolia'
slug: "calea-ternifolia"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Calea ternifolia

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\changa.fa.md`
```md
---
title: 'Changa'
slug: "changa"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Changa

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\changa.md`
```md
---
title: 'Changa'
slug: "changa"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Changa

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\chloroform.fa.md`
```md
---
title: 'Chloroform'
slug: "chloroform"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Chloroform

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\chloroform.md`
```md
---
title: 'Chloroform'
slug: "chloroform"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Chloroform

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\diethyl-ether.fa.md`
```md
---
title: 'Diethyl ether'
slug: "diethyl-ether"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Diethyl ether

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\diethyl-ether.md`
```md
---
title: 'Diethyl ether'
slug: "diethyl-ether"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Diethyl ether

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\dxm-and-dph.fa.md`
```md
---
title: 'DXM & DPH'
slug: "dxm-and-dph"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# DXM & DPH

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\dxm-and-dph.md`
```md
---
title: 'DXM & DPH'
slug: "dxm-and-dph"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# DXM & DPH

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\dxm.fa.md`
```md
---
title: 'DXM'
slug: "dxm"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# DXM

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\dxm.md`
```md
---
title: 'DXM'
slug: "dxm"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# DXM

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\entada-rheedii.fa.md`
```md
---
title: 'Entada rheedii'
slug: "entada-rheedii"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Entada rheedii

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\entada-rheedii.md`
```md
---
title: 'Entada rheedii'
slug: "entada-rheedii"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Entada rheedii

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\galantamine.fa.md`
```md
---
title: 'Galantamine'
slug: "galantamine"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Galantamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\galantamine.md`
```md
---
title: 'Galantamine'
slug: "galantamine"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Galantamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\ibogaine.fa.md`
```md
---
title: 'Ibogaine'
slug: "ibogaine"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Ibogaine

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\ibogaine.md`
```md
---
title: 'Ibogaine'
slug: "ibogaine"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Ibogaine

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\inhalants.fa.md`
```md
---
title: 'Inhalants'
slug: "inhalants"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Inhalants

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\inhalants.md`
```md
---
title: 'Inhalants'
slug: "inhalants"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Inhalants

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\isobutyl-nitrite.fa.md`
```md
---
title: 'Isobutyl nitrite'
slug: "isobutyl-nitrite"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Isobutyl nitrite

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\isobutyl-nitrite.md`
```md
---
title: 'Isobutyl nitrite'
slug: "isobutyl-nitrite"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Isobutyl nitrite

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\isopropyl-nitrite.fa.md`
```md
---
title: 'Isopropyl nitrite'
slug: "isopropyl-nitrite"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Isopropyl nitrite

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\isopropyl-nitrite.md`
```md
---
title: 'Isopropyl nitrite'
slug: "isopropyl-nitrite"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Isopropyl nitrite

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\miscellaneous.fa.md`
```md
---
title: 'Miscellaneous'
slug: "miscellaneous"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Miscellaneous

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\miscellaneous.md`
```md
---
title: 'Miscellaneous'
slug: "miscellaneous"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Miscellaneous

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\nitrous-oxide.fa.md`
```md
---
title: 'Nitrous oxide'
slug: "nitrous-oxide"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Nitrous oxide

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\nitrous-oxide.md`
```md
---
title: 'Nitrous oxide'
slug: "nitrous-oxide"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Nitrous oxide

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\oneirogens.fa.md`
```md
---
title: 'Oneirogens'
slug: "oneirogens"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Oneirogens

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\oneirogens.md`
```md
---
title: 'Oneirogens'
slug: "oneirogens"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Oneirogens

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\opioid-receptor-agonists.fa.md`
```md
---
title: 'κ-Opioid receptor agonists'
slug: "opioid-receptor-agonists"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# κ-Opioid receptor agonists

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\opioid-receptor-agonists.md`
```md
---
title: 'κ-Opioid receptor agonists'
slug: "opioid-receptor-agonists"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# κ-Opioid receptor agonists

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\polysubstance-combinations.fa.md`
```md
---
title: 'Polysubstance combinations'
slug: "polysubstance-combinations"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Polysubstance combinations

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\polysubstance-combinations.md`
```md
---
title: 'Polysubstance combinations'
slug: "polysubstance-combinations"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Polysubstance combinations

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\progesterone.fa.md`
```md
---
title: 'Progesterone'
slug: "progesterone"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Progesterone

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\progesterone.md`
```md
---
title: 'Progesterone'
slug: "progesterone"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Progesterone

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\salvinorin-a.fa.md`
```md
---
title: 'Salvinorin A'
slug: "salvinorin-a"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Salvinorin A

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\salvinorin-a.md`
```md
---
title: 'Salvinorin A'
slug: "salvinorin-a"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Salvinorin A

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\salvinorin-b-methoxymethyl-ether.fa.md`
```md
---
title: 'Salvinorin B methoxymethyl ether'
slug: "salvinorin-b-methoxymethyl-ether"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Salvinorin B methoxymethyl ether

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\salvinorin-b-methoxymethyl-ether.md`
```md
---
title: 'Salvinorin B methoxymethyl ether'
slug: "salvinorin-b-methoxymethyl-ether"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Salvinorin B methoxymethyl ether

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\sigmaergics.fa.md`
```md
---
title: 'Sigmaergics'
slug: "sigmaergics"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Sigmaergics

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\sigmaergics.md`
```md
---
title: 'Sigmaergics'
slug: "sigmaergics"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Sigmaergics

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\various.fa.md`
```md
---
title: 'Various'
slug: "various"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Various

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\various.md`
```md
---
title: 'Various'
slug: "various"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Various

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\xenon.fa.md`
```md
---
title: 'Xenon'
slug: "xenon"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Xenon

_Page coming soon._

```

---
### `wiki\Psychoactives\Miscellaneous\xenon.md`
```md
---
title: 'Xenon'
slug: "xenon"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Xenon

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\2-ai.fa.md`
```md
---
title: '2-AI'
slug: "2-ai"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 2-AI

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\2-ai.md`
```md
---
title: '2-AI'
slug: "2-ai"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 2-AI

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\2-fa.fa.md`
```md
---
title: '2-FA'
slug: "2-fa"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 2-FA

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\2-fa.md`
```md
---
title: '2-FA'
slug: "2-fa"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 2-FA

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\2-fea.fa.md`
```md
---
title: '2-FEA'
slug: "2-fea"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 2-FEA

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\2-fea.md`
```md
---
title: '2-FEA'
slug: "2-fea"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 2-FEA

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\2-fma.fa.md`
```md
---
title: '2-FMA'
slug: "2-fma"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 2-FMA

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\2-fma.md`
```md
---
title: '2-FMA'
slug: "2-fma"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 2-FMA

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\3-fa.fa.md`
```md
---
title: '3-FA'
slug: "3-fa"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 3-FA

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\3-fa.md`
```md
---
title: '3-FA'
slug: "3-fa"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 3-FA

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\3-fea.fa.md`
```md
---
title: '3-FEA'
slug: "3-fea"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 3-FEA

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\3-fea.md`
```md
---
title: '3-FEA'
slug: "3-fea"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 3-FEA

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\3-fma.fa.md`
```md
---
title: '3-FMA'
slug: "3-fma"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 3-FMA

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\3-fma.md`
```md
---
title: '3-FMA'
slug: "3-fma"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 3-FMA

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\3-fpm.fa.md`
```md
---
title: '3-FPM'
slug: "3-fpm"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 3-FPM

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\3-fpm.md`
```md
---
title: '3-FPM'
slug: "3-fpm"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 3-FPM

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\3-mmc.fa.md`
```md
---
title: '3-MMC'
slug: "3-mmc"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 3-MMC

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\3-mmc.md`
```md
---
title: '3-MMC'
slug: "3-mmc"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 3-MMC

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\34-ctmp.fa.md`
```md
---
title: '3,4-CTMP'
slug: "34-ctmp"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 3,4-CTMP

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\34-ctmp.md`
```md
---
title: '3,4-CTMP'
slug: "34-ctmp"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 3,4-CTMP

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\4-fa.fa.md`
```md
---
title: '4-FA'
slug: "4-fa"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 4-FA

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\4-fa.md`
```md
---
title: '4-FA'
slug: "4-fa"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 4-FA

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\4-fma.fa.md`
```md
---
title: '4-FMA'
slug: "4-fma"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 4-FMA

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\4-fma.md`
```md
---
title: '4-FMA'
slug: "4-fma"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 4-FMA

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\4f-eph.fa.md`
```md
---
title: '4F-EPH'
slug: "4f-eph"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 4F-EPH

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\4f-eph.md`
```md
---
title: '4F-EPH'
slug: "4f-eph"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 4F-EPH

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\4f-mph.fa.md`
```md
---
title: '4F-MPH'
slug: "4f-mph"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 4F-MPH

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\4f-mph.md`
```md
---
title: '4F-MPH'
slug: "4f-mph"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 4F-MPH

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\8-chlorotheophylline.fa.md`
```md
---
title: '8-Chlorotheophylline'
slug: "8-chlorotheophylline"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 8-Chlorotheophylline

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\8-chlorotheophylline.md`
```md
---
title: '8-Chlorotheophylline'
slug: "8-chlorotheophylline"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 8-Chlorotheophylline

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\aminorexes.fa.md`
```md
---
title: 'Aminorexes'
slug: "aminorexes"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Aminorexes

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\aminorexes.md`
```md
---
title: 'Aminorexes'
slug: "aminorexes"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Aminorexes

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\amphetamine.fa.md`
```md
---
title: 'Amphetamine'
slug: "amphetamine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Amphetamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\amphetamine.md`
```md
---
title: 'Amphetamine'
slug: "amphetamine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Amphetamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\amphetamines.fa.md`
```md
---
title: 'Amphetamines'
slug: "amphetamines"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Amphetamines

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\amphetamines.md`
```md
---
title: 'Amphetamines'
slug: "amphetamines"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Amphetamines

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\butylone.fa.md`
```md
---
title: 'Butylone'
slug: "butylone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Butylone

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\butylone.md`
```md
---
title: 'Butylone'
slug: "butylone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Butylone

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\caffeine.fa.md`
```md
---
title: 'Caffeine'
slug: "caffeine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Caffeine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\caffeine.md`
```md
---
title: 'Caffeine'
slug: "caffeine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Caffeine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\cathinone.fa.md`
```md
---
title: 'Cathinone'
slug: "cathinone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Cathinone

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\cathinone.md`
```md
---
title: 'Cathinone'
slug: "cathinone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Cathinone

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\cathinones.fa.md`
```md
---
title: 'Cathinones'
slug: "cathinones"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Cathinones

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\cathinones.md`
```md
---
title: 'Cathinones'
slug: "cathinones"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Cathinones

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\cocaine.fa.md`
```md
---
title: 'Cocaine'
slug: "cocaine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Cocaine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\cocaine.md`
```md
---
title: 'Cocaine'
slug: "cocaine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Cocaine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\cyclazodone.fa.md`
```md
---
title: 'Cyclazodone'
slug: "cyclazodone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Cyclazodone

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\cyclazodone.md`
```md
---
title: 'Cyclazodone'
slug: "cyclazodone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Cyclazodone

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\desoxypipradrol.fa.md`
```md
---
title: 'Desoxypipradrol'
slug: "desoxypipradrol"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Desoxypipradrol

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\desoxypipradrol.md`
```md
---
title: 'Desoxypipradrol'
slug: "desoxypipradrol"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Desoxypipradrol

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\dexmethylphenidate.fa.md`
```md
---
title: 'Dexmethylphenidate'
slug: "dexmethylphenidate"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Dexmethylphenidate

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\dexmethylphenidate.md`
```md
---
title: 'Dexmethylphenidate'
slug: "dexmethylphenidate"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Dexmethylphenidate

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\dextroamphetamine.fa.md`
```md
---
title: 'Dextroamphetamine'
slug: "dextroamphetamine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Dextroamphetamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\dextroamphetamine.md`
```md
---
title: 'Dextroamphetamine'
slug: "dextroamphetamine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Dextroamphetamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\ephedrine.fa.md`
```md
---
title: 'Ephedrine'
slug: "ephedrine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Ephedrine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\ephedrine.md`
```md
---
title: 'Ephedrine'
slug: "ephedrine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Ephedrine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\ephylone.fa.md`
```md
---
title: 'Ephylone'
slug: "ephylone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Ephylone

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\ephylone.md`
```md
---
title: 'Ephylone'
slug: "ephylone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Ephylone

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\ethcathinone.fa.md`
```md
---
title: 'Ethcathinone'
slug: "ethcathinone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Ethcathinone

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\ethcathinone.md`
```md
---
title: 'Ethcathinone'
slug: "ethcathinone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Ethcathinone

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\ethylone.fa.md`
```md
---
title: 'Ethylone'
slug: "ethylone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Ethylone

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\ethylone.md`
```md
---
title: 'Ethylone'
slug: "ethylone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Ethylone

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\ethylphenidate.fa.md`
```md
---
title: 'Ethylphenidate'
slug: "ethylphenidate"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Ethylphenidate

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\ethylphenidate.md`
```md
---
title: 'Ethylphenidate'
slug: "ethylphenidate"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Ethylphenidate

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\fenethylline.fa.md`
```md
---
title: 'Fenethylline'
slug: "fenethylline"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Fenethylline

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\fenethylline.md`
```md
---
title: 'Fenethylline'
slug: "fenethylline"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Fenethylline

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\hexedrone.fa.md`
```md
---
title: 'Hexedrone'
slug: "hexedrone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Hexedrone

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\hexedrone.md`
```md
---
title: 'Hexedrone'
slug: "hexedrone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Hexedrone

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\isopropylphenidate.fa.md`
```md
---
title: 'Isopropylphenidate'
slug: "isopropylphenidate"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Isopropylphenidate

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\isopropylphenidate.md`
```md
---
title: 'Isopropylphenidate'
slug: "isopropylphenidate"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Isopropylphenidate

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\lisdexamfetamine.fa.md`
```md
---
title: 'Lisdexamfetamine'
slug: "lisdexamfetamine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Lisdexamfetamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\lisdexamfetamine.md`
```md
---
title: 'Lisdexamfetamine'
slug: "lisdexamfetamine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Lisdexamfetamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\mcpp.fa.md`
```md
---
title: 'mCPP'
slug: "mcpp"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# mCPP

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\mcpp.md`
```md
---
title: 'mCPP'
slug: "mcpp"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# mCPP

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\mdpv.fa.md`
```md
---
title: 'MDPV'
slug: "mdpv"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# MDPV

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\mdpv.md`
```md
---
title: 'MDPV'
slug: "mdpv"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# MDPV

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\mephedrone.fa.md`
```md
---
title: 'Mephedrone'
slug: "mephedrone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Mephedrone

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\mephedrone.md`
```md
---
title: 'Mephedrone'
slug: "mephedrone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Mephedrone

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\methamphetamine.fa.md`
```md
---
title: 'Methamphetamine'
slug: "methamphetamine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Methamphetamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\methamphetamine.md`
```md
---
title: 'Methamphetamine'
slug: "methamphetamine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Methamphetamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\methcathinone.fa.md`
```md
---
title: 'Methcathinone'
slug: "methcathinone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Methcathinone

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\methcathinone.md`
```md
---
title: 'Methcathinone'
slug: "methcathinone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Methcathinone

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\methiopropamine.fa.md`
```md
---
title: 'Methiopropamine'
slug: "methiopropamine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Methiopropamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\methiopropamine.md`
```md
---
title: 'Methiopropamine'
slug: "methiopropamine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Methiopropamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\methylnaphthidate.fa.md`
```md
---
title: 'Methylnaphthidate'
slug: "methylnaphthidate"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Methylnaphthidate

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\methylnaphthidate.md`
```md
---
title: 'Methylnaphthidate'
slug: "methylnaphthidate"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Methylnaphthidate

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\methylphenidate.fa.md`
```md
---
title: 'Methylphenidate'
slug: "methylphenidate"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Methylphenidate

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\methylphenidate.md`
```md
---
title: 'Methylphenidate'
slug: "methylphenidate"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Methylphenidate

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\mexedrone.fa.md`
```md
---
title: 'Mexedrone'
slug: "mexedrone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Mexedrone

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\mexedrone.md`
```md
---
title: 'Mexedrone'
slug: "mexedrone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Mexedrone

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\n-ethylhexedrone.fa.md`
```md
---
title: 'N-Ethylhexedrone'
slug: "n-ethylhexedrone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# N-Ethylhexedrone

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\n-ethylhexedrone.md`
```md
---
title: 'N-Ethylhexedrone'
slug: "n-ethylhexedrone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# N-Ethylhexedrone

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\n-ethylpentedrone.fa.md`
```md
---
title: 'N-Ethylpentedrone'
slug: "n-ethylpentedrone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# N-Ethylpentedrone

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\n-ethylpentedrone.md`
```md
---
title: 'N-Ethylpentedrone'
slug: "n-ethylpentedrone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# N-Ethylpentedrone

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\nicotine.fa.md`
```md
---
title: 'Nicotine'
slug: "nicotine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Nicotine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\nicotine.md`
```md
---
title: 'Nicotine'
slug: "nicotine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Nicotine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\nm-2-ai.fa.md`
```md
---
title: 'NM-2-AI'
slug: "nm-2-ai"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# NM-2-AI

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\nm-2-ai.md`
```md
---
title: 'NM-2-AI'
slug: "nm-2-ai"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# NM-2-AI

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\pentedrone.fa.md`
```md
---
title: 'Pentedrone'
slug: "pentedrone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Pentedrone

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\pentedrone.md`
```md
---
title: 'Pentedrone'
slug: "pentedrone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Pentedrone

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\phenidates.fa.md`
```md
---
title: 'Phenidates'
slug: "phenidates"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Phenidates

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\phenidates.md`
```md
---
title: 'Phenidates'
slug: "phenidates"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Phenidates

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\phenmetrazines.fa.md`
```md
---
title: 'Phenmetrazines'
slug: "phenmetrazines"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Phenmetrazines

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\phenmetrazines.md`
```md
---
title: 'Phenmetrazines'
slug: "phenmetrazines"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Phenmetrazines

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\php.fa.md`
```md
---
title: 'α-PHP'
slug: "php"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# α-PHP

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\php.md`
```md
---
title: 'α-PHP'
slug: "php"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# α-PHP

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\piperazines.fa.md`
```md
---
title: 'Piperazines'
slug: "piperazines"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Piperazines

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\piperazines.md`
```md
---
title: 'Piperazines'
slug: "piperazines"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Piperazines

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\prolintane.fa.md`
```md
---
title: 'Prolintane'
slug: "prolintane"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Prolintane

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\prolintane.md`
```md
---
title: 'Prolintane'
slug: "prolintane"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Prolintane

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\propylhexedrine.fa.md`
```md
---
title: 'Propylhexedrine'
slug: "propylhexedrine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Propylhexedrine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\propylhexedrine.md`
```md
---
title: 'Propylhexedrine'
slug: "propylhexedrine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Propylhexedrine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\pvp.fa.md`
```md
---
title: 'α-PVP'
slug: "pvp"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# α-PVP

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\pvp.md`
```md
---
title: 'α-PVP'
slug: "pvp"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# α-PVP

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\pyrrolidinophenones.fa.md`
```md
---
title: 'Pyrrolidinophenones'
slug: "pyrrolidinophenones"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Pyrrolidinophenones

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\pyrrolidinophenones.md`
```md
---
title: 'Pyrrolidinophenones'
slug: "pyrrolidinophenones"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Pyrrolidinophenones

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\rti-111.fa.md`
```md
---
title: 'RTI-111'
slug: "rti-111"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# RTI-111

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\rti-111.md`
```md
---
title: 'RTI-111'
slug: "rti-111"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# RTI-111

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\stimulants.fa.md`
```md
---
title: 'Stimulants'
slug: "stimulants"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Stimulants

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\stimulants.md`
```md
---
title: 'Stimulants'
slug: "stimulants"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Stimulants

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\theacrine.fa.md`
```md
---
title: 'Theacrine'
slug: "theacrine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Theacrine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\theacrine.md`
```md
---
title: 'Theacrine'
slug: "theacrine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Theacrine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\tropanes.fa.md`
```md
---
title: 'Tropanes'
slug: "tropanes"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Tropanes

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\tropanes.md`
```md
---
title: 'Tropanes'
slug: "tropanes"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Tropanes

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\xanthines.fa.md`
```md
---
title: 'Xanthines'
slug: "xanthines"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Xanthines

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\xanthines.md`
```md
---
title: 'Xanthines'
slug: "xanthines"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Xanthines

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\5-htp.fa.md`
```md
---
title: '5-HTP'
slug: "5-htp"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# 5-HTP

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\5-htp.md`
```md
---
title: '5-HTP'
slug: "5-htp"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# 5-HTP

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\adrafinil.fa.md`
```md
---
title: 'Adrafinil'
slug: "adrafinil"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Adrafinil

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\adrafinil.md`
```md
---
title: 'Adrafinil'
slug: "adrafinil"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Adrafinil

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\alpha-gpc.fa.md`
```md
---
title: 'Alpha-GPC'
slug: "alpha-gpc"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Alpha-GPC

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\alpha-gpc.md`
```md
---
title: 'Alpha-GPC'
slug: "alpha-gpc"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Alpha-GPC

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\aniracetam.fa.md`
```md
---
title: 'Aniracetam'
slug: "aniracetam"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Aniracetam

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\aniracetam.md`
```md
---
title: 'Aniracetam'
slug: "aniracetam"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Aniracetam

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\armodafinil.fa.md`
```md
---
title: 'Armodafinil'
slug: "armodafinil"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Armodafinil

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\armodafinil.md`
```md
---
title: 'Armodafinil'
slug: "armodafinil"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Armodafinil

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\bromantane.fa.md`
```md
---
title: 'Bromantane'
slug: "bromantane"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Bromantane

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\bromantane.md`
```md
---
title: 'Bromantane'
slug: "bromantane"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Bromantane

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\choline-bitartrate.fa.md`
```md
---
title: 'Choline bitartrate'
slug: "choline-bitartrate"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Choline bitartrate

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\choline-bitartrate.md`
```md
---
title: 'Choline bitartrate'
slug: "choline-bitartrate"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Choline bitartrate

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\choline.fa.md`
```md
---
title: 'Choline'
slug: "choline"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Choline

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\choline.md`
```md
---
title: 'Choline'
slug: "choline"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Choline

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\citicoline.fa.md`
```md
---
title: 'Citicoline'
slug: "citicoline"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Citicoline

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\citicoline.md`
```md
---
title: 'Citicoline'
slug: "citicoline"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Citicoline

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\coluracetam.fa.md`
```md
---
title: 'Coluracetam'
slug: "coluracetam"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Coluracetam

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\coluracetam.md`
```md
---
title: 'Coluracetam'
slug: "coluracetam"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Coluracetam

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\creatine.fa.md`
```md
---
title: 'Creatine'
slug: "creatine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Creatine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\creatine.md`
```md
---
title: 'Creatine'
slug: "creatine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Creatine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\dietary-supplements.fa.md`
```md
---
title: 'Dietary supplements'
slug: "dietary-supplements"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Dietary supplements

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\dietary-supplements.md`
```md
---
title: 'Dietary supplements'
slug: "dietary-supplements"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Dietary supplements

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\eugeroics.fa.md`
```md
---
title: 'Eugeroics'
slug: "eugeroics"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Eugeroics

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\eugeroics.md`
```md
---
title: 'Eugeroics'
slug: "eugeroics"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Eugeroics

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\gaba.fa.md`
```md
---
title: 'GABA'
slug: "gaba"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# GABA

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\gaba.md`
```md
---
title: 'GABA'
slug: "gaba"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# GABA

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\l-theanine.fa.md`
```md
---
title: 'L-Theanine'
slug: "l-theanine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# L-Theanine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\l-theanine.md`
```md
---
title: 'L-Theanine'
slug: "l-theanine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# L-Theanine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\l-tyrosine.fa.md`
```md
---
title: 'L-Tyrosine'
slug: "l-tyrosine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# L-Tyrosine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\l-tyrosine.md`
```md
---
title: 'L-Tyrosine'
slug: "l-tyrosine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# L-Tyrosine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\meclofenoxate.fa.md`
```md
---
title: 'Meclofenoxate'
slug: "meclofenoxate"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Meclofenoxate

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\meclofenoxate.md`
```md
---
title: 'Meclofenoxate'
slug: "meclofenoxate"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Meclofenoxate

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\memantine.fa.md`
```md
---
title: 'Memantine'
slug: "memantine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Memantine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\memantine.md`
```md
---
title: 'Memantine'
slug: "memantine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Memantine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\modafinil.fa.md`
```md
---
title: 'Modafinil'
slug: "modafinil"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Modafinil

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\modafinil.md`
```md
---
title: 'Modafinil'
slug: "modafinil"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Modafinil

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\n-acetylcysteine.fa.md`
```md
---
title: 'N-Acetylcysteine'
slug: "n-acetylcysteine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# N-Acetylcysteine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\n-acetylcysteine.md`
```md
---
title: 'N-Acetylcysteine'
slug: "n-acetylcysteine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# N-Acetylcysteine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\n-methylbisfluoromodafinil.fa.md`
```md
---
title: 'N-Methylbisfluoromodafinil'
slug: "n-methylbisfluoromodafinil"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# N-Methylbisfluoromodafinil

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\n-methylbisfluoromodafinil.md`
```md
---
title: 'N-Methylbisfluoromodafinil'
slug: "n-methylbisfluoromodafinil"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# N-Methylbisfluoromodafinil

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\noopept.fa.md`
```md
---
title: 'Noopept'
slug: "noopept"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Noopept

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\noopept.md`
```md
---
title: 'Noopept'
slug: "noopept"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Noopept

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\nootropics.fa.md`
```md
---
title: 'Nootropics'
slug: "nootropics"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Nootropics

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\nootropics.md`
```md
---
title: 'Nootropics'
slug: "nootropics"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Nootropics

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\others.fa.md`
```md
---
title: 'Others'
slug: "others"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Others

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\others.md`
```md
---
title: 'Others'
slug: "others"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Others

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\oxiracetam.fa.md`
```md
---
title: 'Oxiracetam'
slug: "oxiracetam"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Oxiracetam

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\oxiracetam.md`
```md
---
title: 'Oxiracetam'
slug: "oxiracetam"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Oxiracetam

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\phenylpiracetam.fa.md`
```md
---
title: 'Phenylpiracetam'
slug: "phenylpiracetam"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Phenylpiracetam

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\phenylpiracetam.md`
```md
---
title: 'Phenylpiracetam'
slug: "phenylpiracetam"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Phenylpiracetam

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\piracetam.fa.md`
```md
---
title: 'Piracetam'
slug: "piracetam"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Piracetam

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\piracetam.md`
```md
---
title: 'Piracetam'
slug: "piracetam"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Piracetam

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\pramiracetam.fa.md`
```md
---
title: 'Pramiracetam'
slug: "pramiracetam"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Pramiracetam

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\pramiracetam.md`
```md
---
title: 'Pramiracetam'
slug: "pramiracetam"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Pramiracetam

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\racetams.fa.md`
```md
---
title: 'Racetams'
slug: "racetams"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Racetams

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\racetams.md`
```md
---
title: 'Racetams'
slug: "racetams"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Racetams

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\s-adenosyl-methionine.fa.md`
```md
---
title: 'S-Adenosyl methionine'
slug: "s-adenosyl-methionine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# S-Adenosyl methionine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\s-adenosyl-methionine.md`
```md
---
title: 'S-Adenosyl methionine'
slug: "s-adenosyl-methionine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# S-Adenosyl methionine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\tianeptine.fa.md`
```md
---
title: 'Tianeptine'
slug: "tianeptine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Tianeptine

_Page coming soon._

```

---
### `wiki\Psychoactives\Stimulants\Nootropics\tianeptine.md`
```md
---
title: 'Tianeptine'
slug: "tianeptine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Tianeptine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\5f-akb48.fa.md`
```md
---
title: '5F-AKB48'
slug: "5f-akb48"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# 5F-AKB48

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\5f-akb48.md`
```md
---
title: '5F-AKB48'
slug: "5f-akb48"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# 5F-AKB48

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\5f-pb-22.fa.md`
```md
---
title: '5F-PB-22'
slug: "5f-pb-22"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# 5F-PB-22

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\5f-pb-22.md`
```md
---
title: '5F-PB-22'
slug: "5f-pb-22"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# 5F-PB-22

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\ab-fubinaca.fa.md`
```md
---
title: 'AB-FUBINACA'
slug: "ab-fubinaca"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# AB-FUBINACA

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\ab-fubinaca.md`
```md
---
title: 'AB-FUBINACA'
slug: "ab-fubinaca"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# AB-FUBINACA

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\apica.fa.md`
```md
---
title: 'APICA'
slug: "apica"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# APICA

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\apica.md`
```md
---
title: 'APICA'
slug: "apica"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# APICA

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\cannabinoids.fa.md`
```md
---
title: 'Cannabinoids'
slug: "cannabinoids"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# Cannabinoids

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\cannabinoids.md`
```md
---
title: 'Cannabinoids'
slug: "cannabinoids"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# Cannabinoids

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\cbd.fa.md`
```md
---
title: 'CBD'
slug: "cbd"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# CBD

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\cbd.md`
```md
---
title: 'CBD'
slug: "cbd"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# CBD

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\cbda.fa.md`
```md
---
title: 'CBDA'
slug: "cbda"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# CBDA

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\cbda.md`
```md
---
title: 'CBDA'
slug: "cbda"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# CBDA

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\cbdh.fa.md`
```md
---
title: 'CBDH'
slug: "cbdh"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# CBDH

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\cbdh.md`
```md
---
title: 'CBDH'
slug: "cbdh"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# CBDH

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\cbdp.fa.md`
```md
---
title: 'CBDP'
slug: "cbdp"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# CBDP

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\cbdp.md`
```md
---
title: 'CBDP'
slug: "cbdp"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# CBDP

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\delta-10-thc.fa.md`
```md
---
title: 'delta-10-THC'
slug: "delta-10-thc"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# delta-10-THC

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\delta-10-thc.md`
```md
---
title: 'delta-10-THC'
slug: "delta-10-thc"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# delta-10-THC

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\delta-11-thc.fa.md`
```md
---
title: 'delta-11-THC'
slug: "delta-11-thc"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# delta-11-THC

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\delta-11-thc.md`
```md
---
title: 'delta-11-THC'
slug: "delta-11-thc"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# delta-11-THC

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\delta-8-thc.fa.md`
```md
---
title: 'delta-8-THC'
slug: "delta-8-thc"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# delta-8-THC

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\delta-8-thc.md`
```md
---
title: 'delta-8-THC'
slug: "delta-8-thc"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# delta-8-THC

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\hhc.fa.md`
```md
---
title: 'HHC'
slug: "hhc"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# HHC

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\hhc.md`
```md
---
title: 'HHC'
slug: "hhc"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# HHC

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\jwh-018.fa.md`
```md
---
title: 'JWH-018'
slug: "jwh-018"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# JWH-018

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\jwh-018.md`
```md
---
title: 'JWH-018'
slug: "jwh-018"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# JWH-018

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\jwh-073.fa.md`
```md
---
title: 'JWH-073'
slug: "jwh-073"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# JWH-073

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\jwh-073.md`
```md
---
title: 'JWH-073'
slug: "jwh-073"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# JWH-073

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\phytocannabinoids.fa.md`
```md
---
title: 'Phytocannabinoids'
slug: "phytocannabinoids"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# Phytocannabinoids

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\phytocannabinoids.md`
```md
---
title: 'Phytocannabinoids'
slug: "phytocannabinoids"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# Phytocannabinoids

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\semi-synthetic-phytocannabinoids.fa.md`
```md
---
title: 'Semi-synthetic phytocannabinoids'
slug: "semi-synthetic-phytocannabinoids"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# Semi-synthetic phytocannabinoids

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\semi-synthetic-phytocannabinoids.md`
```md
---
title: 'Semi-synthetic phytocannabinoids'
slug: "semi-synthetic-phytocannabinoids"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# Semi-synthetic phytocannabinoids

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\sts-135.fa.md`
```md
---
title: 'STS-135'
slug: "sts-135"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# STS-135

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\sts-135.md`
```md
---
title: 'STS-135'
slug: "sts-135"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# STS-135

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\synthetic-cannabinoids.fa.md`
```md
---
title: 'Synthetic cannabinoids'
slug: "synthetic-cannabinoids"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# Synthetic cannabinoids

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\synthetic-cannabinoids.md`
```md
---
title: 'Synthetic cannabinoids'
slug: "synthetic-cannabinoids"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# Synthetic cannabinoids

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\thc-o-acetate.fa.md`
```md
---
title: 'THC-O-acetate'
slug: "thc-o-acetate"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THC-O-acetate

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\thc-o-acetate.md`
```md
---
title: 'THC-O-acetate'
slug: "thc-o-acetate"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THC-O-acetate

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\thc.fa.md`
```md
---
title: 'THC'
slug: "thc"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THC

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\thc.md`
```md
---
title: 'THC'
slug: "thc"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THC

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\thca.fa.md`
```md
---
title: 'THCA'
slug: "thca"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THCA

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\thca.md`
```md
---
title: 'THCA'
slug: "thca"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THCA

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\thcb.fa.md`
```md
---
title: 'THCB'
slug: "thcb"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THCB

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\thcb.md`
```md
---
title: 'THCB'
slug: "thcb"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THCB

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\thch.fa.md`
```md
---
title: 'THCH'
slug: "thch"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THCH

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\thch.md`
```md
---
title: 'THCH'
slug: "thch"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THCH

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\thcp.fa.md`
```md
---
title: 'THCP'
slug: "thcp"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THCP

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\thcp.md`
```md
---
title: 'THCP'
slug: "thcp"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THCP

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\thj-018.fa.md`
```md
---
title: 'THJ-018'
slug: "thj-018"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THJ-018

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\thj-018.md`
```md
---
title: 'THJ-018'
slug: "thj-018"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THJ-018

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\thj-2201.fa.md`
```md
---
title: 'THJ-2201'
slug: "thj-2201"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THJ-2201

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Cannabinoids\thj-2201.md`
```md
---
title: 'THJ-2201'
slug: "thj-2201"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THJ-2201

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Deliriants\antihistamines.fa.md`
```md
---
title: 'Antihistamines'
slug: "antihistamines"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Antihistamines

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Deliriants\antihistamines.md`
```md
---
title: 'Antihistamines'
slug: "antihistamines"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Antihistamines

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Deliriants\atropine.fa.md`
```md
---
title: 'Atropine'
slug: "atropine"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Atropine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Deliriants\atropine.md`
```md
---
title: 'Atropine'
slug: "atropine"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Atropine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Deliriants\benzydamine.fa.md`
```md
---
title: 'Benzydamine'
slug: "benzydamine"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Benzydamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Deliriants\benzydamine.md`
```md
---
title: 'Benzydamine'
slug: "benzydamine"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Benzydamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Deliriants\deliriants.fa.md`
```md
---
title: 'Deliriants'
slug: "deliriants"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Deliriants

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Deliriants\deliriants.md`
```md
---
title: 'Deliriants'
slug: "deliriants"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Deliriants

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Deliriants\elemicin.fa.md`
```md
---
title: 'Elemicin'
slug: "elemicin"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Elemicin

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Deliriants\elemicin.md`
```md
---
title: 'Elemicin'
slug: "elemicin"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Elemicin

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Deliriants\hyoscyamine.fa.md`
```md
---
title: 'Hyoscyamine'
slug: "hyoscyamine"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Hyoscyamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Deliriants\hyoscyamine.md`
```md
---
title: 'Hyoscyamine'
slug: "hyoscyamine"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Hyoscyamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Deliriants\myristicin.fa.md`
```md
---
title: 'Myristicin'
slug: "myristicin"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Myristicin

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Deliriants\myristicin.md`
```md
---
title: 'Myristicin'
slug: "myristicin"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Myristicin

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Deliriants\promethazine.fa.md`
```md
---
title: 'Promethazine'
slug: "promethazine"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Promethazine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Deliriants\promethazine.md`
```md
---
title: 'Promethazine'
slug: "promethazine"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Promethazine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Deliriants\scopolamine.fa.md`
```md
---
title: 'Scopolamine'
slug: "scopolamine"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Scopolamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Deliriants\scopolamine.md`
```md
---
title: 'Scopolamine'
slug: "scopolamine"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Scopolamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Deliriants\tropane-alkaloids.fa.md`
```md
---
title: 'Tropane alkaloids'
slug: "tropane-alkaloids"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Tropane alkaloids

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Deliriants\tropane-alkaloids.md`
```md
---
title: 'Tropane alkaloids'
slug: "tropane-alkaloids"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Tropane alkaloids

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\2-fluorodeschloroketamine.fa.md`
```md
---
title: '2-Fluorodeschloroketamine'
slug: "2-fluorodeschloroketamine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 2-Fluorodeschloroketamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\2-fluorodeschloroketamine.md`
```md
---
title: '2-Fluorodeschloroketamine'
slug: "2-fluorodeschloroketamine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 2-Fluorodeschloroketamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\2-oxo-pce.fa.md`
```md
---
title: '2''-Oxo-PCE'
slug: "2-oxo-pce"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 2'-Oxo-PCE

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\2-oxo-pce.md`
```md
---
title: '2''-Oxo-PCE'
slug: "2-oxo-pce"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 2'-Oxo-PCE

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\2-oxo-pcm.fa.md`
```md
---
title: '2''-Oxo-PCM'
slug: "2-oxo-pcm"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 2'-Oxo-PCM

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\2-oxo-pcm.md`
```md
---
title: '2''-Oxo-PCM'
slug: "2-oxo-pcm"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 2'-Oxo-PCM

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\3-cl-pcp.fa.md`
```md
---
title: '3-Cl-PCP'
slug: "3-cl-pcp"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 3-Cl-PCP

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\3-cl-pcp.md`
```md
---
title: '3-Cl-PCP'
slug: "3-cl-pcp"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 3-Cl-PCP

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\3-ho-pce.fa.md`
```md
---
title: '3-HO-PCE'
slug: "3-ho-pce"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 3-HO-PCE

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\3-ho-pce.md`
```md
---
title: '3-HO-PCE'
slug: "3-ho-pce"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 3-HO-PCE

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\3-ho-pcp.fa.md`
```md
---
title: '3-HO-PCP'
slug: "3-ho-pcp"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 3-HO-PCP

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\3-ho-pcp.md`
```md
---
title: '3-HO-PCP'
slug: "3-ho-pcp"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 3-HO-PCP

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\3-meo-pce.fa.md`
```md
---
title: '3-MeO-PCE'
slug: "3-meo-pce"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 3-MeO-PCE

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\3-meo-pce.md`
```md
---
title: '3-MeO-PCE'
slug: "3-meo-pce"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 3-MeO-PCE

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\3-meo-pcmo.fa.md`
```md
---
title: '3-MeO-PCMo'
slug: "3-meo-pcmo"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 3-MeO-PCMo

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\3-meo-pcmo.md`
```md
---
title: '3-MeO-PCMo'
slug: "3-meo-pcmo"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 3-MeO-PCMo

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\3-meo-pcp.fa.md`
```md
---
title: '3-MeO-PCP'
slug: "3-meo-pcp"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 3-MeO-PCP

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\3-meo-pcp.md`
```md
---
title: '3-MeO-PCP'
slug: "3-meo-pcp"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 3-MeO-PCP

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\4-meo-pcp.fa.md`
```md
---
title: '4-MeO-PCP'
slug: "4-meo-pcp"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 4-MeO-PCP

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\4-meo-pcp.md`
```md
---
title: '4-MeO-PCP'
slug: "4-meo-pcp"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 4-MeO-PCP

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\adamantanes.fa.md`
```md
---
title: 'Adamantanes'
slug: "adamantanes"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Adamantanes

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\adamantanes.md`
```md
---
title: 'Adamantanes'
slug: "adamantanes"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Adamantanes

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\arylcyclohexylamines.fa.md`
```md
---
title: 'Arylcyclohexylamines'
slug: "arylcyclohexylamines"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Arylcyclohexylamines

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\arylcyclohexylamines.md`
```md
---
title: 'Arylcyclohexylamines'
slug: "arylcyclohexylamines"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Arylcyclohexylamines

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\dextromethorphan.fa.md`
```md
---
title: 'Dextromethorphan'
slug: "dextromethorphan"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Dextromethorphan

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\dextromethorphan.md`
```md
---
title: 'Dextromethorphan'
slug: "dextromethorphan"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Dextromethorphan

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\dextrorphan.fa.md`
```md
---
title: 'Dextrorphan'
slug: "dextrorphan"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Dextrorphan

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\dextrorphan.md`
```md
---
title: 'Dextrorphan'
slug: "dextrorphan"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Dextrorphan

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\diarylethylamines.fa.md`
```md
---
title: 'Diarylethylamines'
slug: "diarylethylamines"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Diarylethylamines

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\diarylethylamines.md`
```md
---
title: 'Diarylethylamines'
slug: "diarylethylamines"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Diarylethylamines

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\diphenidine.fa.md`
```md
---
title: 'Diphenidine'
slug: "diphenidine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Diphenidine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\diphenidine.md`
```md
---
title: 'Diphenidine'
slug: "diphenidine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Diphenidine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\dissociatives.fa.md`
```md
---
title: 'Dissociatives'
slug: "dissociatives"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Dissociatives

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\dissociatives.md`
```md
---
title: 'Dissociatives'
slug: "dissociatives"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Dissociatives

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\ephenidine.fa.md`
```md
---
title: 'Ephenidine'
slug: "ephenidine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Ephenidine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\ephenidine.md`
```md
---
title: 'Ephenidine'
slug: "ephenidine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Ephenidine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\eticyclidine.fa.md`
```md
---
title: 'Eticyclidine'
slug: "eticyclidine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Eticyclidine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\eticyclidine.md`
```md
---
title: 'Eticyclidine'
slug: "eticyclidine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Eticyclidine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\hydroxetamine.fa.md`
```md
---
title: 'Hydroxetamine'
slug: "hydroxetamine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Hydroxetamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\hydroxetamine.md`
```md
---
title: 'Hydroxetamine'
slug: "hydroxetamine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Hydroxetamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\ketamine.fa.md`
```md
---
title: 'Ketamine'
slug: "ketamine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Ketamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\ketamine.md`
```md
---
title: 'Ketamine'
slug: "ketamine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Ketamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\methoxetamine.fa.md`
```md
---
title: 'Methoxetamine'
slug: "methoxetamine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Methoxetamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\methoxetamine.md`
```md
---
title: 'Methoxetamine'
slug: "methoxetamine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Methoxetamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\morphinans.fa.md`
```md
---
title: 'Morphinans'
slug: "morphinans"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Morphinans

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\morphinans.md`
```md
---
title: 'Morphinans'
slug: "morphinans"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Morphinans

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\phencyclidine.fa.md`
```md
---
title: 'Phencyclidine'
slug: "phencyclidine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Phencyclidine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\phencyclidine.md`
```md
---
title: 'Phencyclidine'
slug: "phencyclidine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Phencyclidine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\r-ketamine.fa.md`
```md
---
title: 'R-Ketamine'
slug: "r-ketamine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# R-Ketamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\r-ketamine.md`
```md
---
title: 'R-Ketamine'
slug: "r-ketamine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# R-Ketamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\s-ketamine.fa.md`
```md
---
title: 'S-Ketamine'
slug: "s-ketamine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# S-Ketamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Dissociatives\s-ketamine.md`
```md
---
title: 'S-Ketamine'
slug: "s-ketamine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# S-Ketamine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\psychedelics.fa.md`
```md
---
title: 'psychedelics'
slug: "psychedelics"
lang: "en"
category: 'psychedelics'
weight: 1000
template: "wiki"
summary: ''
---
```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\psychedelics.md`
```md
---
title: 'psychedelics'
slug: "psychedelics"
lang: "en"
category: 'psychedelics'
weight: 1000
template: "wiki"
summary: ''
---
```

---
### `wiki\Psychoactives\Hallucinogens\β-Carbolines\harmaline.fa.md`
```md
---
title: 'Harmaline'
slug: "harmaline"
lang: "en"
category: 'β-Carbolines'
weight: 1000
template: "wiki"
summary: ''
---

# Harmaline

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\β-Carbolines\harmaline.md`
```md
---
title: 'Harmaline'
slug: "harmaline"
lang: "en"
category: 'β-Carbolines'
weight: 1000
template: "wiki"
summary: ''
---

# Harmaline

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\β-Carbolines\harmine.fa.md`
```md
---
title: 'Harmine'
slug: "harmine"
lang: "en"
category: 'β-Carbolines'
weight: 1000
template: "wiki"
summary: ''
---

# Harmine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\β-Carbolines\harmine.md`
```md
---
title: 'Harmine'
slug: "harmine"
lang: "en"
category: 'β-Carbolines'
weight: 1000
template: "wiki"
summary: ''
---

# Harmine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\β-Carbolines\tetrahydroharmine.fa.md`
```md
---
title: 'Tetrahydroharmine'
slug: "tetrahydroharmine"
lang: "en"
category: 'β-Carbolines'
weight: 1000
template: "wiki"
summary: ''
---

# Tetrahydroharmine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\β-Carbolines\tetrahydroharmine.md`
```md
---
title: 'Tetrahydroharmine'
slug: "tetrahydroharmine"
lang: "en"
category: 'β-Carbolines'
weight: 1000
template: "wiki"
summary: ''
---

# Tetrahydroharmine

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\β-Carbolines\β-Carbolines.fa.md`
```md
---
title: 'β-Carbolines'
slug: "carbolines"
lang: "en"
category: 'β-Carbolines'
weight: 1000
template: "wiki"
summary: ''
---

# β-Carbolines

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\β-Carbolines\β-Carbolines.md`
```md
---
title: 'β-Carbolines'
slug: "carbolines"
lang: "en"
category: 'β-Carbolines'
weight: 1000
template: "wiki"
summary: ''
---

# β-Carbolines

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-b.fa.md`
```md
---
title: '2C-B'
slug: "2c-b"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-B

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-b.md`
```md
---
title: '2C-B'
slug: "2c-b"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-B

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-c.fa.md`
```md
---
title: '2C-C'
slug: "2c-c"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-C

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-c.md`
```md
---
title: '2C-C'
slug: "2c-c"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-C

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-d.fa.md`
```md
---
title: '2C-D'
slug: "2c-d"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-D

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-d.md`
```md
---
title: '2C-D'
slug: "2c-d"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-D

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-e.fa.md`
```md
---
title: '2C-E'
slug: "2c-e"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-E

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-e.md`
```md
---
title: '2C-E'
slug: "2c-e"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-E

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-h.fa.md`
```md
---
title: '2C-H'
slug: "2c-h"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-H

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-h.md`
```md
---
title: '2C-H'
slug: "2c-h"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-H

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-i.fa.md`
```md
---
title: '2C-I'
slug: "2c-i"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-I

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-i.md`
```md
---
title: '2C-I'
slug: "2c-i"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-I

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-p.fa.md`
```md
---
title: '2C-P'
slug: "2c-p"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-P

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-p.md`
```md
---
title: '2C-P'
slug: "2c-p"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-P

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-t-2.fa.md`
```md
---
title: '2C-T-2'
slug: "2c-t-2"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-T-2

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-t-2.md`
```md
---
title: '2C-T-2'
slug: "2c-t-2"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-T-2

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-t-21.fa.md`
```md
---
title: '2C-T-21'
slug: "2c-t-21"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-T-21

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-t-21.md`
```md
---
title: '2C-T-21'
slug: "2c-t-21"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-T-21

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-t-7.fa.md`
```md
---
title: '2C-T-7'
slug: "2c-t-7"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-T-7

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-t-7.md`
```md
---
title: '2C-T-7'
slug: "2c-t-7"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-T-7

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-t-x.fa.md`
```md
---
title: '2C-T-x'
slug: "2c-t-x"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-T-x

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-t-x.md`
```md
---
title: '2C-T-x'
slug: "2c-t-x"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-T-x

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-t.fa.md`
```md
---
title: '2C-T'
slug: "2c-t"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-T

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-t.md`
```md
---
title: '2C-T'
slug: "2c-t"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-T

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-x.fa.md`
```md
---
title: '2C-x'
slug: "2c-x"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-x

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-x.md`
```md
---
title: '2C-x'
slug: "2c-x"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-x

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-xderivatives.fa.md`
```md
---
title: '2C-xـderivatives'
slug: "2c-xderivatives"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-xـderivatives

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\2C-x\2c-xderivatives.md`
```md
---
title: '2C-xـderivatives'
slug: "2c-xderivatives"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-xـderivatives

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Classical_psychedelics\classical-psychedelics.fa.md`
```md
---
title: 'Classical_psychedelics'
slug: "classical-psychedelics"
lang: "en"
category: 'Classical_psychedelics'
weight: 1000
template: "wiki"
summary: ''
---

# Classical_psychedelics

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Classical_psychedelics\classical-psychedelics.md`
```md
---
title: 'Classical_psychedelics'
slug: "classical-psychedelics"
lang: "en"
category: 'Classical_psychedelics'
weight: 1000
template: "wiki"
summary: ''
---

# Classical_psychedelics

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\DOx\25-dma.fa.md`
```md
---
title: '2,5-DMA'
slug: "25-dma"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# 2,5-DMA

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\DOx\25-dma.md`
```md
---
title: '2,5-DMA'
slug: "25-dma"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# 2,5-DMA

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\DOx\dob.fa.md`
```md
---
title: 'DOB'
slug: "dob"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# DOB

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\DOx\dob.md`
```md
---
title: 'DOB'
slug: "dob"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# DOB

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\DOx\doc.fa.md`
```md
---
title: 'DOC'
slug: "doc"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# DOC

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\DOx\doc.md`
```md
---
title: 'DOC'
slug: "doc"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# DOC

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\DOx\doi.fa.md`
```md
---
title: 'DOI'
slug: "doi"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# DOI

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\DOx\doi.md`
```md
---
title: 'DOI'
slug: "doi"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# DOI

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\DOx\dom.fa.md`
```md
---
title: 'DOM'
slug: "dom"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# DOM

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\DOx\dom.md`
```md
---
title: 'DOM'
slug: "dom"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# DOM

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\DOx\dox.fa.md`
```md
---
title: 'DOx'
slug: "dox"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# DOx

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\DOx\dox.md`
```md
---
title: 'DOx'
slug: "dox"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# DOx

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\DOx\doxderivatives.fa.md`
```md
---
title: 'DOxـderivatives'
slug: "doxderivatives"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# DOxـderivatives

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\DOx\doxderivatives.md`
```md
---
title: 'DOxـderivatives'
slug: "doxderivatives"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# DOxـderivatives

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\5-apb.fa.md`
```md
---
title: '5-APB'
slug: "5-apb"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# 5-APB

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\5-apb.md`
```md
---
title: '5-APB'
slug: "5-apb"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# 5-APB

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\5-mapb.fa.md`
```md
---
title: '5-MAPB'
slug: "5-mapb"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# 5-MAPB

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\5-mapb.md`
```md
---
title: '5-MAPB'
slug: "5-mapb"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# 5-MAPB

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\6-apb.fa.md`
```md
---
title: '6-APB'
slug: "6-apb"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# 6-APB

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\6-apb.md`
```md
---
title: '6-APB'
slug: "6-apb"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# 6-APB

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\6-apdb.fa.md`
```md
---
title: '6-APDB'
slug: "6-apdb"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# 6-APDB

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\6-apdb.md`
```md
---
title: '6-APDB'
slug: "6-apdb"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# 6-APDB

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\benzofurans.fa.md`
```md
---
title: 'Benzofurans'
slug: "benzofurans"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# Benzofurans

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\benzofurans.md`
```md
---
title: 'Benzofurans'
slug: "benzofurans"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# Benzofurans

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\empathogens.fa.md`
```md
---
title: 'Empathogens'
slug: "empathogens"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# Empathogens

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\empathogens.md`
```md
---
title: 'Empathogens'
slug: "empathogens"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# Empathogens

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\mda.fa.md`
```md
---
title: 'MDA'
slug: "mda"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# MDA

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\mda.md`
```md
---
title: 'MDA'
slug: "mda"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# MDA

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\mdai.fa.md`
```md
---
title: 'MDAI'
slug: "mdai"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# MDAI

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\mdai.md`
```md
---
title: 'MDAI'
slug: "mdai"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# MDAI

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\mdea.fa.md`
```md
---
title: 'MDEA'
slug: "mdea"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# MDEA

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\mdea.md`
```md
---
title: 'MDEA'
slug: "mdea"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# MDEA

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\mdma.fa.md`
```md
---
title: 'MDMA'
slug: "mdma"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# MDMA

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\mdma.md`
```md
---
title: 'MDMA'
slug: "mdma"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# MDMA

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\mdxx.fa.md`
```md
---
title: 'MDxx'
slug: "mdxx"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# MDxx

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\mdxx.md`
```md
---
title: 'MDxx'
slug: "mdxx"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# MDxx

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\methylone.fa.md`
```md
---
title: 'Methylone'
slug: "methylone"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# Methylone

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\methylone.md`
```md
---
title: 'Methylone'
slug: "methylone"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# Methylone

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\pma.fa.md`
```md
---
title: 'PMA'
slug: "pma"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# PMA

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\pma.md`
```md
---
title: 'PMA'
slug: "pma"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# PMA

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\pmma.fa.md`
```md
---
title: 'PMMA'
slug: "pmma"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# PMMA

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Empathogens\pmma.md`
```md
---
title: 'PMMA'
slug: "pmma"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# PMMA

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\1b-lsd.fa.md`
```md
---
title: '1B-LSD'
slug: "1b-lsd"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1B-LSD

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\1b-lsd.md`
```md
---
title: '1B-LSD'
slug: "1b-lsd"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1B-LSD

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\1cp-al-lad.fa.md`
```md
---
title: '1cP-AL-LAD'
slug: "1cp-al-lad"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1cP-AL-LAD

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\1cp-al-lad.md`
```md
---
title: '1cP-AL-LAD'
slug: "1cp-al-lad"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1cP-AL-LAD

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\1cp-lsd.fa.md`
```md
---
title: '1cP-LSD'
slug: "1cp-lsd"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1cP-LSD

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\1cp-lsd.md`
```md
---
title: '1cP-LSD'
slug: "1cp-lsd"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1cP-LSD

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\1cp-mipla.fa.md`
```md
---
title: '1cP-MiPLA'
slug: "1cp-mipla"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1cP-MiPLA

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\1cp-mipla.md`
```md
---
title: '1cP-MiPLA'
slug: "1cp-mipla"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1cP-MiPLA

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\1p-eth-lad.fa.md`
```md
---
title: '1P-ETH-LAD'
slug: "1p-eth-lad"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1P-ETH-LAD

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\1p-eth-lad.md`
```md
---
title: '1P-ETH-LAD'
slug: "1p-eth-lad"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1P-ETH-LAD

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\1p-lsd.fa.md`
```md
---
title: '1P-LSD'
slug: "1p-lsd"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1P-LSD

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\1p-lsd.md`
```md
---
title: '1P-LSD'
slug: "1p-lsd"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1P-LSD

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\1v-lsd.fa.md`
```md
---
title: '1V-LSD'
slug: "1v-lsd"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1V-LSD

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\1v-lsd.md`
```md
---
title: '1V-LSD'
slug: "1v-lsd"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1V-LSD

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\al-lad.fa.md`
```md
---
title: 'AL-LAD'
slug: "al-lad"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# AL-LAD

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\al-lad.md`
```md
---
title: 'AL-LAD'
slug: "al-lad"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# AL-LAD

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\ald-52.fa.md`
```md
---
title: 'ALD-52'
slug: "ald-52"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# ALD-52

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\ald-52.md`
```md
---
title: 'ALD-52'
slug: "ald-52"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# ALD-52

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\eth-lad.fa.md`
```md
---
title: 'ETH-LAD'
slug: "eth-lad"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# ETH-LAD

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\eth-lad.md`
```md
---
title: 'ETH-LAD'
slug: "eth-lad"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# ETH-LAD

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\lae-32.fa.md`
```md
---
title: 'LAE-32'
slug: "lae-32"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# LAE-32

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\lae-32.md`
```md
---
title: 'LAE-32'
slug: "lae-32"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# LAE-32

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\lsa.fa.md`
```md
---
title: 'LSA'
slug: "lsa"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# LSA

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\lsa.md`
```md
---
title: 'LSA'
slug: "lsa"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# LSA

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\lsd.fa.md`
```md
---
title: 'LSD'
slug: "lsd"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# LSD

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\lsd.md`
```md
---
title: 'LSD'
slug: "lsd"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# LSD

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\lsh.fa.md`
```md
---
title: 'LSH'
slug: "lsh"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# LSH

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\lsh.md`
```md
---
title: 'LSH'
slug: "lsh"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# LSH

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\lsm-775.fa.md`
```md
---
title: 'LSM-775'
slug: "lsm-775"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# LSM-775

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\lsm-775.md`
```md
---
title: 'LSM-775'
slug: "lsm-775"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# LSM-775

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\lsz.fa.md`
```md
---
title: 'LSZ'
slug: "lsz"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# LSZ

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\lsz.md`
```md
---
title: 'LSZ'
slug: "lsz"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# LSZ

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\lysergamides.fa.md`
```md
---
title: 'Lysergamides'
slug: "lysergamides"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# Lysergamides

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\lysergamides.md`
```md
---
title: 'Lysergamides'
slug: "lysergamides"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# Lysergamides

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\mipla.fa.md`
```md
---
title: 'MiPLA'
slug: "mipla"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# MiPLA

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\mipla.md`
```md
---
title: 'MiPLA'
slug: "mipla"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# MiPLA

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\pargy-lad.fa.md`
```md
---
title: 'PARGY-LAD'
slug: "pargy-lad"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# PARGY-LAD

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\pargy-lad.md`
```md
---
title: 'PARGY-LAD'
slug: "pargy-lad"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# PARGY-LAD

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\pro-lad.fa.md`
```md
---
title: 'PRO-LAD'
slug: "pro-lad"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# PRO-LAD

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Lysergamides\pro-lad.md`
```md
---
title: 'PRO-LAD'
slug: "pro-lad"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# PRO-LAD

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Mescaline_homologues\3c-e.fa.md`
```md
---
title: '3C-E'
slug: "3c-e"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# 3C-E

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Mescaline_homologues\3c-e.md`
```md
---
title: '3C-E'
slug: "3c-e"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# 3C-E

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Mescaline_homologues\3c-p.fa.md`
```md
---
title: '3C-P'
slug: "3c-p"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# 3C-P

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Mescaline_homologues\3c-p.md`
```md
---
title: '3C-P'
slug: "3c-p"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# 3C-P

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Mescaline_homologues\allylescaline.fa.md`
```md
---
title: 'Allylescaline'
slug: "allylescaline"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# Allylescaline

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Mescaline_homologues\allylescaline.md`
```md
---
title: 'Allylescaline'
slug: "allylescaline"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# Allylescaline

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Mescaline_homologues\escaline.fa.md`
```md
---
title: 'Escaline'
slug: "escaline"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# Escaline

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Mescaline_homologues\escaline.md`
```md
---
title: 'Escaline'
slug: "escaline"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# Escaline

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Mescaline_homologues\mescaline-homologues.fa.md`
```md
---
title: 'Mescaline_homologues'
slug: "mescaline-homologues"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# Mescaline_homologues

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Mescaline_homologues\mescaline-homologues.md`
```md
---
title: 'Mescaline_homologues'
slug: "mescaline-homologues"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# Mescaline_homologues

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Mescaline_homologues\mescaline.fa.md`
```md
---
title: 'Mescaline'
slug: "mescaline"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# Mescaline

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Mescaline_homologues\mescaline.md`
```md
---
title: 'Mescaline'
slug: "mescaline"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# Mescaline

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Mescaline_homologues\methallylescaline.fa.md`
```md
---
title: 'Methallylescaline'
slug: "methallylescaline"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# Methallylescaline

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Mescaline_homologues\methallylescaline.md`
```md
---
title: 'Methallylescaline'
slug: "methallylescaline"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# Methallylescaline

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Mescaline_homologues\proscaline.fa.md`
```md
---
title: 'Proscaline'
slug: "proscaline"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# Proscaline

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Mescaline_homologues\proscaline.md`
```md
---
title: 'Proscaline'
slug: "proscaline"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# Proscaline

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Miscellaneousـphenethylamines\2c-b-fly.fa.md`
```md
---
title: '2C-B-FLY'
slug: "2c-b-fly"
lang: "en"
category: 'Miscellaneousـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-B-FLY

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Miscellaneousـphenethylamines\2c-b-fly.md`
```md
---
title: '2C-B-FLY'
slug: "2c-b-fly"
lang: "en"
category: 'Miscellaneousـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-B-FLY

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Miscellaneousـphenethylamines\bromo-dragonfly.fa.md`
```md
---
title: 'Bromo-DragonFLY'
slug: "bromo-dragonfly"
lang: "en"
category: 'Miscellaneousـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# Bromo-DragonFLY

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Miscellaneousـphenethylamines\bromo-dragonfly.md`
```md
---
title: 'Bromo-DragonFLY'
slug: "bromo-dragonfly"
lang: "en"
category: 'Miscellaneousـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# Bromo-DragonFLY

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Miscellaneousـphenethylamines\k-2c-b.fa.md`
```md
---
title: 'βk-2C-B'
slug: "k-2c-b"
lang: "en"
category: 'Miscellaneousـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# βk-2C-B

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Miscellaneousـphenethylamines\k-2c-b.md`
```md
---
title: 'βk-2C-B'
slug: "k-2c-b"
lang: "en"
category: 'Miscellaneousـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# βk-2C-B

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Miscellaneousـphenethylamines\miscellaneousphenethylamines.fa.md`
```md
---
title: 'Miscellaneousـphenethylamines'
slug: "miscellaneousphenethylamines"
lang: "en"
category: 'Miscellaneousـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# Miscellaneousـphenethylamines

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Miscellaneousـphenethylamines\miscellaneousphenethylamines.md`
```md
---
title: 'Miscellaneousـphenethylamines'
slug: "miscellaneousphenethylamines"
lang: "en"
category: 'Miscellaneousـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# Miscellaneousـphenethylamines

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Miscellaneousـphenethylamines\tma-2.fa.md`
```md
---
title: 'TMA-2'
slug: "tma-2"
lang: "en"
category: 'Miscellaneousـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# TMA-2

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Miscellaneousـphenethylamines\tma-2.md`
```md
---
title: 'TMA-2'
slug: "tma-2"
lang: "en"
category: 'Miscellaneousـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# TMA-2

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Miscellaneousـphenethylamines\tma-6.fa.md`
```md
---
title: 'TMA-6'
slug: "tma-6"
lang: "en"
category: 'Miscellaneousـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# TMA-6

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Miscellaneousـphenethylamines\tma-6.md`
```md
---
title: 'TMA-6'
slug: "tma-6"
lang: "en"
category: 'Miscellaneousـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# TMA-6

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\N-Benzylـphenethylamines\25b-nboh.fa.md`
```md
---
title: '25B-NBOH'
slug: "25b-nboh"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25B-NBOH

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\N-Benzylـphenethylamines\25b-nboh.md`
```md
---
title: '25B-NBOH'
slug: "25b-nboh"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25B-NBOH

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\N-Benzylـphenethylamines\25b-nbome.fa.md`
```md
---
title: '25B-NBOMe'
slug: "25b-nbome"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25B-NBOMe

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\N-Benzylـphenethylamines\25b-nbome.md`
```md
---
title: '25B-NBOMe'
slug: "25b-nbome"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25B-NBOMe

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\N-Benzylـphenethylamines\25c-nboh.fa.md`
```md
---
title: '25C-NBOH'
slug: "25c-nboh"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25C-NBOH

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\N-Benzylـphenethylamines\25c-nboh.md`
```md
---
title: '25C-NBOH'
slug: "25c-nboh"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25C-NBOH

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\N-Benzylـphenethylamines\25c-nbome.fa.md`
```md
---
title: '25C-NBOMe'
slug: "25c-nbome"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25C-NBOMe

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\N-Benzylـphenethylamines\25c-nbome.md`
```md
---
title: '25C-NBOMe'
slug: "25c-nbome"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25C-NBOMe

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\N-Benzylـphenethylamines\25d-nbome.fa.md`
```md
---
title: '25D-NBOMe'
slug: "25d-nbome"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25D-NBOMe

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\N-Benzylـphenethylamines\25d-nbome.md`
```md
---
title: '25D-NBOMe'
slug: "25d-nbome"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25D-NBOMe

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\N-Benzylـphenethylamines\25e-nboh.fa.md`
```md
---
title: '25E-NBOH'
slug: "25e-nboh"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25E-NBOH

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\N-Benzylـphenethylamines\25e-nboh.md`
```md
---
title: '25E-NBOH'
slug: "25e-nboh"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25E-NBOH

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\N-Benzylـphenethylamines\25i-nboh.fa.md`
```md
---
title: '25I-NBOH'
slug: "25i-nboh"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25I-NBOH

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\N-Benzylـphenethylamines\25i-nboh.md`
```md
---
title: '25I-NBOH'
slug: "25i-nboh"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25I-NBOH

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\N-Benzylـphenethylamines\25i-nbome.fa.md`
```md
---
title: '25I-NBOMe'
slug: "25i-nbome"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25I-NBOMe

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\N-Benzylـphenethylamines\25i-nbome.md`
```md
---
title: '25I-NBOMe'
slug: "25i-nbome"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25I-NBOMe

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\N-Benzylـphenethylamines\25n-nbome.fa.md`
```md
---
title: '25N-NBOMe'
slug: "25n-nbome"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25N-NBOMe

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\N-Benzylـphenethylamines\25n-nbome.md`
```md
---
title: '25N-NBOMe'
slug: "25n-nbome"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25N-NBOMe

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\N-Benzylـphenethylamines\n-benzylphenethylamines.fa.md`
```md
---
title: 'N-Benzylـphenethylamines'
slug: "n-benzylphenethylamines"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# N-Benzylـphenethylamines

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\N-Benzylـphenethylamines\n-benzylphenethylamines.md`
```md
---
title: 'N-Benzylـphenethylamines'
slug: "n-benzylphenethylamines"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# N-Benzylـphenethylamines

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Others\5-meo-dibf.fa.md`
```md
---
title: '5-MeO-DiBF'
slug: "5-meo-dibf"
lang: "en"
category: 'Others'
weight: 1000
template: "wiki"
summary: ''
---

# 5-MeO-DiBF

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Others\5-meo-dibf.md`
```md
---
title: '5-MeO-DiBF'
slug: "5-meo-dibf"
lang: "en"
category: 'Others'
weight: 1000
template: "wiki"
summary: ''
---

# 5-MeO-DiBF

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Others\efavirenz.fa.md`
```md
---
title: 'Efavirenz'
slug: "efavirenz"
lang: "en"
category: 'Others'
weight: 1000
template: "wiki"
summary: ''
---

# Efavirenz

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Others\efavirenz.md`
```md
---
title: 'Efavirenz'
slug: "efavirenz"
lang: "en"
category: 'Others'
weight: 1000
template: "wiki"
summary: ''
---

# Efavirenz

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\tryptamines.fa.md`
```md
---
title: 'Tryptamines'
slug: "tryptamines"
lang: "en"
category: "Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# Tryptamines

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\tryptamines.md`
```md
---
title: 'Tryptamines'
slug: "tryptamines"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# Tryptamines

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Base Tryptamines\amt.fa.md`
```md
---
title: 'aMT'
slug: "amt"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# aMT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Base Tryptamines\amt.md`
```md
---
title: 'aMT'
slug: "amt"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# aMT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Base Tryptamines\base-tryptamines.fa.md`
```md
---
title: 'Substituted tryptamines'
slug: "substituted-tryptamines"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# Substituted tryptamines

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Base Tryptamines\base-tryptamines.md`
```md
---
title: 'Substituted tryptamines'
slug: "substituted-tryptamines"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# Substituted tryptamines

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Base Tryptamines\det.fa.md`
```md
---
title: 'DET'
slug: "det"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# DET

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Base Tryptamines\det.md`
```md
---
title: 'DET'
slug: "det"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# DET

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Base Tryptamines\dipt.fa.md`
```md
---
title: 'DiPT'
slug: "dipt"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# DiPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Base Tryptamines\dipt.md`
```md
---
title: 'DiPT'
slug: "dipt"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# DiPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Base Tryptamines\dmt.fa.md`
```md
---
title: 'DMT'
slug: "dmt"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# DMT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Base Tryptamines\dmt.md`
```md
---
title: 'DMT'
slug: "dmt"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# DMT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Base Tryptamines\dpt.fa.md`
```md
---
title: 'DPT'
slug: "dpt"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# DPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Base Tryptamines\dpt.md`
```md
---
title: 'DPT'
slug: "dpt"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# DPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Base Tryptamines\ept.fa.md`
```md
---
title: 'EPT'
slug: "ept"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# EPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Base Tryptamines\ept.md`
```md
---
title: 'EPT'
slug: "ept"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# EPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Base Tryptamines\met.fa.md`
```md
---
title: 'MET'
slug: "met"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# MET

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Base Tryptamines\met.md`
```md
---
title: 'MET'
slug: "met"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# MET

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Base Tryptamines\mipt.fa.md`
```md
---
title: 'MiPT'
slug: "mipt"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# MiPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Base Tryptamines\mipt.md`
```md
---
title: 'MiPT'
slug: "mipt"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# MiPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Base Tryptamines\mpt.fa.md`
```md
---
title: 'MPT'
slug: "mpt"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# MPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Base Tryptamines\mpt.md`
```md
---
title: 'MPT'
slug: "mpt"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# MPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\4-aco-det.fa.md`
```md
---
title: '4-AcO-DET'
slug: "4-aco-det"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-AcO-DET

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\4-aco-det.md`
```md
---
title: '4-AcO-DET'
slug: "4-aco-det"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-AcO-DET

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\4-aco-dipt.fa.md`
```md
---
title: '4-AcO-DiPT'
slug: "4-aco-dipt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-AcO-DiPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\4-aco-dipt.md`
```md
---
title: '4-AcO-DiPT'
slug: "4-aco-dipt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-AcO-DiPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\4-aco-dmt.fa.md`
```md
---
title: '4-AcO-DMT'
slug: "4-aco-dmt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-AcO-DMT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\4-aco-dmt.md`
```md
---
title: '4-AcO-DMT'
slug: "4-aco-dmt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-AcO-DMT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\4-aco-met.fa.md`
```md
---
title: '4-AcO-MET'
slug: "4-aco-met"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-AcO-MET

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\4-aco-met.md`
```md
---
title: '4-AcO-MET'
slug: "4-aco-met"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-AcO-MET

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\4-aco-mipt.fa.md`
```md
---
title: '4-AcO-MiPT'
slug: "4-aco-mipt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-AcO-MiPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\4-aco-mipt.md`
```md
---
title: '4-AcO-MiPT'
slug: "4-aco-mipt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-AcO-MiPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\4-ho-det.fa.md`
```md
---
title: '4-HO-DET'
slug: "4-ho-det"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-DET

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\4-ho-det.md`
```md
---
title: '4-HO-DET'
slug: "4-ho-det"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-DET

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\4-ho-dipt.fa.md`
```md
---
title: '4-HO-DiPT'
slug: "4-ho-dipt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-DiPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\4-ho-dipt.md`
```md
---
title: '4-HO-DiPT'
slug: "4-ho-dipt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-DiPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\4-ho-dpt.fa.md`
```md
---
title: '4-HO-DPT'
slug: "4-ho-dpt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-DPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\4-ho-dpt.md`
```md
---
title: '4-HO-DPT'
slug: "4-ho-dpt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-DPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\4-ho-ept.fa.md`
```md
---
title: '4-HO-EPT'
slug: "4-ho-ept"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-EPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\4-ho-ept.md`
```md
---
title: '4-HO-EPT'
slug: "4-ho-ept"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-EPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\4-ho-met.fa.md`
```md
---
title: '4-HO-MET'
slug: "4-ho-met"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-MET

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\4-ho-met.md`
```md
---
title: '4-HO-MET'
slug: "4-ho-met"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-MET

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\4-ho-mipt.fa.md`
```md
---
title: '4-HO-MiPT'
slug: "4-ho-mipt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-MiPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\4-ho-mipt.md`
```md
---
title: '4-HO-MiPT'
slug: "4-ho-mipt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-MiPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\4-ho-mpt.fa.md`
```md
---
title: '4-HO-MPT'
slug: "4-ho-mpt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-MPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\4-ho-mpt.md`
```md
---
title: '4-HO-MPT'
slug: "4-ho-mpt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-MPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\5-meo-dalt.fa.md`
```md
---
title: '5-MeO-DALT'
slug: "5-meo-dalt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 5-MeO-DALT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\5-meo-dalt.md`
```md
---
title: '5-MeO-DALT'
slug: "5-meo-dalt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 5-MeO-DALT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\5-meo-dipt.fa.md`
```md
---
title: '5-MeO-DiPT'
slug: "5-meo-dipt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 5-MeO-DiPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\5-meo-dipt.md`
```md
---
title: '5-MeO-DiPT'
slug: "5-meo-dipt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 5-MeO-DiPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\5-meo-dmt.fa.md`
```md
---
title: '5-MeO-DMT'
slug: "5-meo-dmt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 5-MeO-DMT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\5-meo-dmt.md`
```md
---
title: '5-MeO-DMT'
slug: "5-meo-dmt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 5-MeO-DMT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\5-meo-mipt.fa.md`
```md
---
title: '5-MeO-MiPT'
slug: "5-meo-mipt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 5-MeO-MiPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\5-meo-mipt.md`
```md
---
title: '5-MeO-MiPT'
slug: "5-meo-mipt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 5-MeO-MiPT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\56-mdo-dmt.fa.md`
```md
---
title: '5,6-MDO-DMT'
slug: "56-mdo-dmt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 5,6-MDO-DMT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\56-mdo-dmt.md`
```md
---
title: '5,6-MDO-DMT'
slug: "56-mdo-dmt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 5,6-MDO-DMT

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\baeocystin.fa.md`
```md
---
title: 'Baeocystin'
slug: "baeocystin"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# Baeocystin

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\baeocystin.md`
```md
---
title: 'Baeocystin'
slug: "baeocystin"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# Baeocystin

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\bufotenin.fa.md`
```md
---
title: 'Bufotenin'
slug: "bufotenin"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# Bufotenin

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\bufotenin.md`
```md
---
title: 'Bufotenin'
slug: "bufotenin"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# Bufotenin

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\psilocin.fa.md`
```md
---
title: 'Psilocin'
slug: "psilocin"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# Psilocin

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\psilocin.md`
```md
---
title: 'Psilocin'
slug: "psilocin"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# Psilocin

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\psilocybin.fa.md`
```md
---
title: 'Psilocybin'
slug: "psilocybin"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# Psilocybin

_Page coming soon._

```

---
### `wiki\Psychoactives\Hallucinogens\Psychedelics\Tryptamines\Substituted tryptamines\psilocybin.md`
```md
---
title: 'Psilocybin'
slug: "psilocybin"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# Psilocybin

_Page coming soon._

```

---
### `pages\fa\about.astro`
```astro
---
import BaseLayout from "../../layouts/BaseLayout.astro";
---

<BaseLayout lang="fa">

  <main class="px-[clamp(1rem,4vw,4rem)] py-24 
               text-neutral-800 dark:text-neutral-100
               max-w-4xl mx-auto leading-relaxed">

    <!-- Heading -->
    <h1 class="text-4xl font-bold mb-12 tracking-tight text-center">
      About Me
    </h1>

    <!-- Card -->
    <section
      class="rounded-3xl p-8 mb-20
             bg-white/10 dark:bg-black/20 backdrop-blur-xl
             border border-white/20 shadow-xl
             transition-all">

      <h2 class="text-2xl font-semibold mb-6">Hi, I’m Ali Ghorbani AKA “Coughy”</h2>

      <p class="mb-6">
        I write fiction, poetry, research papers, and develop experimental tools across
        philosophy, linguistics, computation, and consciousness studies.  
        My work spans many domains, but all share the same theme:
        <strong>breaking inherited structures</strong> — whether linguistic, conceptual, or computational — 
        to see what grows in the cracks.
      </p>

      <p class="mb-6">
        I explore intersections between human cognition, altered states, language, and
        machine intelligence. I also build software tools, write experimental poetry,
        and maintain <a href="/wiki" class="text-blue-600 dark:text-blue-400 underline">my online wiki</a>
        documenting altered states of consciousness.
      </p>

      <p class="mb-6">
        Some of my projects include:
      </p>

      <ul class="list-disc pl-6 space-y-2 mb-6">
        <li><strong>Contraculator</strong> — a philosophical numerical system.</li>
        <li><strong>Flatshot</strong> — flatten entire codebases for AI processing.</li>
        <li>
          <strong>Fa_Docs</strong> — a Persian typography extension for Google Docs.
        </li>
        <li>
          <strong>Enpsyclopedia</strong> — a conceptual database on consciousness.
        </li>
      </ul>

      <p class="mb-6">
        My work often mixes formal structure with surrealistic or playful elements.
        Whether in code or poetry, I focus on <strong>rewiring assumptions</strong> —
        seeing what happens when you loosen a system from its historical constraints.
      </p>

      <p class="opacity-70">
        If you'd like to collaborate, talk, or ask questions:
        you can find me on Twitter, GitHub, or Telegram.
      </p>

    </section>

    <!-- Optional Portrait / Photo Block 
    <section
      class="w-full rounded-3xl overflow-hidden 
             bg-white/10 dark:bg-black/20 backdrop-blur-xl
             border border-white/20 shadow-xl">
      <img 
        src="/images/profile-placeholder.jpg"
        alt="Ali Ghorbani"
        class="w-full h-80 object-cover opacity-90"
      />
    </section>-->

  </main>

</BaseLayout>

```

---
### `pages\fa\art.astro`
```astro

```

---
### `pages\fa\blog.astro`
```astro
---
import { getCollection } from "astro:content";
import BaseLayout from "../../layouts/BaseLayout.astro";
import BlogPost from "../../components/BlogPost.astro";

const pageTitle = "My Astro Learning Blog";
const allPosts = await getCollection("blog");
---

<BaseLayout lang="fa">
  <section class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-16 text-white">
    <header class="mb-10 text-center">
      <h1 class="text-4xl font-extrabold tracking-tight mb-3 bg-clip-text text-transparent bg-linear-to-r from-blue-400 to-purple-500">
        {pageTitle}
      </h1>
      <p class="text-lg text-white/80">
        This is where I’ll share posts about my journey learning Astro.
      </p>
    </header>

    <ul class="space-y-6">
      {
        allPosts.map((post) => (
          <li
            class="p-6 bg-white/10 border border-white/20 backdrop-blur-md rounded-2xl shadow-md hover:bg-white/15 transition-all duration-300 ease-in-out"
          >
            <BlogPost
              url={`/posts/${post.id}/`}
              title={post.data.title}
            />
          </li>
        ))
      }
    </ul>
  </section>
</BaseLayout>

```

---
### `pages\fa\index.astro`
```astro
---
import BaseLayout from "../../layouts/BaseLayout.astro";
---

<BaseLayout lang="fa">

<main dir="rtl" class="relative text-neutral-800 dark:text-neutral-100 font-[Vazirmatn]">

  <!-- BACKGROUND -->
  <div class="pointer-events-none fixed inset-0 z-0 opacity-50">
    <div class="absolute inset-0 bg-linear-to-br from-purple-500/10 via-blue-500/10 to-pink-500/10 blur-3xl animate-pulse-slow"></div>
  </div>

  <!-- HERO -->
  <section class="relative z-10 flex flex-col items-center justify-center 
                  text-center pt-48 pb-32 px-4">

    <h1 class="text-6xl md:text-7xl font-semibold tracking-tight mb-6 drop-shadow-lg">
      coughy<span class="opacity-50 bg-linear-to-r from-blue-500 to-purple-500 bg-clip-text text-transparent">.</span>net
    </h1>

    <p class="text-xl md:text-2xl opacity-80 max-w-2xl leading-relaxed">
      کافی‌نت، کافی برای همه‌ی نت‌ها
    </p>

  </section>

  <!-- PORTALS FLEX -->
  <section class="relative z-10 max-w-5xl mx-auto px-2 sm:px-6 pb-8">
    <div
      class="flex flex-wrap gap-8 justify-center items-start"
    >
      <!-- ویکی / گردان‌روان (FEATURE CARD) -->
      <a
        href="/fa/wiki"
        class="group flex-[2_2_0%] min-w-full md:min-w-[360px] lg:min-w-[360px] lg:max-w-2xl
               rounded-3xl  bg-white/10 dark:bg-black/20
               border border-white/20 backdrop-blur-xl shadow-lg
               hover:bg-white/20 dark:hover:bg-black/30
               hover:-translate-y-1 hover:shadow-2xl
               transition-all duration-500 cursor-pointer text-right"
      >
        
        <div class="relative w-full aspect-square overflow-hidden rounded-2xl bg-white/10 backdrop-blur-md shadow">
          <img
            src="/images/gardanravan.jpg"
            alt="گردان‌روان"
            class="absolute inset-0 w-full h-full object-cover"
            loading="lazy"
          />
        </div>
        <h2 class="text-2xl font-semibold mb-4 pt-3 pr-5">ویکی گردان‌روان</h2>
        <p class="opacity-80 leading-relaxed mt-4 pt-2 pr-5">
          بزرگ‌ترین دانشنامه‌ی حالات تغییریافته‌ی آگاهی به زبان فارسی
        </p>

        <div class="mt-6 text-blue-300 opacity-0 group-hover:opacity-100 transition-all">
          ← مشاهده
        </div>
      </a>
      <!-- Fiction & Poetry -->
      <a
        href="/fa/literature"
        class="group flex-1 min-w-60 sm:min-w-[260px] lg:max-w-sm
               rounded-3xl p-6 sm:p-8 bg-white/10 dark:bg-black/20
               border border-white/20 backdrop-blur-xl shadow-lg
               hover:bg-white/20 dark:hover:bg-black/30
               hover:-translate-y-1 hover:shadow-2xl
               transition-all duration-500 cursor-pointer text-right"
      >
        <h2 class="text-2xl font-semibold mb-4">داستان کوتاه</h2>
        <p class="opacity-80 leading-relaxed">
          داستان‌های کوتاه منتشرشده و پیش‌نویس‌ها
        </p>
        <div class="mt-6 text-blue-300 opacity-0 group-hover:opacity-100 transition-all">
          ← مشاهده
        </div>
      </a>
      <!-- Projects -->
      <a
        href="/fa/projects"
        class="group flex-1 min-w-60 sm:min-w-[260px] lg:max-w-sm
               rounded-3xl p-6 sm:p-8 bg-white/10 dark:bg-black/20
               border border-white/20 backdrop-blur-xl shadow-lg
               hover:bg-white/20 dark:hover:bg-black/30
               hover:-translate-y-1 hover:shadow-2xl
               transition-all duration-500 cursor-pointer text-right"
      >
        <h2 class="text-2xl font-semibold mb-4">نرم‌افزارآلات</h2>
        <p class="opacity-80 leading-relaxed">
          نرم‌افزار، آزمایش‌ها و ابزارهای فلسفی
        </p>
        <div class="mt-6 text-blue-300 opacity-0 group-hover:opacity-100 transition-all">
          ← مشاهده
        </div>
      </a>




      <!-- Research
      <a
        href="/fa/research"
        class="group flex-1 min-w-[240px] sm:min-w-[260px] lg:max-w-sm
               rounded-3xl p-6 sm:p-8 bg-white/10 dark:bg-black/20
               border border-white/20 backdrop-blur-xl shadow-lg
               hover:bg-white/20 dark:hover:bg-black/30
               hover:-translate-y-1 hover:shadow-2xl
               transition-all duration-500 cursor-pointer text-right"
      >
        <h2 class="text-2xl font-semibold mb-4">مقالات و پژوهش‌ها</h2>
        <p class="opacity-80 leading-relaxed">
          مقالات علمی و پژوهش‌ها
        </p>
        <div class="mt-6 text-blue-300 opacity-0 group-hover:opacity-100 transition-all">
          ← مشاهده
        </div>
      </a> -->

    </div>
  </section>

  <!-- QUOTE -->
  <section class="relative z-10 pb-32 mt-10 px-6 flex justify-center">
    <blockquote
      class="max-w-3xl text-center text-xl md:text-2xl font-light
             opacity-80 leading-relaxed italic"
    >
      سه چیز را به خاطر بسپار
      <br>
      <i class="text-lg jus">-کنفسیونس</i>
    </blockquote>
  </section>

</main>

</BaseLayout>

<style is:global>
  @keyframes pulse-slow {
    0% { opacity: 0.3; transform: scale(1); }
    50% { opacity: 0.6; transform: scale(1.05); }
    100% { opacity: 0.3; transform: scale(1); }
  }
</style>

```

---
### `pages\fa\literature.astro`
```astro
---
import BaseLayout from "../../layouts/BaseLayout.astro";
---

<BaseLayout lang="fa">

  <main class="px-6 py-24 max-w-4xl mx-auto text-neutral-800 dark:text-neutral-100 leading-relaxed">

    <h1 class="text-4xl font-serif font-bold mb-12 text-center tracking-tight">
      ادبیات
    </h1>

    <p dir="rtl" class="text-center opacity-80 max-w-2xl mx-auto mb-16 ">
     داستان های کوتاه و... فعلاً همین!
    </p>

    <div class="grid md:grid-cols-2 gap-10">

      <!-- Poems 
      <a 
        href="/poems"
        class="group rounded-2xl overflow-hidden bg-white/10 dark:bg-white/5
               border border-white/20 backdrop-blur-lg 
               hover:bg-white/20 dark:hover:bg-white/10 
               transition-all duration-300 p-8 text-center"
      >
        <h2 class="text-3xl font-serif font-semibold mb-4 group-hover:opacity-80">
          Poems
        </h2>
        <p class="opacity-70 text-sm font-serif leading-snug">
        </p>
      </a>-->

      <!-- Stories -->
      <a 
        href="/fa/stories"
        class="group rounded-2xl overflow-hidden bg-white/10 dark:bg-white/5
               border border-white/20 backdrop-blur-lg 
               hover:bg-white/20 dark:hover:bg-white/10 
               transition-all duration-300 p-8 text-center"
      >
        <h2 class="text-3xl font-serif font-semibold mb-4 group-hover:opacity-80">
          داستان‌های کوتاه
        </h2>
        <p class="opacity-70 text-sm font-serif leading-snug">
        </p>
      </a>

      <!-- (Optional) Essays 
      <a 
        href="/essays"
        class="group rounded-2xl overflow-hidden bg-white/10 dark:bg-white/5
               border border-white/20 backdrop-blur-lg 
               hover:bg-white/20 dark:hover:bg-white/10 
               transition-all duration-300 p-8 text-center"
      >
        <h2 class="text-3xl font-serif font-semibold mb-4 group-hover:opacity-80">
          Essays
        </h2>
        <p class="opacity-70 text-sm font-serif leading-snug">
          Reflections, thoughts, and longer explorations — coming soon.
        </p>
      </a>-->

      <!-- (Optional) Quotes 
      <a 
        href="/quotes"
        class="group rounded-2xl overflow-hidden bg-white/10 dark:bg-white/5
               border border-white/20 backdrop-blur-lg 
               hover:bg-white/20 dark:hover:bg-white/10 
               transition-all duration-300 p-8 text-center"
      >
        <h2 class="text-3xl font-serif font-semibold mb-4 group-hover:opacity-80">
          Quotes
        </h2>
        <p class="opacity-70 text-sm font-serif leading-snug">
          Favorite lines and wisdom from writers, poets, and thinkers.
        </p>
      </a>-->

    </div>


  </main>

</BaseLayout>

```

---
### `pages\fa\partners.astro`
```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
const pageTitle = "Home Page";
---
<BaseLayout lang="fa">

    
</BaseLayout>
```

---
### `pages\fa\projects.astro`
```astro
---
import BaseLayout from "../../layouts/BaseLayout.astro";

const projects = [
  {
    title: "Contraculator",
    description:
      "A philosophical calculator free from most evolutionary assumptions. You must first construct its numeric system from scratch in order to use it.",
    github: "https://github.com/wr3yth/Contraculator",
    demo: "https://wr3yth.github.io/Contraculator/"
  },

  {
    title: "Flatshot",
    description:
      "Feed entire projects into LLMs without mess. Flatshot flattens any project into a single machine/human-readable file, ignoring irrelevant data.",
    github: "https://github.com/wr3yth/Flatshot"
  },

  {
    title: "🇮🇷 Fa_Docs | گوگل فاکس",
    description:
      "A Google Docs add-on that brings advanced Persian (Farsi) typography & numbering features — fully RTL-compatible.",
    link: "https://workspace.google.com/marketplace/app/farsi_tools/xxxxxxxx"
  },

  {
    title: "Enpsyclopedia of Altered States of Consciousness",
    description:
      "My ongoing documenting of altered states of consciousness, phenomenology, and psychedelic cognition.",
    link: "/wiki"
  },

    {
    title: "LightMeNow",
    description:
      "web based RGB screen lighting.",
    github: "/https://github.com/wr3yth"
  },
];
---

<BaseLayout lang="fa">
  <main class="w-full px-[clamp(1rem,4vw,4rem)] py-24 
               text-neutral-800 dark:text-neutral-100">

    <h1 class="text-4xl font-bold text-center mb-16 tracking-tight">
پروژه ها    </h1>

    <div
      class="grid gap-10 
             sm:grid-cols-2 
             lg:grid-cols-3 
             xl:grid-cols-4 
             mx-auto max-w-[2000px]"
    >
      {projects.map((p) => (
        <div
          class="rounded-3xl p-6 
                 bg-white/30 dark:bg-black/20 backdrop-blur-xl
                 border border-white/20 shadow-lg
                 transition-all duration-500 
                 hover:bg-white/20 dark:hover:bg-black/30
                 hover:-translate-y-1 hover:shadow-2xl
                 flex flex-col justify-between"
        >
          <div>
            <h2 class="text-xl font-semibold mb-3">{p.title}</h2>
            <p class="text-[0.95rem] opacity-90 leading-relaxed mb-6">
              {p.description}
            </p>
          </div>

          <div class="mt-auto flex flex-wrap gap-3">

            {p.link && (
              <a
                href={p.link}
                class="px-4 py-2 rounded-full text-sm font-medium
                       bg-blue-500/20 hover:bg-blue-500/30
                       dark:bg-blue-500/30 dark:hover:bg-blue-500/40
                       border border-blue-400/40
                       transition-all"
                target="_blank"
              >
                لینک
              </a>
            )}

            {p.github && (
              <a
                href={p.github}
                class="px-4 py-2 rounded-full text-sm font-medium
                       bg-gray-500/20 hover:bg-gray-500/30
                       dark:bg-gray-500/30 dark:hover:bg-gray-500/40
                       border border-gray-400/40
                       transition-all"
                target="_blank"
              >
                گیت‌هاب
              </a>
            )}

            {p.demo && (
              <a
                href={p.demo}
                class="px-4 py-2 rounded-full text-sm font-medium
                       bg-purple-500/20 hover:bg-purple-500/30
                       dark:bg-purple-500/30 dark:hover:bg-purple-500/40
                       border border-purple-400/40
                       transition-all"
                target="_blank"
              >
دموی زنده              </a>
            )}

          </div>
        </div>
      ))}
    </div>
  <!-- QUOTE -->
  <section dir="rtl" class="relative z-10 mb-10 mt-110 pb-10 px-6 flex justify-center">
    <blockquote
      class="max-w-3xl text-center text-xl md:text-2xl font-light
             opacity-80 leading-relaxed italic"
    >
ترجیح می‌دهم در خانه بنشینم و به کفش‌هایم فکر کنم<br>
<i class="text-lg jus">-دکتر علی شریعتی</i></blockquote>
  </section>
  </main>
</BaseLayout>

```

---
### `pages\literature\index.astro`
```astro
---
import BaseLayout from "../../layouts/BaseLayout.astro";
---

<BaseLayout>

  <main class="px-6 py-24 max-w-4xl mx-auto text-neutral-800 dark:text-neutral-100 leading-relaxed">

    <h1 class="text-4xl font-serif font-bold mb-12 text-center tracking-tight">
      Literature
    </h1>

    <p class="text-center opacity-80 max-w-2xl mx-auto mb-16">
      A curated selection of my creative writing and poetry.
    </p>

    <div class="grid md:grid-cols-2 gap-10">

      <!-- Poems -->
      <a 
        href="/poems"
        class="group rounded-2xl overflow-hidden bg-white/10 dark:bg-white/5
               border border-white/20 backdrop-blur-lg 
               hover:bg-white/20 dark:hover:bg-white/10 
               transition-all duration-300 p-8 text-center"
      >
        <h2 class="text-3xl font-serif font-semibold mb-4 group-hover:opacity-80">
          Poems
        </h2>
        <p class="opacity-70 text-sm font-serif leading-snug">
        </p>
      </a>

      <!-- Stories -->
      <a 
        href="/stories"
        class="group rounded-2xl overflow-hidden bg-white/10 dark:bg-white/5
               border border-white/20 backdrop-blur-lg 
               hover:bg-white/20 dark:hover:bg-white/10 
               transition-all duration-300 p-8 text-center"
      >
        <h2 class="text-3xl font-serif font-semibold mb-4 group-hover:opacity-80">
          Stories
        </h2>
        <p class="opacity-70 text-sm font-serif leading-snug">
        </p>
      </a>

      <!-- (Optional) Essays 
      <a 
        href="/essays"
        class="group rounded-2xl overflow-hidden bg-white/10 dark:bg-white/5
               border border-white/20 backdrop-blur-lg 
               hover:bg-white/20 dark:hover:bg-white/10 
               transition-all duration-300 p-8 text-center"
      >
        <h2 class="text-3xl font-serif font-semibold mb-4 group-hover:opacity-80">
          Essays
        </h2>
        <p class="opacity-70 text-sm font-serif leading-snug">
          Reflections, thoughts, and longer explorations — coming soon.
        </p>
      </a>-->

      <!-- (Optional) Quotes 
      <a 
        href="/quotes"
        class="group rounded-2xl overflow-hidden bg-white/10 dark:bg-white/5
               border border-white/20 backdrop-blur-lg 
               hover:bg-white/20 dark:hover:bg-white/10 
               transition-all duration-300 p-8 text-center"
      >
        <h2 class="text-3xl font-serif font-semibold mb-4 group-hover:opacity-80">
          Quotes
        </h2>
        <p class="opacity-70 text-sm font-serif leading-snug">
          Favorite lines and wisdom from writers, poets, and thinkers.
        </p>
      </a>-->

    </div>

  </main>

</BaseLayout>

```

---
### `pages\poems\index.astro`
```astro
---
import BaseLayout from "../../layouts/BaseLayout.astro";
import { getCollection } from "astro:content";

// load poems
const poems = await getCollection("poetry");

// get first 2–3 lines as excerpt
const excerpt = (body?: string) => {
  if (!body) return "";
  const lines = body.trim().split("\n").filter(Boolean).slice(0, 3);
  return lines.join("\n");
};
---

<BaseLayout>

  <main class="px-6 py-24 max-w-4xl mx-auto text-neutral-800 dark:text-neutral-100 leading-relaxed">

    <!-- Title -->
    <h1 class="text-4xl font-serif font-bold mb-12 text-center tracking-tight">
      Poems
    </h1>

    <div class="grid md:grid-cols-2 gap-10">
      {poems.map((poem) => (
        <a 
          href={`/poems/${poem.id}`} 
          class="group rounded-2xl overflow-hidden bg-white/10 dark:bg-white/5
                 border border-white/20 backdrop-blur-lg 
                 hover:bg-white/20 dark:hover:bg-white/10 
                 transition-all duration-300"
        >

          <!-- Preview image/video if exists -->
          {poem.data.image && poem.data.image.endsWith(".mp4") ? (
            <video 
              src={poem.data.image}
              autoplay
              loop
              muted
              playsinline
              class="w-full h-48 object-cover opacity-80 group-hover:opacity-100 transition"
            ></video>
          ) : poem.data.image ? (
            <img 
              src={poem.data.image}
              alt={poem.data.title}
              class="w-full h-48 object-cover opacity-80 group-hover:opacity-100 transition"
            />
          ) : (
            <div class="w-full h-48 bg-gradient-to-br from-white/10 to-white/5 dark:from-white/5 dark:to-white/10"></div>
          )}

          <!-- Text content -->
          <div class="p-6">
            <h2 class="text-2xl font-serif font-semibold mb-2 group-hover:opacity-80">
              {poem.data.title}
            </h2>

            {poem.data.poet && (
              <p class="text-sm opacity-60 italic mb-3">
                by {poem.data.poet}
              </p>
            )}

            <p class="whitespace-pre-line opacity-80 text-sm font-serif leading-snug line-clamp-4">
              {excerpt(poem.body)}
            </p>

          </div>

        </a>
      ))}
    </div>

  </main>

</BaseLayout>

```

---
### `pages\poems\[id].astro`
```astro
---
import { getCollection, render } from "astro:content";
import PoetryLayout from "../../layouts/PoetryLayout.astro";

export async function getStaticPaths() {
  const poems = await getCollection("poetry");

  return poems.map((entry) => ({
    params: { id: entry.id },
    props: { entry }
  }));
}

const { entry } = Astro.props;
const { Content } = await render(entry);
---

<PoetryLayout frontmatter={entry.data}>
  <Content />
</PoetryLayout>

```

---
### `pages\posts\[...slug].astro`
```astro
---
import { getCollection, render } from 'astro:content';
import MarkdownPostLayout from '../../layouts/MarkdownPostLayout.astro';

export async function getStaticPaths() {
  const posts = await getCollection('blog');
  return posts.map(post => ({
    params: { slug: post.id }, props: { post },
  }));
}

const { post } = Astro.props;
const { Content } = await render(post);
---
<MarkdownPostLayout frontmatter={post.data}>
  <Content />
</MarkdownPostLayout>
```

---
### `pages\research\index.astro`
```astro
---
import BaseLayout from "../../layouts/BaseLayout.astro";

const papers = [
  {
    title: "How AI can Revolutionize NPCs in Single-player Games",
    link: "/pdf/Threshold-16_2-v6.pdf#page=83",
    image: "/images/Threshold.jpeg", // ← replace later
  },

];
---

<BaseLayout>

  <main class="w-full px-[clamp(1rem,4vw,4rem)] py-24 
               text-neutral-800 dark:text-neutral-100">

    <h1 class="text-4xl font-bold text-center mb-16 tracking-tight">
      Research & Publications
    </h1>

    <div
      class="grid gap-12 
             sm:grid-cols-1
             lg:grid-cols-2 
             xl:grid-cols-3 
             max-w-[1400px] mx-auto"
    >
      {papers.map((p) => (
        <article
          class="rounded-3xl overflow-hidden
                 bg-white/10 dark:bg-black/20 backdrop-blur-xl
                 border border-white/20 shadow-lg
                 hover:bg-white/20 dark:hover:bg-black/30
                 hover:-translate-y-1 hover:shadow-2xl
                 transition-all duration-500 flex flex-col"
        >
          <!-- Image -->
          <div class="w-full h-full relative">
            <img
              src={p.image}
              alt={p.title}
              class="w-full h-full object-cover transition-transform duration-700
                     hover:scale-105"
            />
            <!-- Light overlay for readability -->
            <div class="absolute inset-0 bg-black/10 dark:bg-black/20 pointer-events-none"></div>
          </div>
        
          <!-- Content -->
          <div class="p-6 flex flex-col flex-grow">
            <h2 class="text-xl font-semibold mb-3">{p.title}</h2>
          
            <p class="text-[0.95rem] opacity-90 leading-relaxed mb-6">
                    Published in <b>Threshold</b> - Scholarly Journal of the English Language Department of <b>Shahid Beheshti University.</b><br/> - Vol 16 · No 2 · p.75 

            </p>
          
            <div class="mt-auto">
              <a
                href={p.link}
                target="_blank"
                class="inline-block px-4 py-2 rounded-full text-sm font-medium
                       bg-blue-500/20 hover:bg-blue-500/30
                       dark:bg-blue-500/30 dark:hover:bg-blue-500/40
                       border border-blue-400/40 transition-all"
              >
                Read full paper
              </a>
            </div>
          </div>
        </article>

      ))}
    </div>

  </main>
</BaseLayout>

```

---
### `pages\stories\index.astro`
```astro
---
import BaseLayout from "../../layouts/BaseLayout.astro";
import { getCollection } from "astro:content";

const stories = await getCollection("stories");
---

<BaseLayout>
  <main class="max-w-3xl mx-auto px-6 py-20">

    <h1 class="text-3xl font-semibold mb-10">Stories</h1>

    {stories.length === 0 && (
      <p class="text-neutral-500">No stories found.</p>
    )}

    <ul class="space-y-8">
      {stories.map((story) => (
        <li class="p-5 rounded-xl bg-white/10 backdrop-blur-md shadow">
          <a href={`/stories/${story.id}/`} class="text-2xl font-bold hover:text-blue-400">
            {story.data.title}
          </a>

          {story.data.description && (
            <p class="mt-2 opacity-80">{story.data.description}</p>
          )}
        </li>
      ))}
    </ul>

  </main>
</BaseLayout>

```

---
### `pages\stories\[id].astro`
```astro
---
import { getCollection, render } from "astro:content";
import FictionLayout from "../../layouts/FictionLayout.astro";

export async function getStaticPaths() {
  const stories = await getCollection("stories");
  return stories.map(entry => ({
    params: { id: entry.id },
    props: { entry },
  }));
}

const { entry } = Astro.props;
const { Content } = await render(entry);
---

<FictionLayout frontmatter={entry.data}>


  <Content />

</FictionLayout>

```

---
### `pages\tags\index.astro`
```astro
---
import { getCollection } from "astro:content";
import BaseLayout from '../../layouts/BaseLayout.astro';
const allPosts = await getCollection("blog");
const tags = [...new Set(allPosts.map((post) => post.data.tags).flat())];
const pageTitle = "Tag Index";
---
<!-- ... -->
<BaseLayout pageTitle={pageTitle}>
  <div class="tags">
    {tags.map((tag) => (
      <p class="tag"><a href={`/tags/${tag}`}>{tag}</a></p>
    ))}
  </div>
</BaseLayout>
<style>
  a {
    color: #00539F;
  }

  .tags {
    display: flex;
    flex-wrap: wrap;
  }

  .tag {
    margin: 0.25em;
    border: dotted 1px #a1a1a1;
    border-radius: .5em;
    padding: .5em 1em;
    font-size: 1.15em;
    background-color: #F8FCFD;
  }
</style>
```

---
### `pages\tags\[tag].astro`
```astro
---
import { getCollection } from "astro:content";
import BaseLayout from "../../layouts/BaseLayout.astro";
import BlogPost from "../../components/BlogPost.astro";

export async function getStaticPaths() {
  const allPosts = await getCollection("blog");
  const uniqueTags = [...new Set(allPosts.map((post) => post.data.tags).flat())];

  return uniqueTags.map((tag) => {
    const filteredPosts = allPosts.filter((post) =>
      post.data.tags.includes(tag)
    );
    return {
      params: { tag },
      props: { posts: filteredPosts },
    };
  });
}

const { tag } = Astro.params;
const { posts } = Astro.props;
---

<BaseLayout pageTitle={tag}>
  <p>Posts tagged with {tag}</p>
  <ul>
    { posts.map((post) => <BlogPost url={`/posts/${post.id}/`} title={post.data.title} />) }
  </ul>
</BaseLayout>
```

---
### `pages\wiki\about.astro`
```astro

```

---
### `pages\wiki\effects.astro`
```astro
---
import BaseLayout from "../../layouts/LayoutWiki.astro";
import { getCollection } from "astro:content";
import WikiTree from "../../components/WikiTree.astro";

const all = await getCollection("wiki");

// English only
const entries = all.filter((e) => !e.id.endsWith(".fa"));

const effectEntries = entries.filter((e) =>
  e.filePath?.includes("/Psychoactive_Effects/")
);
---

<BaseLayout pageTitle="Coughy's Wiki">
  <main class="w-full px-6 lg:px-10 py-16 lg:py-24 max-w-7xl mx-auto">
    <header class="mb-14">
      <h1 class="text-4xl lg:text-5xl font-bold mb-4">
        Coughy’s Encyclopedia of Consciousness
      </h1>
      <p class="opacity-80 max-w-2xl">
        An encyclopedia of consciousness — concepts, states, tools, and maps.
      </p>
    </header>

    <section class="mb-20">
      <h2 class="text-2xl lg:text-3xl font-semibold mb-4">
        Psychoactive Effects
      </h2>
      <p class="opacity-75 mb-6 max-w-3xl">
        Phenomenological effects grouped by sensory, cognitive, physical and experiential domains.
      </p>

      <WikiTree entries={effectEntries} rootFolder="Psychoactive_Effects" />
    </section>
  </main>
</BaseLayout>

```

---
### `pages\wiki\harm_reduction.astro`
```astro

```

---
### `pages\wiki\index.astro`
```astro
---
import BaseLayout from "../../layouts/LayoutWiki.astro";
---

<BaseLayout pageTitle="Coughy's Encyclopedia of Consciousness">
  <main class="w-full px-6 lg:px-10 py-20 lg:py-28 max-w-7xl mx-auto">

    <!-- HERO SECTION -->
    <section class="mb-20 text-center">
      <h1 class="text-5xl lg:text-6xl font-bold mb-6">
        Coughy’s Encyclopedia of Consciousness
      </h1>

      <p class="opacity-80 text-lg max-w-3xl mx-auto leading-relaxed">
        A continuously expanding knowledgebase of altered states, psychoactive
        substances, phenomenological effects, and cognitive models of 
        consciousness.
      </p>
    </section>

    <!-- CATEGORY GRID -->
    <section>
      <div
        class="grid gap-10 lg:gap-14
               grid-cols-1 sm:grid-cols-2
               max-w-4xl mx-auto"
      >

        <!-- EFFECTS -->
        <a
          href="/wiki/effects"
          class="group block p-8 rounded-3xl 
                 bg-white/10 dark:bg-white/5 
                 border border-white/10 backdrop-blur-xl shadow-xl
                 hover:-translate-y-1 hover:shadow-2xl 
                 transition-all duration-300"
        >
          <div class="flex items-center gap-4 mb-4">

            <!-- Inline brain SVG -->
            <svg 
              xmlns="http://www.w3.org/2000/svg" 
              class="w-10 h-10 opacity-70 group-hover:opacity-90 transition"
              viewBox="0 0 24 24" fill="none" stroke="currentColor"
              stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"
            >
              <path d="M12 5a3 3 0 1 0-6 0c0 1 .5 1.5 1 2-1 0-2 .5-2 2a3 3 0 1 0 3 3"/>
              <path d="M12 5a3 3 0 1 1 6 0c0 1-.5 1.5-1 2 1 0 2 .5 2 2a3 3 0 1 1-3 3"/>
              <path d="M12 5v14"/>
            </svg>

            <h2 class="text-2xl font-semibold">
              Psychoactive Effects
            </h2>
          </div>

          <p class="opacity-75 leading-relaxed text-sm">
            A structured taxonomy of sensory, cognitive, physical and
            experiential psychoactive effects.
          </p>
        </a>

        <!-- PSYCHOACTIVES -->
        <a
          href="/wiki/psychoactives"
          class="group block p-8 rounded-3xl 
                 bg-white/10 dark:bg-white/5 
                 border border-white/10 backdrop-blur-xl shadow-xl
                 hover:-translate-y-1 hover:shadow-2xl 
                 transition-all duration-300"
        >
          <div class="flex items-center gap-4 mb-4">

            <!-- Inline molecule SVG -->
            <svg 
              xmlns="http://www.w3.org/2000/svg" 
              class="w-10 h-10 opacity-70 group-hover:opacity-90 transition"
              viewBox="0 0 24 24" fill="none" stroke="currentColor"
              stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"
            >
              <circle cx="12" cy="12" r="3" />
              <path d="M19.4 15a1.65 1.65 0 0 0 0-3"/>
              <path d="M4.6 15a1.65 1.65 0 0 1 0-3"/>
              <path d="M12 5.6a1.65 1.65 0 0 1 0-3"/>
              <path d="M12 21.4a1.65 1.65 0 0 0 0-3"/>
            </svg>

            <h2 class="text-2xl font-semibold">
              Psychoactives
            </h2>
          </div>

          <p class="opacity-75 leading-relaxed text-sm">
            Explore chemical families, plants, and preparations that alter consciousness.
          </p>
        </a>

      </div>
    </section>

    <!-- FOOTNOTE -->
    <section class="mt-24 border-t border-white/10 pt-14 text-center opacity-70">
      <p class="text-sm tracking-wide">
        More categories coming soon — cognition, models, maps, protocols, and research.
      </p>
    </section>

  </main>
</BaseLayout>

```

---
### `pages\wiki\interactions.astro`
```astro

```

---
### `pages\wiki\psychoactives.astro`
```astro
---
import BaseLayout from "../../layouts/LayoutWiki.astro";
import { getCollection } from "astro:content";
import WikiTree from "../../components/WikiTree.astro";

const all = await getCollection("wiki");

// English only
const entries = all.filter((e) => !e.id.endsWith(".fa"));

const effectEntries = entries.filter((e) =>
  e.filePath?.includes("/Psychoactive_Effects/")
);

const psychoactiveEntries = entries.filter((e) =>
  e.filePath?.includes("/Psychoactives/")
);
---

<BaseLayout pageTitle="Coughy's Wiki">
  <main class="w-full px-6 lg:px-10 py-16 lg:py-24 max-w-7xl mx-auto">
    <header class="mb-14">
      <h1 class="text-4xl lg:text-5xl font-bold mb-4">
        Coughy’s Encyclopedia of Consciousness
      </h1>
      <p class="opacity-80 max-w-2xl">
        An encyclopedia of consciousness — concepts, states, tools, and maps.
      </p>
    </header>
    
    <section>
      <h2 class="text-2xl lg:text-3xl font-semibold mb-4">
        Psychoactives
      </h2>
      <p class="opacity-75 mb-6 max-w-3xl">
        Chemical families and preparations which alter consciousness — psychedelics, dissociatives, stimulants, depressants, nootropics.
      </p>

      <WikiTree entries={psychoactiveEntries} rootFolder="Psychoactives" />
    </section>
  </main>
</BaseLayout>

```

---
### `pages\wiki\reports.astro`
```astro

```

---
### `pages\wiki\[id].astro`
```astro
---
import { getCollection, render } from "astro:content";
import WikiLayout from "../../layouts/LayoutWiki.astro";

export async function getStaticPaths() {
  const articles = await getCollection("wiki");
  return articles.map((entry) => ({
    params: { id: entry.id },
    props: { entry },
  }));
}

const { entry } = Astro.props;
const { Content } = await render(entry);
---

<WikiLayout frontmatter={entry.data}>
  <Content />
</WikiLayout>

```

---
### `pages\fa\poems\index.astro`
```astro
---
import BaseLayout from "../../../layouts/BaseLayout.astro";
import { getCollection } from "astro:content";

// load poems
const poems = await getCollection("poetry");

// get first 2–3 lines as excerpt
const excerpt = (body?: string) => {
  if (!body) return "";
  const lines = body.trim().split("\n").filter(Boolean).slice(0, 3);
  return lines.join("\n");
};
---

<BaseLayout lang="fa">

  <main class="px-6 py-24 max-w-4xl mx-auto text-neutral-800 dark:text-neutral-100 leading-relaxed">

    <!-- Title -->
    <h1 class="text-4xl font-serif font-bold mb-12 text-center tracking-tight">
      Poems
    </h1>

    <div class="grid md:grid-cols-2 gap-10">
      {poems.map((poem) => (
        <a 
          href={`/poems/${poem.id}`} 
          class="group rounded-2xl overflow-hidden bg-white/10 dark:bg-white/5
                 border border-white/20 backdrop-blur-lg 
                 hover:bg-white/20 dark:hover:bg-white/10 
                 transition-all duration-300"
        >

          <!-- Preview image/video if exists -->
          {poem.data.image && poem.data.image.endsWith(".mp4") ? (
            <video 
              src={poem.data.image}
              autoplay
              loop
              muted
              playsinline
              class="w-full h-48 object-cover opacity-80 group-hover:opacity-100 transition"
            ></video>
          ) : poem.data.image ? (
            <img 
              src={poem.data.image}
              alt={poem.data.title}
              class="w-full h-48 object-cover opacity-80 group-hover:opacity-100 transition"
            />
          ) : (
            <div class="w-full h-48 bg-gradient-to-br from-white/10 to-white/5 dark:from-white/5 dark:to-white/10"></div>
          )}

          <!-- Text content -->
          <div class="p-6">
            <h2 class="text-2xl font-serif font-semibold mb-2 group-hover:opacity-80">
              {poem.data.title}
            </h2>

            {poem.data.poet && (
              <p class="text-sm opacity-60 italic mb-3">
                by {poem.data.poet}
              </p>
            )}

            <p class="whitespace-pre-line opacity-80 text-sm font-serif leading-snug line-clamp-4">
              {excerpt(poem.body)}
            </p>

          </div>

        </a>
      ))}
    </div>

  </main>

</BaseLayout>

```

---
### `pages\fa\poems\[id].astro`
```astro
---
import { getCollection, render } from "astro:content";
import PoetryLayout from "../../../layouts/PoetryLayout.astro";

export async function getStaticPaths() {
  const poems = await getCollection("poetry");

  return poems.map((entry) => ({
    params: { id: entry.id },
    props: { entry }
  }));
}

const { entry } = Astro.props;
const { Content } = await render(entry);
---

<PoetryLayout frontmatter={entry.data}>
  <Content />
</PoetryLayout>

```

---
### `pages\fa\research\index.astro`
```astro
---
import BaseLayout from "../../../layouts/BaseLayout.astro";

const papers = [
  {
    title: "How AI can Revolutionize NPCs in Single-player Games",
    link: "/pdf/Threshold-16_2-v6.pdf#page=83",
    image: "/images/Threshold.jpeg", // ← replace later
  },

];
---

<BaseLayout lang="fa">

  <main class="w-full px-[clamp(1rem,4vw,4rem)] py-24 
               text-neutral-800 dark:text-neutral-100">

    <h1 class="text-4xl font-bold text-center mb-16 tracking-tight">
      Research & Publications
    </h1>

    <div
      class="grid gap-12 
             sm:grid-cols-1
             lg:grid-cols-2 
             xl:grid-cols-3 
             max-w-[1400px] mx-auto"
    >
      {papers.map((p) => (
        <article
          class="rounded-3xl overflow-hidden
                 bg-white/10 dark:bg-black/20 backdrop-blur-xl
                 border border-white/20 shadow-lg
                 hover:bg-white/20 dark:hover:bg-black/30
                 hover:-translate-y-1 hover:shadow-2xl
                 transition-all duration-500 flex flex-col"
        >
          <!-- Image -->
          <div class="w-full h-full relative">
            <img
              src={p.image}
              alt={p.title}
              class="w-full h-full object-cover transition-transform duration-700
                     hover:scale-105"
            />
            <!-- Light overlay for readability -->
            <div class="absolute inset-0 bg-black/10 dark:bg-black/20 pointer-events-none"></div>
          </div>
        
          <!-- Content -->
          <div class="p-6 flex flex-col flex-grow">
            <h2 class="text-xl font-semibold mb-3">{p.title}</h2>
          
            <p class="text-[0.95rem] opacity-90 leading-relaxed mb-6">
                    Published in <b>Threshold</b> - Scholarly Journal of the English Language Department of <b>Shahid Beheshti University.</b><br/> - Vol 16 · No 2 · p.75 

            </p>
          
            <div class="mt-auto">
              <a
                href={p.link}
                target="_blank"
                class="inline-block px-4 py-2 rounded-full text-sm font-medium
                       bg-blue-500/20 hover:bg-blue-500/30
                       dark:bg-blue-500/30 dark:hover:bg-blue-500/40
                       border border-blue-400/40 transition-all"
              >
                Read full paper
              </a>
            </div>
          </div>
        </article>

      ))}
    </div>

  </main>
</BaseLayout>

```

---
### `pages\fa\stories\index.astro`
```astro
---
import BaseLayout from "../../../layouts/BaseLayout.astro";
import { getCollection } from "astro:content";
import { formatDate } from "../../../utils/formatDate";

const stories = await getCollection("storiesFa");

// Sort by date newest → oldest
stories.sort((a, b) => {
  const da = new Date(a.data.date ?? 0).getTime();
  const db = new Date(b.data.date ?? 0).getTime();
  return db - da;
});


// Split into two groups
const published = stories.filter((s) => s.data.published === true);
const drafts = stories.filter((s) => !s.data.published);
---

<BaseLayout lang="fa" pageTitle="داستان‌ها">

  <main class="px-6 py-20 max-w-5xl mx-auto direction-rtl text-right">

    <h1 class="text-4xl font-bold mb-12">داستان‌ها</h1>


    <!-- ============================= -->
    <!--        PUBLISHED STORIES      -->
    <!-- ============================= -->
    {published.length > 0 && (
      <section class="mb-16">
        <h2 class="text-2xl font-semibold mb-6 opacity-90">
          منتشر شده
        </h2>

        <div class="grid gap-10 sm:grid-cols-2 lg:grid-cols-3 auto-rows-[1fr]">
          {published.map((story) => (
            <a
              href={`/fa/story/${story.id}`}
              class="group block rounded-2xl overflow-hidden
                     bg-white/10 dark:bg-white/5 
                     border border-white/20 backdrop-blur-xl shadow-lg
                     hover:-translate-y-1 hover:shadow-2xl
                     transition-all duration-300"
            >
            {story.data.image ? (
              <div class="w-full overflow-hidden rounded-t-2xl">
                <img
                  src={story.data.image}
                  alt={story.data.title}
                  class="w-full h-auto object-cover group-hover:scale-105 transition-transform duration-500"
                />
              </div>
            ) : (
              <div 
                class="w-full aspect-4/3 bg-linear-to-br from-purple-600/20 
                       to-blue-600/20 flex items-center justify-center
                       text-5xl opacity-30"
              >
                📘
              </div>
            )}


              <div class="p-6">
                <h3 class="text-xl font-semibold mb-3 group-hover:opacity-80">
                  {story.data.title}
                </h3>

                {story.data.description && (
                  <p class="opacity-70 mb-3 text-sm leading-relaxed line-clamp-3">
                    {story.data.description}
                  </p>
                )}

                {story.data.date && (
                  <p class="text-xs opacity-60">
                    {formatDate(new Date(story.data.date), "fa")}
                  </p>
                )}
              </div>
            </a>
          ))}
        </div>
      </section>
    )}


    <!-- ============================= -->
    <!--      UNPUBLISHED STORIES      -->
    <!-- ============================= -->
    {drafts.length > 0 && (
      <section class="mb-10">
        <h2 class="text-2xl font-semibold mb-6 opacity-60">
          منتشر نشده / پیش‌نویس
        </h2>

        <div class="grid gap-10 sm:grid-cols-2 lg:grid-cols-3 auto-rows-[1fr]">
          {drafts.map((story) => (
            <a
              href={`/fa/story/${story.id}`}
              class="group block rounded-2xl overflow-hidden
                     bg-white/5 dark:bg-black/20
                     border border-white/10 backdrop-blur-xl shadow-lg
                     hover:-translate-y-1 hover:shadow-2xl
                     transition-all duration-300 opacity-75 hover:opacity-100"
            >
          {story.data.image ? (
              <div class="w-full overflow-hidden rounded-t-2xl">
                <img
                  src={story.data.image}
                  alt={story.data.title}
                  class="w-full h-auto object-cover group-hover:scale-105 transition-transform duration-500"
                />
              </div>
            ) : (
              <div 
                class="w-full aspect-4/3 bg-linear-to-br from-purple-600/20 
                       to-blue-600/20 flex items-center justify-center
                       text-5xl opacity-30"
              >
                📘
              </div>
            )}
            
          

              <div class="p-6">
                <h3 class="text-xl font-semibold mb-3 group-hover:opacity-80">
                  {story.data.title}
                </h3>

                {story.data.description && (
                  <p class="opacity-70 mb-3 text-sm leading-relaxed line-clamp-3">
                    {story.data.description}
                  </p>
                )}

                {story.data.date && (
                  <p class="text-xs opacity-60">
                    {formatDate(new Date(story.data.date), "fa")}
                  </p>
                )}
              </div>
            </a>
          ))}
        </div>
      </section>
    )}

  </main>

</BaseLayout>

```

---
### `pages\fa\stories\[id].astro`
```astro
---
import { getCollection, render } from "astro:content";
import BaseLayout from "../../../layouts/BaseLayout.astro";
import { formatDate } from "../../../utils/formatDate.ts";
import FaFictionLayout from "../../../layouts/FictionLayoutFa.astro";
export async function getStaticPaths() {
  const stories = await getCollection("storiesFa");
  return stories.map((entry) => ({
    params: { id: entry.id },
    props: { entry },
  }));
}

const { entry } = Astro.props;



const isPDF = entry.data.file?.endsWith(".pdf");
---

<BaseLayout lang="fa">

  <main class="px-6 py-20 max-w-3xl mx-auto text-right direction-rtl">

    <h1 class="text-3xl font-serif mb-6">{entry.data.title}</h1>

    {entry.data.description && (
      <p class="opacity-70 mb-6">{entry.data.description}</p>
    )}

    {isPDF ? (
      <object
        data={`/fa-stories/${entry.data.file}`}
        type="application/pdf"
        class="w-full h-[80vh] rounded-xl border border-white/20"
      >
        <a
          href={`/fa-stories/${entry.data.file}`}
          class="text-blue-400 underline"
        >
          دانلود PDF
        </a>
      </object>
    ) : (
      // markdown story
      <article class="prose prose-invert max-w-none leading-relaxed">
      </article>
    )}

  </main>

</BaseLayout>

```

---
### `pages\fa\wiki\about.astro`
```astro

```

---
### `pages\fa\wiki\effects.astro`
```astro

```

---
### `pages\fa\wiki\harm_reduction.astro`
```astro

```

---
### `pages\fa\wiki\index.astro`
```astro
---
import BaseLayout from "../../../layouts/LayoutWiki.astro";
import { getCollection } from "astro:content";

const all = (await getCollection("wiki")).filter(
  (e) => !e.id.endsWith(".fa")
);

type WikiEntry = (typeof all)[number];

type TreeNode = {
  indexEntry: WikiEntry | null;
  pages: WikiEntry[];
  children: Map<string, TreeNode>;
};

function normalizeName(str: string): string {
  return str
    .toLowerCase()
    .replace(/\.fa$/, "")
    .replace(/\.md$/, "")
    .replace(/[_\-]+/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function formatLabel(s: string): string {
  return s.replace(/[_\-]+/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());
}

const rootMap: Map<string, TreeNode> = new Map();

function getOrCreateNode(name: string, map: Map<string, TreeNode>): TreeNode {
  let node = map.get(name);
  if (!node) {
    node = { indexEntry: null, pages: [], children: new Map() };
    map.set(name, node);
  }
  return node;
}

// Build tree
for (const entry of all) {
  const filePath = entry.filePath!;
  const parts = filePath.split("/");
  const wikiParts = parts.slice(2);
  if (wikiParts.length === 0) continue;

  const filename = wikiParts.at(-1)!;
  const baseName = filename.replace(/\.fa\.md$/, "").replace(/\.md$/, "");

  const folders = wikiParts.slice(0, -1);
  const top = folders[0] ?? "General";

  let node = getOrCreateNode(top, rootMap);

  for (let i = 1; i < folders.length; i++) {
    node = getOrCreateNode(folders[i]!, node.children);
  }

  const lastFolder = folders[folders.length - 1] ?? top;
  if (normalizeName(lastFolder) === normalizeName(baseName)) {
    node.indexEntry = entry;
  } else {
    node.pages.push(entry);
  }
}

// Sort tree
function sortTree(node: TreeNode): void {
  node.pages.sort((a, b) => a.data.title.localeCompare(b.data.title));
  for (const child of node.children.values()) sortTree(child);
}
for (const node of rootMap.values()) sortTree(node);

const sortedRoots = Array.from(rootMap.entries()).sort(
  (a, b) => a[0].localeCompare(b[0])
);

// Recursive renderer
function renderNode(name: string, node: TreeNode, depth: number) {
  const children = Array.from(node.children.entries()).sort(
    (a, b) => a[0].localeCompare(b[0])
  );

  const containerClass =
    depth === 0
      ? "mb-20"
      : "mb-8 ml-4 border-l border-white/10 pl-4";

  return (
    <section class={containerClass}>
      {depth === 0 && (
        <h2 class="text-2xl lg:text-3xl font-semibold mb-4">
          {node.indexEntry ? (
            <a
              href={`/wiki/${node.indexEntry.id}`}
              class="hover:underline underline-offset-2"
            >
              {formatLabel(name)}
            </a>
          ) : (
            formatLabel(name)
          )}
        </h2>
      )}

      {depth === 1 && (
        <h3 class="text-xl font-semibold mb-3">
          {node.indexEntry ? (
            <a
              href={`/wiki/${node.indexEntry.id}`}
              class="hover:underline underline-offset-2"
            >
              {formatLabel(name)}
            </a>
          ) : (
            formatLabel(name)
          )}
        </h3>
      )}

      {depth >= 2 && (
        <h4 class="text-lg font-semibold mb-2">
          {node.indexEntry ? (
            <a
              href={`/wiki/${node.indexEntry.id}`}
              class="hover:underline underline-offset-2"
            >
              {formatLabel(name)}
            </a>
          ) : (
            formatLabel(name)
          )}
        </h4>
      )}

      {node.pages.length > 0 && (
        <ul class="space-y-1.5 text-sm mb-3">
          {node.pages.map((entry) => (
            <li>
              <a
                href={`/wiki/${entry.id}`}
                class="hover:underline underline-offset-2 hover:opacity-80"
              >
                {entry.data.title}
              </a>
            </li>
          ))}
        </ul>
      )}

      {children.length > 0 && (
        <div
          class={
            depth === 0
              ? "grid gap-8 md:grid-cols-2 xl:grid-cols-3"
              : "space-y-3"
          }
        >
          {children.map(([childName, childNode]) =>
            renderNode(childName, childNode, depth + 1)
          )}
        </div>
      )}
    </section>
  );
}
---

<BaseLayout pageTitle="Coughy's Wiki">
  <main class="w-full px-6 lg:px-10 py-16 lg:py-24 max-w-7xl mx-auto">
    <header class="mb-14">
      <h1 class="text-4xl lg:text-5xl font-bold mb-4">
        Coughy’s Encyclopedia of Consciousness
      </h1>
      <p class="opacity-80 max-w-2xl">
        An encyclopedia of consciousness — concepts, states, tools, and maps.
      </p>
    </header>

    {sortedRoots.map(([rootName, rootNode]) =>
      renderNode(rootName, rootNode, 0)
    )}
  </main>
</BaseLayout>

```

---
### `pages\fa\wiki\interactions.astro`
```astro

```

---
### `pages\fa\wiki\reports.astro`
```astro

```

---
### `pages\fa\wiki\substances.astro`
```astro

```

---
### `pages\fa\wiki\[id].astro`
```astro
---
import { getCollection, render } from "astro:content";
import WikiLayout from "../../../layouts/LayoutWiki.astro";

export async function getStaticPaths() {
  const articles = await getCollection("wiki");
  return articles.map((entry) => ({
    params: { id: entry.id },
    props: { entry },
  }));
}

const { entry } = Astro.props;
const { Content } = await render(entry);
---

<WikiLayout frontmatter={entry.data}>
  <Content />
</WikiLayout>

```

---
### `assets\backgrounds\bwca-dusk.png`
```png
[Error reading file: 'utf-8' codec can't decode byte 0x89 in position 0: invalid start byte]
```

---
### `assets\backgrounds\bwca-night.png`
```png
[Error reading file: 'utf-8' codec can't decode byte 0x89 in position 0: invalid start byte]
```

