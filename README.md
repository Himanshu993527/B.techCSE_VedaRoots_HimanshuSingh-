 # 🌿 VedaRoots — The Herbal Healing Experience

---
# 🌱 About the Project
VedaRoots is India's comprehensive digital Ayurvedic plant encyclopedia built as a frontend web application. The platform combines detailed botanical plant profiles, an interactive India map tour, herbal quizzes, and smart search/filter tools to make ancient Ayurvedic knowledge accessible to everyone.
The project covers 500+ medicinal plants across 28 Indian states, organized by AYUSH systems — Ayurveda, Yoga & Naturopathy, Unani, Siddha, and Homeopathy — all recognized by the Government of India's Ministry of AYUSH.

# 🎯 Problem Statement
India has one of the world's richest traditions of plant-based medicine, yet this knowledge remains scattered across ancient texts, regional traditions, and specialist practitioners — inaccessible to the general public, students, and researchers. VedaRoots solves this by creating a centralized, interactive, and user-friendly digital platform.

# 💡 Solution
A fully responsive, interactive web application that:
Digitizes plant profiles with 11 standardized data attributes
Maps medicinal plants geographically across every Indian state
Provides smart search and multi-parameter filtering
Engages users through quizzes, bookmarks, and shareable plant profiles
Works completely offline — no internet required after loading

---

---
# ✨ Features
🗺️ Interactive India Map Tour
Full SVG map of India with all 28 states drawn using coordinate geometry
Hover over any state → tooltip shows state name and plant count
Click any state → side panel displays all native medicinal plants
Click a plant in the panel → full detail modal opens
States highlighted in gold when selected, green glow on hover

# 🌿 Plant Encyclopedia
Detailed profiles with 11 data attributes per plant:
Botanical Name, Common Name, Family
AYUSH System, Therapeutic Category
Plant Type, Plant Part Used
Major Medicinal Uses, Preparation Method
Native Region
Grid and List view toggle
Real-time search by plant name, botanical name, or family
Multi-parameter filtering:
By Plant Type (Herb, Tree, Shrub, Climber, Grass)
By Disease / Therapeutic Category (Diabetes, Fever, Skin, etc.)
By AYUSH System (Ayurveda, Siddha, Unani, etc.)

# 🔖 Bookmark & Share
Bookmark favourite plants — saved to `localStorage` (persists after refresh)
One-click shareable URL — copies direct link to any plant profile
URL updates dynamically (`?plant=id`) for deep linking

# 🧠 Herbal Knowledge Quiz
10 carefully crafted questions about Ayurvedic plants
Progress bar showing completion percentage
Immediate feedback — correct answers turn green, wrong turns red
Final score with performance-based message
Available both on the homepage and as a modal popup

# ❓ FAQ System
10 comprehensive FAQs with smooth accordion animation
Available on-page and as a modal from the navbar icon
CSS `max-height` transition technique for buttery smooth open/close

# 🔐 Login / Register
Tab-switching modal with Login and Register forms
Ready for backend integration (Node.js / Firebase)
Toast notification system for user feedback

# 🎨 Design & Animation
Animated floating leaf particles in hero section
Live counters animating from 0 to target value on page load
Smooth hover transitions on all interactive elements
Fully responsive — works on desktop, tablet, and mobile
Sticky navigation with backdrop blur effect
Custom CSS design system with CSS Variables
---

# 🛠️ Tech Stack
Technology	Version	Purpose
HTML5	Latest	Page structure and semantic markup
CSS3	Latest	Styling, animations, responsive layout
Vanilla JavaScript	ES6+	Interactivity, data rendering, DOM manipulation
SVG	1.1	Interactive India map (all state paths)
Google Fonts	—	Cormorant Garamond + DM Sans typography
localStorage API	—	Client-side bookmark persistence
CSS Grid & Flexbox	—	Responsive layout system
CSS Custom Properties	—	Design token / color system
> ⚡ **Zero external libraries or frameworks** — Pure HTML, CSS, and JavaScript only.

# 📁 Project Structure
```
VedaRoots/
│
├── 📄 index.html              # Main homepage
│   ├── Hero Section           # Animated landing with statistics
│   ├── Features Section       # 6 feature highlight cards
│   ├── India Map Tour         # Interactive SVG state map
│   ├── Quiz Section           # Embedded herbal quiz
│   ├── About Section          # About VedaRoots + Vision + Mission
│   └── FAQ Section            # Accordion FAQ
│
├── 📄 plants.html             # Plant encyclopedia page
│   ├── Sidebar Filters        # Search + type + disease + AYUSH filters
│   ├── Plants Grid            # Responsive card grid
│   └── Plant Detail Modal     # Full profile popup
│
├── 📄 README.md               # This file
│
└── 📄 LICENSE                 # MIT License
```
> 📌 **Note:** The entire project is contained in just 2 HTML files. All CSS and JavaScript is embedded — no separate files needed. This makes deployment as simple as uploading the files.
---
# 🔬 Methodology
The project was developed using Agile Development Methodology in 5 phases:
```
Phase 1: Research & Planning
    ↓ Literature review, requirement analysis, tech selection
Phase 2: System Design  
    ↓ Architecture design, UI/UX wireframing, data schema design
Phase 3: Implementation
    ↓ Module-by-module development (Map → Quiz → FAQ → Auth)
Phase 4: Testing
    ↓ Functional, responsive, browser, and data testing
Phase 5: Deployment
    ↓ Static hosting on GitHub Pages / Netlify
```
# Architecture
```
┌─────────────────────────────────────────┐
│         PRESENTATION LAYER              │
│    HTML5 Structure + CSS3 Styling       │
├─────────────────────────────────────────┤
│           LOGIC LAYER                   │
│    Vanilla JavaScript (ES6+)            │
│  • Event Listeners  • DOM Manipulation  │
│  • Array Methods    • State Management  │
├─────────────────────────────────────────┤
│            DATA LAYER                   │
│  JavaScript Objects + localStorage API  │
│  • Plant Dataset  • Quiz Questions      │
│  • State Map Data • FAQ Content         │
└─────────────────────────────────────────┘
```
# How the India Map Works
All 28 Indian states are drawn as SVG `<path>` elements using coordinate geometry (`M` move, `L` line, `Z` close commands)
Each path has a unique `id` (e.g., `st-mh` for Maharashtra) matching a key in the `stateData` JavaScript object
JavaScript attaches 4 event listeners to every state path: `mouseenter` (tooltip), `mouseleave` (hide tooltip), `mousemove` (follow cursor), `click` (show plant panel)
On click, the state ID is extracted, plant data is fetched from `stateData`, and dynamically rendered as HTML in the side panel

---
# 🎯 Objectives
Primary Objectives
Digitize Ayurvedic Knowledge — Create a comprehensive, searchable digital encyclopedia of Indian medicinal plants
Regional Plant Mapping — Geographically map plants across all 28 Indian states
Education & Awareness — Make Ayurvedic plant knowledge accessible to students, practitioners, and the public
Promote AYUSH Systems — Highlight all 5 government-recognized traditional medicine systems
User Engagement — Drive learning through interactive quizzes, bookmarks, and gamified elements
Knowledge Preservation — Ensure traditional healing knowledge is digitally preserved for future generations
Secondary Objectives
Support Botany, Pharmacy, and Ayurvedic Medicine students with verified plant data
Provide practitioners with a quick-reference plant profile tool
Build a foundation scalable to a full-stack application with real database backend
Demonstrate integration of traditional knowledge with modern web technology

---

# 🤝 Contributing
Contributions are welcome and greatly appreciated! Here's how you can help:
Ways to Contribute
🌿 Add more plants to the encyclopedia dataset
🗺️ Improve state map accuracy using GeoJSON
🌐 Add language translations (Hindi, Tamil, Telugu, etc.)
🐛 Report bugs by opening an Issue
💡 Suggest features via Discussions
🎨 Improve UI/UX design

# 🙏 Acknowledgements
Ministry of AYUSH, Government of India — for publicly available plant data and AYUSH system documentation
National Medicinal Plants Board (NMPB) — for regional plant distribution data
CSIR-NISCAIR — for the Indian Medicinal Plants reference encyclopedia
Google Fonts — for Cormorant Garamond and DM Sans typefaces
Ancient Ayurvedic scholars — whose knowledge in Charaka Samhita and Sushruta Samhita forms the foundation of this project
WHO — for Traditional Medicine Strategy documentation

---
<div align="center">
Made with 🌿 and ❤️ for India's healing heritage
VedaRoots — Rooted in tradition, grown for the future
⭐ Star this repo if you found it helpful! ⭐
</div>
