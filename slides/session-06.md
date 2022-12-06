autoscale: true
slidenumbers: true
build-lists: true
slide-transition: true

# Mineure OSS @ EPITA
## Session 6

---

# Cette session

- Préparation visite OSXP
- Licences du logiciel libre (suites et fin)
- Comment animer un projet de logiciel libre (deck 6.5)

---

# Les conférences open source

---

# Qu'est-ce qu'une conférence ?

- Un événement, localisé dans le temps et l'espace, où des personnes se réunissent pour échanger sur un sujet donné.

- Un (ou plusieurs) organisateurs qui préparent l'événement, s'occupent de la communication, de la logistique, la commercialisation, etc.

- Business de plateforme triface:

  - Visiteurs (participants)
  - Speakers (intervenants)
  - Sponsors / exposants

---

# Typologie

- Modèle économique
  - Profit / non profit / hybrid
  - Modèle de revenu (payant / gratuit, mais pour qui ?)
- Conférence / Workshop / Salon / Rencontre d'affaires...
- Généralistes / spécifiques (sur 1 métier, 1 techno, 1 domaine, 1 produit...)
- Standalone / dans un événement plus large ("embedded")
- Audiences (regionale, nationale, internationale)
- Lieu (fixe / tournant / en ligne / hybride)
- Typoologie des speakers (pros/amateurs, stars/anonymes, payés/défrayés/pas payés/payants)
- Cas des formations ?

---

# OSXP

- 1998: "village open source" au milieu du salon "Interop"
- 1998-2005: Linux Expo
- 2006-2010: Solutions Linux
- 2010-2014: Open World Forum (OWF)
- 2015-2019: Paris Open Source Summit
- 2021-...: Open Source Experience (OSXP)

---

# "Mission OSXP"

- Participe de l'évaluation de la mineure OSS (35% de la note finale)
- Prévoir une visite de l'OSXP le 8 novembre (ou à un autre moment)
- A minima:
  - Visiter le salon
  - Assister à 3 talks (minimum), au choix
- Restitution par écrit (15 nov. -> sf@fermigier.com)
  - "Rapport d'étonnement" (1 page)
      - "Gap analysis" (la réalité du salon vs. les concepts vus en cours)
  - CR synthétique de 3 talks (mini):
      - Modèle: <https://reinout.vanrees.org/weblog/2022/06/16/rotterdam-meetup.html> et autres (<https://reinout.vanrees.org/weblog/tags/python.html>)

---

![fit](images/osxp-mardi-8-0.png)

---

![fit](images/osxp-mardi-8.png)

---

# Retour aux licences

---

# Historique des principales licences libres

OSI: "The following OSI-approved licenses are popular, widely used, or have strong communities:"

[.column]
- 1987: MIT
- 1988: (proto-)BSD
- 1989: GPL v1
- 1990: BSD "4-clause"
- 1991: GPL v2, LGPL ("v2")
- 1998: Mozilla Public License 1.0

[.column]
- 1999: BSD "3-clause" et "2-clause"
- 2004: Apache 2.0
- 2004: CDDL
- 2007: GPL v3, LGPL v2.1
- 2012: Mozilla Public License 2.0
- 2017: Eclipse Public License 2.0

---

# Les points clefs

---

![fit](orig/riehle-ip/slide-16.png)

---

![fit](orig/riehle-ip/slide-17.png)

---

![fit](orig/riehle-ip/slide-18.png)

---

![fit](orig/riehle-ip/slide-22.png)

---

![fit](orig/riehle-ip/slide-23.png)

---

![fit](orig/riehle-ip/slide-26.png)

---

![fit](orig/riehle-ip/slide-27.png)

---

![fit](orig/riehle-ip/slide-28.png)

---

![fit](orig/riehle-ip/slide-29.png)

---

![fit](orig/riehle-ip/slide-30.png)

---

![fit](orig/riehle-ip/slide-31.png)

---

![fit](orig/riehle-ip/slide-32.png)

---

![fit](orig/riehle-ip/slide-33.png)

---

# Shims ?

"Cales" en francais. Aussi appelés "wrappers", "proxies", "adapters", etc.

"In computer programming, a shim is a library that transparently intercepts API calls and changes the arguments passed, handles the operation itself or redirects the operation elsewhere. Shims can be used to support an old API in a newer environment, or a new API in an older environment. Shims can also be used for running programs on different software platforms than they were developed for."

Question ouverte: quelle solution *technique* pour résoudre ce problème *juridique* ?

---

![fit](orig/riehle-ip/slide-34.png)

---

![fit](orig/riehle-ip/slide-35.png)

---

![fit](orig/riehle-ip/slide-39.png)

---

![fit](orig/riehle-ip/slide-46.png)

---

![fit](orig/riehle-ip/slide-47.png)

---

![fit](orig/riehle-ip/slide-48.png)

---

![fit](orig/riehle-ip/slide-49.png)

---

![fit](orig/riehle-ip/slide-50.png)

---

![fit](orig/riehle-ip/slide-51.png)

---

# Outillage

---

# Quelques spécifications

- SPDX: Software Package Data Exchange (<https://spdx.dev/>)
  "An open standard for communicating software bill of material information, including provenance, license, security, and other related information. SPDX reduces redundant work by providing common formats for organizations and communities to share important data, thereby streamlining and improving compliance, security, and dependability. Recognized as the international open standard for security, license compliance, and other software supply chain artifacts as ISO/IEC 5962:2021."

- REUSE (<https://reuse.software/>)
  A set of recommendations to make licensing your Free Software projects easier + to check compliance 

---

# Et quelques outils (Software composition analysis tools)

[.column]
- Open source:
  - FOSSology (open source)
  - Hermine (<https://hermine-foss.org/>)
  - ScanCode
  - Reuse

[.column]
- Propriétaires (périmètres plus large que juste les licences):
  - Black Duck
  - Snyk
  - ...

Plus: (<https://owasp.org/www-community/Component_Analysis>)

---

# Focus: Prolifération des licences

- https://spdx.org/licenses/
- https://www.gnu.org/licenses/license-list.html
- https://opensource.org/licenses
- <https://en.wikipedia.org/wiki/Comparison_of_free_and_open-source_software_licenses>
- https://www.numerique.gouv.fr/publications/politique-logiciel-libre/ouverture/
- https://www.data.gouv.fr/fr/pages/legal/licences/

---

![fit](orig/zack-licenses/slide-022.png)

---

![fit](orig/zack-licenses/slide-023.png)

---

![fit](orig/zack-licenses/slide-024.png)

---

![fit](orig/zack-licenses/slide-025.png)

---

![fit](orig/zack-licenses/slide-026.png)

---

![fit](orig/zack-licenses/slide-027.png)

---

![fit](orig/zack-licenses/slide-028.png)

---

![fit](orig/zack-licenses/slide-029.png)

---

![fit](orig/zack-licenses/slide-030.png)

---

# Focus: politique de licences de l'Etat

---

![fit](images/licences-dinum-1.png)

---

![fit](images/licences-dinum-3.png)

---

![fit](images/licences-dinum-2.png)

---

![fit](images/licences-dinum-4.png)

---

# Le bestiaire des licences

---

![fit](orig/zack-licenses/slide-031.png)

---

![fit](orig/zack-licenses/slide-032.png)

---

![fit](orig/zack-licenses/slide-033.png)

---

![fit](orig/zack-licenses/slide-034.png)

---

![fit](orig/zack-licenses/slide-035.png)

---

![fit](orig/zack-licenses/slide-036.png)

---

![fit](orig/zack-licenses/slide-037.png)

---

![fit](orig/zack-licenses/slide-038.png)

---

![fit](orig/zack-licenses/slide-039.png)

---

![fit](orig/zack-licenses/slide-040.png)

---

![fit](orig/zack-licenses/slide-041.png)

---

![fit](orig/zack-licenses/slide-042.png)

---

![fit](orig/zack-licenses/slide-043.png)

---

![fit](orig/zack-licenses/slide-044.png)

---

![fit](orig/zack-licenses/slide-045.png)

---

![fit](orig/zack-licenses/slide-046.png)

---

![fit](orig/zack-licenses/slide-047.png)

---

![fit](orig/zack-licenses/slide-048.png)

---

![fit](orig/zack-licenses/slide-050.png)

---

![fit](orig/zack-licenses/slide-051.png)

---

![fit](orig/zack-licenses/slide-052.png)

---

![fit](orig/zack-licenses/slide-053.png)

---

![fit](orig/zack-licenses/slide-054.png)

---

![fit](orig/zack-licenses/slide-055.png)

---

![fit](orig/zack-licenses/slide-056.png)

---

![fit](orig/zack-licenses/slide-057.png)

---

![fit](orig/zack-licenses/slide-058.png)

---

![fit](orig/zack-licenses/slide-059.png)

---

![fit](orig/zack-licenses/slide-060.png)

---

![fit](orig/zack-licenses/slide-061.png)

---

![fit](orig/zack-licenses/slide-062.png)

---

![fit](orig/zack-licenses/slide-063.png)

---

![fit](orig/zack-licenses/slide-064.png)

---

![fit](orig/zack-licenses/slide-065.png)

---

![fit](orig/zack-licenses/slide-066.png)

---

![fit](orig/zack-licenses/slide-067.png)

---

![fit](orig/zack-licenses/slide-068.png)

---

![fit](orig/zack-licenses/slide-069.png)

---

![fit](orig/zack-licenses/slide-070.png)

---

![fit](orig/zack-licenses/slide-071.png)

---

![fit](orig/zack-licenses/slide-072.png)

---

![fit](orig/zack-licenses/slide-073.png)

---

![fit](orig/zack-licenses/slide-074.png)

---

![fit](orig/zack-licenses/slide-075.png)

---

![fit](orig/zack-licenses/slide-076.png)

---

![fit](orig/zack-licenses/slide-077.png)

---

![fit](orig/zack-licenses/slide-078.png)

---

![fit](orig/zack-licenses/slide-079.png)

---

![fit](orig/zack-licenses/slide-080.png)

---

![fit](orig/zack-licenses/slide-081.png)

---

![fit](orig/zack-licenses/slide-082.png)

---

![fit](orig/zack-licenses/slide-083.png)

---

![fit](orig/zack-licenses/slide-084.png)

---

![fit](orig/zack-licenses/slide-085.png)

---

![fit](orig/zack-licenses/slide-086.png)

---

![fit](orig/zack-licenses/slide-087.png)

---

![fit](orig/zack-licenses/slide-088.png)

---

![fit](orig/zack-licenses/slide-089.png)

---

![fit](orig/zack-licenses/slide-090.png)

---

![fit](orig/zack-licenses/slide-091.png)

---

![fit](orig/zack-licenses/slide-092.png)

---

![fit](orig/zack-licenses/slide-093.png)

---

![fit](orig/zack-licenses/slide-094.png)

---

![fit](orig/zack-licenses/slide-095.png)

---

![fit](orig/zack-licenses/slide-096.png)

---

![fit](orig/zack-licenses/slide-097.png)

---

![fit](orig/zack-licenses/slide-098.png)

---

![fit](orig/zack-licenses/slide-099.png)

---

![fit](orig/zack-licenses/slide-100.png)

---

![fit](orig/zack-licenses/slide-101.png)

---

![fit](orig/zack-licenses/slide-102.png)

---

![fit](orig/zack-licenses/slide-103.png)

---

![fit](orig/zack-licenses/slide-104.png)

---

![fit](orig/zack-licenses/slide-105.png)

---

# Bonus slides

---

![fit](orig/zack-licenses/slide-107.png)

---

![fit](orig/zack-licenses/slide-108.png)

---

![fit](orig/zack-licenses/slide-109.png)

---

![fit](orig/zack-licenses/slide-110.png)

---

![fit](orig/zack-licenses/slide-111.png)

---

![fit](orig/zack-licenses/slide-112.png)

---

![fit](orig/zack-licenses/slide-113.png)

---

![fit](orig/zack-licenses/slide-114.png)

---

![fit](orig/zack-licenses/slide-115.png)

---

![fit](orig/zack-licenses/slide-116.png)

---

![fit](orig/zack-licenses/slide-117.png)

---

![fit](orig/zack-licenses/slide-118.png)

---

![fit](orig/zack-licenses/slide-119.png)

---

![fit](orig/zack-licenses/slide-120.png)

---

![fit](orig/zack-licenses/slide-121.png)

---

![fit](orig/zack-licenses/slide-122.png)

---

![fit](orig/zack-licenses/slide-123.png)

---

![fit](orig/zack-licenses/slide-124.png)

---

![fit](orig/zack-licenses/slide-125.png)

---

![fit](orig/zack-licenses/slide-126.png)

---

![fit](orig/zack-licenses/slide-127.png)

---

![fit](orig/zack-licenses/slide-128.png)

---

![fit](orig/zack-licenses/slide-129.png)

---

![fit](orig/zack-licenses/slide-130.png)

---

![fit](orig/zack-licenses/slide-131.png)

---

![fit](orig/zack-licenses/slide-132.png)

---

![fit](orig/zack-licenses/slide-133.png)

---

![fit](orig/zack-licenses/slide-134.png)

---

![fit](orig/zack-licenses/slide-135.png)

---

![fit](orig/zack-licenses/slide-136.png)

---

![fit](orig/zack-licenses/slide-137.png)

---

![fit](orig/zack-licenses/slide-138.png)

---

![fit](orig/zack-licenses/slide-139.png)

---

![fit](orig/zack-licenses/slide-140.png)

---

# Crédits

---

![fit](orig/zack-licenses/slide-001.png)

---
![fit](orig/riehle-ip/slide-01.png)
