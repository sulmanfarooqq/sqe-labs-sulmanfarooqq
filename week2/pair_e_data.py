from pathlib import Path


PAIR_LETTER = "E"
EVALUATION_DATE = "2026-04-27"
EVALUATOR_NAME = "Muhammad Suliman and Adnan Arif"
STUDENT_ID = "FA23-BSE-047 and FA23-BSE-047"
SECTION = "BSE"
DEVICE_MODEL = "Android test device"
OS_VERSION = "Android 14"
NETWORK_CONDITIONS = "Stable WiFi with mobile-data fallback"

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
WORKBOOK_TEMPLATE = WORKSPACE_ROOT / "SQE_Lab2_Excel_Templates (1).xlsx"
WORKBOOK_OUTPUT = WORKSPACE_ROOT / "SQE_Lab2_Excel_Templates_filled_PairE.xlsx"
RADAR_OUTPUT = Path(__file__).resolve().parent / "quality_radar_Spotify_YouTube_Music.png"
REPORT_OUTPUT = Path(__file__).resolve().parent / "SQE_Lab2_Muhammad_Suliman_Adnan_Arif_PairE.pdf"

WEIGHTS = [0.15, 0.12, 0.10, 0.15, 0.15, 0.15, 0.08, 0.10]
CHARACTERISTICS = [
    "Functional Suitability",
    "Performance Efficiency",
    "Compatibility",
    "Usability",
    "Reliability",
    "Security",
    "Maintainability",
    "Portability",
]

APPS = {
    "app1": {
        "name": "Spotify",
        "store_name": "Spotify: Music and Podcasts",
        "version": "9.1.42.2058",
        "platform": "Android",
        "min_os": "Android 7.0+",
        "store_rating": "4.1/5",
        "last_updated": "Apr 22, 2026",
        "ratings": [4, 4, 5, 5, 4, 4, 3, 5],
        "summary_observations": [
            "Observation 1: Spotify covers the main music-streaming workflow well with playlists, podcasts, audiobooks, recommendations, and offline support for Premium. Observation 2: It lacks YouTube Music's native music-video switching and remix/live-performance depth, so functional breadth is strong but not unmatched.",
            "Observation 1: Official documentation offers quality settings up to approximately 320kbit/s on Premium for mobile, tablet, and desktop. Observation 2: Recent store reviews still mention ad friction and occasional recommendation issues, so performance was rated good rather than excellent.",
            "Observation 1: Spotify officially supports desktop, mobile, tablet, web browsers, watches, cars, TVs, speakers, and Spotify Connect. Observation 2: Its cross-device control is stronger and more mature than YouTube Music's current device story.",
            "Observation 1: Spotify's interface is familiar, polished, and fast to learn for search, playback, playlisting, and discovery. Observation 2: Core actions are visually prominent and the navigation structure is simpler than YouTube Music's ecosystem blend.",
            "Observation 1: Spotify has broad deployment and mature infrastructure, but current Play Store reviews still report intermittent bugs in recommendations and free-tier playback friction. Observation 2: Reliability is good overall, yet not perfect enough to justify a 5.",
            "Observation 1: Spotify encrypts data in transit, but the Play Store also says the app may share location, personal info, and device identifiers with third parties. Observation 2: That privacy trade-off keeps Security at 4 instead of 5.",
            "Observation 1: Spotify updates frequently, but its Android Play listing provides only generic release notes rather than detailed changelogs. Observation 2: Limited transparency about individual fixes lowers maintainability despite active releases.",
            "Observation 1: Spotify is available on Android, iOS, Windows, macOS, web, watches, cars, TVs, speakers, and more. Observation 2: Spotify Connect makes handoff across devices especially strong, so portability is one of its clearest advantages.",
        ],
        "comparative_strength": "Stronger device ecosystem, easier cross-device control, cleaner usability",
    },
    "app2": {
        "name": "YouTube Music",
        "store_name": "YouTube Music",
        "version": "9.15.50",
        "platform": "Android",
        "min_os": "Use latest browser on desktop; Android app current-store build",
        "store_rating": "4.5/5",
        "last_updated": "Apr 25, 2026",
        "ratings": [5, 4, 3, 4, 4, 4, 4, 3],
        "summary_observations": [
            "Observation 1: YouTube Music combines standard streaming with music videos, covers, remixes, live performances, and hard-to-find content that Spotify often lacks. Observation 2: The official feature list also highlights seamless switching between audio and video, making functional suitability its strongest category.",
            "Observation 1: Official help documents show up to 256kbps AAC and OPUS for high-quality playback, and Play Store reviews praise low delay when switching tracks. Observation 2: Desktop-web lag complaints and slower feature rollout keep the score at 4 rather than 5.",
            "Observation 1: Google says YouTube Music works on mobile devices and computers, and can be used with watches, cars, Google Assistant, Maps, and Waze. Observation 2: However, Google also states the dedicated YouTube Music app is not available on living-room devices, which weakens compatibility versus Spotify.",
            "Observation 1: YouTube Music is easy to use for listeners already invested in YouTube and Google accounts. Observation 2: The app is feature-rich, but playlist and desktop interactions still feel less polished than Spotify's overall navigation model.",
            "Observation 1: YouTube Music has the scale and stability of Google's platform and recent reviews describe playback as generally smooth. Observation 2: Some users still complain about missing features and finicky desktop behavior, which prevents an excellent reliability score.",
            "Observation 1: The Play Store says YouTube Music shares no data with third parties, encrypts data in transit, and has an independent security review. Observation 2: It still collects personal and financial information, so the score remains 4 rather than 5.",
            "Observation 1: Google updates the app frequently and recent versions continued shipping through April 2026. Observation 2: Feature rollout appears active, but users still report slow arrival of parity features such as stronger cross-device playback controls.",
            "Observation 1: YouTube Music works across phone, desktop, browser, watch, car, and smart-speaker contexts. Observation 2: The official note that the dedicated app is unavailable on living-room devices reduces portability compared with Spotify's broader native-device footprint.",
        ],
        "comparative_strength": "Broader content catalog, audio-video switching, stronger YouTube ecosystem fit",
    },
}


COMPARATIVE_TEXT = {
    "overall": (
        "Spotify achieved a weighted quality score of 4.27/5.00, while YouTube Music achieved 3.95/5.00, "
        "giving Spotify a margin of 0.32 points. Both apps are strong mainstream streaming products, but the "
        "gap appears because the rubric heavily rewards device compatibility, usability, and portability."
    ),
    "gaps": (
        "The largest gap is Compatibility. Spotify documents broader native device coverage and stronger remote "
        "control through Spotify Connect, while YouTube Music still depends on the main YouTube app for some TV "
        "use cases. The second major gap is Portability, where Spotify again benefits from a more mature device "
        "handoff model across speakers, TVs, cars, browsers, and desktop apps. The third important difference is "
        "Usability: Spotify keeps core discovery, playback, playlist, and device-switch actions more visible, "
        "while YouTube Music's strengths are tied more closely to the larger YouTube ecosystem."
    ),
    "tradeoff": (
        "A clear trade-off exists between ecosystem breadth and device polish. YouTube Music scores higher in "
        "Functional Suitability because it uniquely blends songs, music videos, live performances, remixes, and "
        "rare uploads into one product. Spotify gives up some of that content variety, but in return it offers a "
        "cleaner and more predictable cross-device experience."
    ),
    "recommendation": (
        "Spotify is the better overall recommendation for users who want the most reliable all-purpose music app "
        "across phones, desktop, speakers, TVs, and cars. YouTube Music is the better fit for users who already "
        "pay for YouTube Premium or who care most about music videos, unofficial/live content, and deeper YouTube "
        "integration. Under the weighted ISO 25010 scoring used in this lab, Spotify is the stronger overall app."
    ),
}


STRUCTURED_JUSTIFICATIONS = {
    "app1": {
        1: "Justification: Spotify earned 4/5 for Functional Suitability because it delivers its main streaming, playlist, podcast, and discovery functions consistently, but it lacks YouTube Music's richer music-video and remix ecosystem.",
        2: "Justification: Spotify earned 4/5 for Performance Efficiency because official support documents strong audio-quality options and mature cross-device behavior, but current reviews still mention occasional playback and recommendation friction.",
        3: "Justification: Spotify earned 5/5 for Compatibility because it officially supports a wider and more uniform device ecosystem, including desktop, web, speakers, TVs, cars, watches, and strong Spotify Connect behavior.",
        4: "Justification: Spotify earned 5/5 for Usability because its navigation is polished, predictable, and easy to learn, with core playback, search, library, and device-switching actions kept highly visible.",
        5: "Justification: Spotify earned 4/5 for Reliability because it is a mature large-scale service, but recent store feedback still reports some intermittent issues that prevent a perfect score.",
        6: "Justification: Spotify earned 4/5 for Security because the Play Store states that data is encrypted in transit, but its data-sharing posture is weaker than YouTube Music's current public data-safety declarations.",
        7: "Justification: Spotify earned 3/5 for Maintainability because it updates frequently, yet its public changelogs remain generic and do not explain fixes with enough detail for strong maintainability evidence.",
        8: "Justification: Spotify earned 5/5 for Portability because it provides one of the strongest cross-device listening models in this comparison, especially through Spotify Connect and its broad native platform coverage.",
    },
    "app2": {
        1: "Justification: YouTube Music earned 5/5 for Functional Suitability because it combines standard streaming with music videos, remixes, live performances, and rare uploads that give it broader music-use coverage than Spotify.",
        2: "Justification: YouTube Music earned 4/5 for Performance Efficiency because official audio-quality support and recent user feedback suggest solid playback speed, but desktop-web lag complaints still appear often enough to prevent a 5.",
        3: "Justification: YouTube Music earned 3/5 for Compatibility because it works across many Google-linked environments, but Google's own help pages confirm that the dedicated YouTube Music app is unavailable on living-room devices.",
        4: "Justification: YouTube Music earned 4/5 for Usability because it is easy for Google and YouTube users to understand, though its overall interaction model is still less polished and less direct than Spotify's.",
        5: "Justification: YouTube Music earned 4/5 for Reliability because it benefits from Google's large platform infrastructure, but current feedback still points to occasional missing-feature and desktop-behavior frustrations.",
        6: "Justification: YouTube Music earned 4/5 for Security because the Play Store says data is encrypted in transit, shared with no third parties, and independently reviewed, yet the app still collects sensitive account-linked information.",
        7: "Justification: YouTube Music earned 4/5 for Maintainability because current update cadence is active and feature work continues, but some product-quality improvements still arrive more slowly than users expect.",
        8: "Justification: YouTube Music earned 3/5 for Portability because it works across phones, browsers, cars, watches, and speakers, but it still lacks Spotify's stronger session-handoff model and full living-room parity.",
    },
}


RECOMMENDATIONS = [
    {
        "app": "Spotify",
        "action": "Publish detailed release notes that clearly separate bug fixes, performance changes, and new features",
        "characteristic": "Maintainability",
        "current": 3,
        "target": 4,
        "deficiency": "the Play Store listing uses very generic update notes, which makes it difficult to understand what was fixed in each release",
        "benefit": "users and evaluators would be able to track product quality changes and developer responsiveness more confidently",
    },
    {
        "app": "Spotify",
        "action": "Reduce free-tier ad interruption density and improve recovery from ad-to-playback transitions",
        "characteristic": "Reliability",
        "current": 4,
        "target": 5,
        "deficiency": "recent Play Store reviews still describe excessive ads and disrupted listening flow on the free tier",
        "benefit": "listeners would experience fewer interruptions and a more stable end-to-end playback session",
    },
    {
        "app": "YouTube Music",
        "action": "Deliver a dedicated living-room app experience instead of relying on the broader YouTube app for TV scenarios",
        "characteristic": "Compatibility",
        "current": 3,
        "target": 5,
        "deficiency": "Google's own help page states that the YouTube Music app is not available on living-room devices",
        "benefit": "users would get more consistent playback and navigation behavior across TV and non-TV environments",
    },
    {
        "app": "YouTube Music",
        "action": "Expand cross-device playback control to match Spotify-style session continuity across desktop, mobile, and speakers",
        "characteristic": "Portability",
        "current": 3,
        "target": 4,
        "deficiency": "recent user feedback still points to weaker cross-device playback control compared with Spotify",
        "benefit": "listeners could move between devices more smoothly without losing session context or control options",
    },
]


SOURCES = [
    {
        "label": "Spotify Google Play",
        "url": "https://play.google.com/store/apps/details?id=com.spotify.music",
    },
    {
        "label": "YouTube Music Google Play",
        "url": "https://play.google.com/store/apps/details?hl=en&id=com.google.android.apps.youtube.music",
    },
    {
        "label": "Spotify supported devices",
        "url": "https://support.spotify.com/jo-en/article/supported-devices-for-spotify/",
    },
    {
        "label": "Spotify audio quality",
        "url": "https://support.spotify.com/om-en/article/audio-quality/",
    },
    {
        "label": "Spotify Connect",
        "url": "https://support.spotify.com/ee-en/article/spotify-connect/",
    },
    {
        "label": "YouTube Music supported devices",
        "url": "https://support.google.com/youtubemusic/answer/6308244?hl=en",
    },
    {
        "label": "What is YouTube Music?",
        "url": "https://support.google.com/youtubemusic/answer/6313529?hl=en",
    },
    {
        "label": "YouTube Music audio quality",
        "url": "https://support.google.com/youtubemusic/answer/9076559?co=GENIE.Platform%3DAndroid&hl=en",
    },
    {
        "label": "Where YouTube Music is available",
        "url": "https://support.google.com/youtubemusic/answer/6313540?co=GENIE.Platform%3DDesktop&hl=en",
    },
    {
        "label": "Spotify Android version reference",
        "url": "https://www.techspot.com/downloads/6773-spotify-for-android.html",
    },
    {
        "label": "YouTube Music Android version reference",
        "url": "https://www.apkmirror.com/apk/google-inc/youtube-music/",
    },
]


def weighted_score(ratings):
    return round(sum(r * w for r, w in zip(ratings, WEIGHTS)), 2)


APP1_TOTAL = weighted_score(APPS["app1"]["ratings"])
APP2_TOTAL = weighted_score(APPS["app2"]["ratings"])
