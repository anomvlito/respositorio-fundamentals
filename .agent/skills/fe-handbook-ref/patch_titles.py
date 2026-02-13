#!/usr/bin/env python3
"""
Patch generic titles in handbook_map.json.
- Reads content_raw to derive descriptive titles.
- Removes duplicate entries for pages 1 and 34.
- Saves patched JSON.
"""
import json, re, sys

JSON_PATH = "resources/handbook_map.json"

# Manual title overrides based on content_raw analysis
TITLE_MAP = {
    # Pages 5-33: Mathematics section
    5:   "Mathematics (Straight Line, Quadratic Equation & Logarithms)",
    6:   "Mathematics (Logarithm Identities & Complex Numbers)",
    7:   "Mathematics (Euler's Identity & Trigonometry)",
    8:   "Mathematics (Trigonometric Identities)",
    9:   "Mathematics (Mensuration of Areas and Volumes — Parabola & Ellipse)",
    10:  "Mathematics (Mensuration — Circular Segment, Sector & Sphere)",
    11:  "Mathematics (Mensuration — Parallelogram, Regular Polygon & Prismoid)",
    12:  "Mathematics (Mensuration — Cone, Cylinder & Paraboloid)",
    13:  "Mathematics (Conic Sections — Parabola & Ellipse)",
    14:  "Mathematics (Conic Sections — Hyperbola & Circle)",
    15:  "Mathematics (Conic Section Equation & Differential Calculus)",
    16:  "Mathematics (Curvature & Radius of Curvature)",
    17:  "Mathematics (L'Hôpital's Rule & Integral Calculus)",
    18:  "Mathematics (Derivatives)",
    19:  "Mathematics (Indefinite Integrals)",
    20:  "Mathematics (Progressions & Series)",
    21:  "Mathematics (Taylor's Series & Differential Equations)",
    22:  "Mathematics (Differential Equations — 2nd Order & Fourier Transform)",
    23:  "Mathematics (Fourier Series)",
    24:  "Mathematics (Fourier Series Examples & Fourier Transform Pair)",
    25:  "Mathematics (Fourier Transform Pairs & Theorems)",
    26:  "Mathematics (Laplace Transforms)",
    27:  "Mathematics (Matrices)",
    28:  "Mathematics (Matrix Properties & Determinants)",
    29:  "Mathematics (Vectors — Dot Product, Cross Product, Gradient)",
    30:  "Mathematics (Vector Identities & Numerical Methods)",
    31:  "Mathematics (Newton's Method of Minimization & Numerical Integration)",
    32:  "Mathematics (Simpson's Rule & Numerical Solution of ODEs)",
    33:  "Probability & Statistics (Dispersion, Mean, Median, Mode)",
    # Scattered pages
    81:  "Statics (Area, Centroid & Moment of Inertia Table)",
    90:  "Dynamics (Kinetic Energy)",
    # Thermodynamics area
    162: "Fluid Mechanics (Net Positive Suction Head — NPSHA)",
    163: "Fluid Mechanics (Compressors)",
    164: "Fluid Mechanics (Isothermal Compression)",
    166: "Fluid Mechanics (Venturi Meters)",
    167: "Fluid Mechanics (Orifice Meters)",
    168: "Fluid Mechanics (Dimensional Analysis & Similitude)",
    # Pages 238-269: Electrical & Computer Engineering
    238: "Electrical & Computer Engineering (Diodes)",
    239: "Electrical & Computer Engineering (Bipolar Junction Transistors — BJT)",
    240: "Electrical & Computer Engineering (JFETs & Depletion MOSFETs)",
    241: "Electrical & Computer Engineering (Enhancement MOSFET)",
    242: "Electrical & Computer Engineering (Number Systems & Codes)",
    243: "Electrical & Computer Engineering (Logic Operations & Boolean Algebra)",
    244: "Electrical & Computer Engineering (Flip-Flops)",
    245: "Electrical & Computer Engineering (Karnaugh Maps — K-Maps)",
    246: "Electrical & Computer Engineering (Network & Internet Layer)",
    247: "Electrical & Computer Engineering (Internet Protocol Addressing)",
    248: "Electrical & Computer Engineering (IPv4 Special Address Blocks)",
    249: "Electrical & Computer Engineering (IPv6 Special Address Blocks)",
    250: "Electrical & Computer Engineering (IPv4 Header Format)",
    251: "Electrical & Computer Engineering (Fragment Offset)",
    252: "Electrical & Computer Engineering (IPv6 Header)",
    253: "Electrical & Computer Engineering (IPv6 Destination Address)",
    254: "Electrical & Computer Engineering (TCP Header — Reserved & Flags)",
    255: "Electrical & Computer Engineering (TCP Options — SYN)",
    256: "Electrical & Computer Engineering (Checksum & Error Checking)",
    257: "Electrical & Computer Engineering (ICMPv6 Types & Codes)",
    258: "Electrical & Computer Engineering (Local Area Network — LAN)",
    259: "Electrical & Computer Engineering (Network Topologies — Star, Bus, Ring)",
    260: "Electrical & Computer Engineering (Communication Methodologies)",
    261: "Electrical & Computer Engineering (Computer Systems & Memory)",
    262: "Electrical & Computer Engineering (Microprocessor Architecture — Harvard)",
    263: "Electrical & Computer Engineering (Instruction Set Architectures — CISC/RISC)",
    264: "Electrical & Computer Engineering (Data Structures)",
    265: "Electrical & Computer Engineering (Algorithm Efficiency — Big-O)",
    266: "Electrical & Computer Engineering (Software Syntax & Pointers)",
    267: "Electrical & Computer Engineering (Nmap Tools & Network Scanning)",
    268: "Electrical & Computer Engineering (Nmap Examples & Port Scanning)",
    269: "Electrical & Computer Engineering (Security Triad & Cryptography)",
}


def main():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    pages = data["pages"]

    # 1. Remove duplicate entries (page 1 with pdf_index=2, page 34 with pdf_index=10)
    before = len(pages)
    pages = [p for p in pages if not (
        (p["handbook_page"] == 1 and p["pdf_index"] == 2) or
        (p["handbook_page"] == 34 and p["pdf_index"] == 10)
    )]
    removed = before - len(pages)
    print(f"Removed {removed} duplicate entries")

    # 2. Patch generic titles
    patched = 0
    for p in pages:
        hp = p["handbook_page"]
        if hp in TITLE_MAP:
            old = p["title"]
            new = TITLE_MAP[hp]
            if "Handbook Page" in old or "(Title TBD)" in old:
                p["title"] = new
                patched += 1
                print(f"  Page {hp}: '{old}' -> '{new}'")

    data["pages"] = pages
    print(f"\nPatched {patched} titles")

    # 3. Save
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved to {JSON_PATH}")

    # 4. Verify no generic titles remain
    remaining = [p for p in pages if "Handbook Page" in p.get("title", "")]
    if remaining:
        print(f"\nWARNING: {len(remaining)} pages still have generic titles:")
        for p in remaining:
            print(f"  Page {p['handbook_page']}: {p['title']}")
    else:
        print("\n✓ All titles are now descriptive!")


if __name__ == "__main__":
    main()
