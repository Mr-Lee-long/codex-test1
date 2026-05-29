from pathlib import Path

OUT = Path("tactical_iphone_dock_output")
OUT.mkdir(exist_ok=True)


def svg_header(title):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1050" viewBox="0 0 1600 1050">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#eef2f4"/>
      <stop offset="1" stop-color="#cfd8dc"/>
    </linearGradient>
    <linearGradient id="cream" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#f2ead8"/>
      <stop offset="0.55" stop-color="#d9ceb7"/>
      <stop offset="1" stop-color="#b8ad98"/>
    </linearGradient>
    <linearGradient id="green" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#788a65"/>
      <stop offset="1" stop-color="#46563f"/>
    </linearGradient>
    <linearGradient id="grey" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#8b9189"/>
      <stop offset="1" stop-color="#59615a"/>
    </linearGradient>
    <linearGradient id="blackRubber" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#262a2d"/>
      <stop offset="1" stop-color="#07090a"/>
    </linearGradient>
    <linearGradient id="screen" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#06111d"/>
      <stop offset="0.7" stop-color="#12324f"/>
      <stop offset="1" stop-color="#00b7ff"/>
    </linearGradient>
    <filter id="shadow" x="-30%" y="-30%" width="160%" height="180%">
      <feDropShadow dx="0" dy="30" stdDeviation="32" flood-color="#263238" flood-opacity="0.32"/>
    </filter>
    <filter id="glow" x="-80%" y="-80%" width="260%" height="260%">
      <feGaussianBlur stdDeviation="7" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="softGlow" x="-60%" y="-60%" width="220%" height="220%">
      <feDropShadow dx="0" dy="0" stdDeviation="8" flood-color="#17dfff" flood-opacity="0.82"/>
    </filter>
    <pattern id="strap" width="16" height="16" patternUnits="userSpaceOnUse" patternTransform="rotate(20)">
      <rect width="16" height="16" fill="#101214"/>
      <rect x="0" y="0" width="4" height="16" fill="#2f3437"/>
      <rect x="9" y="0" width="2" height="16" fill="#41484c"/>
    </pattern>
    <style>
      .label {{ font-family: Arial, sans-serif; fill: #111827; }}
      .tiny {{ font-family: Arial, sans-serif; fill: #bff7ff; font-size: 22px; font-weight: 700; }}
      .screw {{ fill: #111; stroke: #777; stroke-width: 4; }}
      .line {{ stroke: #111; stroke-opacity: .38; stroke-width: 5; fill: none; stroke-linecap: round; }}
    </style>
  </defs>
  <rect width="1600" height="1050" fill="url(#bg)"/>
  <ellipse cx="820" cy="850" rx="590" ry="120" fill="#46515a" opacity=".18"/>
  <text x="80" y="90" class="label" font-size="42" font-weight="800">{title}</text>
'''


def screw(x, y):
    return f'''<circle class="screw" cx="{x}" cy="{y}" r="16"/><path d="M{x-8} {y} L{x+8} {y} M{x} {y-8} L{x} {y+8}" stroke="#6f7578" stroke-width="4" stroke-linecap="round"/>'''


def front_render():
    s = svg_header("户外机能风 iPhone StandBy 底座 - 效果图 01")
    s += '''
  <g filter="url(#shadow)" transform="translate(65 40) skewX(-5)">
    <path d="M310 360 Q310 315 355 315 H1170 Q1220 315 1225 365 L1288 710 Q1296 758 1250 762 H250 Q205 760 216 710 L278 365 Q283 340 310 360 Z" fill="#6d716b"/>
    <path d="M380 300 H1115 Q1160 300 1160 345 V705 Q1160 752 1112 752 H382 Q334 752 334 704 V346 Q334 300 380 300 Z" fill="url(#cream)" stroke="#817a69" stroke-width="5"/>
    <path d="M245 395 Q250 335 315 330 H445 V752 H230 Q197 752 205 717 Z" fill="url(#green)" stroke="#283323" stroke-width="5"/>
    <path d="M1052 330 H1182 Q1248 335 1254 396 L1294 715 Q1300 752 1265 752 H1052 Z" fill="url(#grey)" stroke="#343b36" stroke-width="5"/>

    <rect x="425" y="360" width="590" height="270" rx="54" fill="#12191f" stroke="#0b0d0f" stroke-width="18"/>
    <rect x="448" y="382" width="544" height="226" rx="38" fill="url(#screen)" stroke="#63e8ff" stroke-opacity=".65" stroke-width="4"/>
    <text x="492" y="445" class="tiny">SAT MAR</text>
    <text x="492" y="570" font-family="Arial, sans-serif" font-size="138" fill="#f8fbff" font-weight="900">28</text>
    <text x="765" y="440" class="tiny">MARCH</text>
    <g fill="#e8fbff" opacity=".9" font-family="Arial, sans-serif" font-size="18" font-weight="700">
      <text x="760" y="486">S  M  T  W  T  F  S</text>
      <text x="768" y="525">1   2   3   4   5   6   7</text>
      <text x="768" y="560">8   9  10  11  12  13  14</text>
      <text x="768" y="595">15 16  17  18  19  20  21</text>
    </g>

    <rect x="520" y="670" width="360" height="66" rx="30" fill="#24282a" stroke="#0e1214" stroke-width="5"/>
    <rect x="548" y="690" width="195" height="26" rx="13" fill="none" stroke="#21e8ff" stroke-width="7" filter="url(#softGlow)"/>
    <circle cx="1002" cy="704" r="60" fill="#d6d0c2" stroke="#18e6ff" stroke-width="8" filter="url(#softGlow)"/>
    <circle cx="998" cy="704" r="41" fill="#b9b1a1"/>
    <rect x="294" y="628" width="34" height="104" rx="16" fill="#1c2022" stroke="#111" stroke-width="4"/>
    <rect x="352" y="628" width="34" height="104" rx="16" fill="#1c2022" stroke="#111" stroke-width="4"/>
    <rect x="303" y="640" width="14" height="72" rx="7" fill="#22e6ff" filter="url(#softGlow)"/>
    <rect x="361" y="648" width="14" height="72" rx="7" fill="#22e6ff" filter="url(#softGlow)"/>
    <path d="M276 770 H1202" stroke="#20e4ff" stroke-width="9" stroke-linecap="round" filter="url(#softGlow)"/>

    <circle cx="322" cy="438" r="48" fill="#2e3334" stroke="#101315" stroke-width="7"/>
    <path d="M298 438 H346 M322 414 V462" stroke="#070808" stroke-width="9" stroke-linecap="round"/>
    <circle cx="1158" cy="435" r="34" fill="#2d3030" stroke="#111" stroke-width="6"/>
    <path d="M1143 435 H1173 M1158 420 V450" stroke="#070808" stroke-width="6" stroke-linecap="round"/>
    <circle cx="1168" cy="560" r="35" fill="#2a2d2f" stroke="#111" stroke-width="6"/>
    <circle cx="1168" cy="655" r="46" fill="#1f2325" stroke="#111" stroke-width="6"/>

    <rect x="174" y="512" width="96" height="145" rx="22" fill="url(#blackRubber)" transform="rotate(-7 222 584)"/>
    <path d="M196 542 H250 M190 580 H244 M184 620 H238" stroke="#3e4548" stroke-width="10" stroke-linecap="round" transform="rotate(-7 222 584)"/>
    <rect x="1225" y="505" width="96" height="145" rx="22" fill="url(#blackRubber)" transform="rotate(7 1273 584)"/>
    <path d="M1247 542 H1301 M1253 580 H1307 M1259 620 H1313" stroke="#3e4548" stroke-width="10" stroke-linecap="round" transform="rotate(7 1273 584)"/>

    ''' + screw(390, 345) + screw(1098, 345) + screw(390, 720) + screw(1098, 720) + '''
  </g>
  <text x="92" y="970" class="label" font-size="30" opacity=".72">奶白主舱 + 军绿护甲 + 黑色橡胶块 + 青蓝氛围灯，保留手机横屏待机窗口和右侧充电口。</text>
</svg>'''
    return s


def angled_render():
    s = svg_header("户外机能风 iPhone StandBy 底座 - 效果图 02")
    s += '''
  <g filter="url(#shadow)" transform="translate(30 30)">
    <path d="M330 332 L1128 250 L1322 425 L518 532 Z" fill="#6d756a"/>
    <path d="M518 532 L1322 425 L1266 776 L454 895 Z" fill="#505750"/>
    <path d="M330 332 L518 532 L454 895 L260 690 Z" fill="#55664a"/>

    <path d="M398 334 L1075 272 L1236 420 L560 506 Z" fill="url(#cream)" stroke="#807565" stroke-width="5"/>
    <path d="M560 506 L1236 420 L1192 716 L516 812 Z" fill="#c2b9a6" stroke="#776f60" stroke-width="5"/>
    <path d="M398 334 L560 506 L516 812 L350 641 Z" fill="#748864" stroke="#39432f" stroke-width="5"/>

    <path d="M505 373 L982 331 Q1017 326 1040 350 L1110 420 Q1132 443 1098 449 L624 510 Q590 514 568 490 L493 414 Q470 390 505 373 Z" fill="#0d131a" stroke="#080b0e" stroke-width="18"/>
    <path d="M534 389 L974 347 Q1001 344 1018 362 L1074 418 Q1092 436 1065 439 L634 493 Q606 496 588 477 L527 416 Q508 397 534 389 Z" fill="url(#screen)" stroke="#3bdfff" stroke-width="4"/>
    <text x="584" y="445" class="tiny" transform="rotate(-5 584 445)">STANDBY</text>
    <text x="595" y="510" font-family="Arial, sans-serif" font-size="82" fill="#f6fbff" font-weight="900" transform="rotate(-5 595 510)">28</text>
    <text x="835" y="415" class="tiny" transform="rotate(-5 835 415)">09:41</text>

    <path d="M602 628 L930 586 Q970 581 996 604 L1015 621 Q1040 645 1000 651 L675 694 Q635 699 609 675 L590 657 Q565 634 602 628 Z" fill="#202527" stroke="#111" stroke-width="5"/>
    <path d="M654 647 L821 626" stroke="#20e7ff" stroke-width="9" stroke-linecap="round" filter="url(#softGlow)"/>
    <circle cx="1096" cy="633" r="55" fill="#d4cdbc" stroke="#1deaff" stroke-width="8" filter="url(#softGlow)"/>
    <circle cx="1096" cy="633" r="36" fill="#a79f90"/>
    <path d="M500 804 L1106 716" stroke="#20e7ff" stroke-width="9" stroke-linecap="round" filter="url(#softGlow)"/>

    <path d="M360 250 C430 135 548 120 650 210" fill="none" stroke="url(#strap)" stroke-width="42" stroke-linecap="round"/>
    <rect x="430" y="162" width="115" height="58" rx="14" fill="#252a2b" stroke="#111" stroke-width="6" transform="rotate(22 488 191)"/>
    <path d="M452 184 L508 170 L522 204 L467 218 Z" fill="none" stroke="#7e8f44" stroke-width="10"/>
    <rect x="380" y="283" width="105" height="52" rx="15" fill="#596b4c" stroke="#222" stroke-width="5" transform="rotate(-5 432 309)"/>
    <rect x="994" y="205" width="105" height="52" rx="15" fill="#687065" stroke="#222" stroke-width="5" transform="rotate(-5 1046 231)"/>

    <circle cx="415" cy="612" r="43" fill="#242a2c" stroke="#0d1112" stroke-width="7"/>
    <path d="M392 612 H438 M415 590 V634" stroke="#060708" stroke-width="8" stroke-linecap="round"/>
    <circle cx="469" cy="697" r="40" fill="#f0a33b" stroke="#8f5b1f" stroke-width="7"/>
    <path d="M469 678 V716" stroke="#9c5a18" stroke-width="8" stroke-linecap="round"/>
    <rect x="1228" y="548" width="88" height="140" rx="23" fill="url(#blackRubber)" transform="rotate(-5 1272 618)"/>
    <path d="M1247 582 H1302 M1244 619 H1298 M1241 657 H1295" stroke="#41494c" stroke-width="10" stroke-linecap="round" transform="rotate(-5 1272 618)"/>
    ''' + screw(430, 362) + screw(1118, 306) + screw(536, 790) + screw(1190, 690) + '''
  </g>
  <text x="92" y="970" class="label" font-size="30" opacity=".72">透视效果：顶部织带挂点、侧边防撞块和橙色旋钮，让底座更像便携户外电子装备。</text>
</svg>'''
    return s


def rear_side_render():
    s = svg_header("户外机能风 iPhone StandBy 底座 - 背侧效果图")
    s += '''
  <g filter="url(#shadow)" transform="translate(0 55)">
    <path d="M440 285 H1110 Q1175 285 1190 350 L1268 670 Q1282 735 1220 750 H350 Q287 735 302 670 L380 350 Q395 285 440 285 Z" fill="#596259"/>
    <path d="M478 322 H1064 Q1112 322 1124 370 L1184 642 Q1198 694 1146 704 H396 Q344 694 358 642 L418 370 Q430 322 478 322 Z" fill="url(#cream)" stroke="#776f60" stroke-width="5"/>
    <path d="M442 363 H1100 L1068 596 H410 Z" fill="#bfb5a1" stroke="#877c69" stroke-width="5"/>
    <path d="M500 410 H992 Q1028 410 1038 444 L1064 540 Q1074 576 1038 576 H462 Q426 576 436 540 L462 444 Q472 410 500 410 Z" fill="#777f73" stroke="#384037" stroke-width="5"/>
    <path d="M512 432 H980 Q1002 432 1008 452 L1028 526 Q1034 548 1012 548 H482 Q460 548 466 526 L486 452 Q492 432 512 432 Z" fill="#485346"/>
    <path d="M520 455 H994 M510 505 H1004" class="line"/>
    <path d="M724 704 H836 V790 H724 Z" fill="#303638" stroke="#111" stroke-width="6"/>
    <path d="M670 790 H890 Q912 790 912 812 V842 H648 V812 Q648 790 670 790 Z" fill="#1c2022" stroke="#0c0f10" stroke-width="6"/>

    <path d="M390 245 C470 125 642 92 786 242" fill="none" stroke="url(#strap)" stroke-width="46" stroke-linecap="round"/>
    <path d="M790 242 C910 118 1075 124 1160 248" fill="none" stroke="url(#strap)" stroke-width="46" stroke-linecap="round"/>
    <rect x="536" y="132" width="130" height="62" rx="15" fill="#252a2b" stroke="#111" stroke-width="6" transform="rotate(15 601 163)"/>
    <rect x="938" y="135" width="130" height="62" rx="15" fill="#252a2b" stroke="#111" stroke-width="6" transform="rotate(-14 1003 166)"/>
    <rect x="410" y="240" width="108" height="60" rx="17" fill="#596b4c" stroke="#222" stroke-width="5"/>
    <rect x="1035" y="240" width="108" height="60" rx="17" fill="#6a7069" stroke="#222" stroke-width="5"/>

    <rect x="262" y="438" width="105" height="175" rx="28" fill="url(#blackRubber)" transform="rotate(7 315 526)"/>
    <path d="M286 475 H345 M282 522 H341 M278 569 H337" stroke="#41494c" stroke-width="11" stroke-linecap="round" transform="rotate(7 315 526)"/>
    <rect x="1160" y="438" width="105" height="175" rx="28" fill="url(#blackRubber)" transform="rotate(-7 1213 526)"/>
    <path d="M1184 475 H1243 M1188 522 H1247 M1192 569 H1251" stroke="#41494c" stroke-width="11" stroke-linecap="round" transform="rotate(-7 1213 526)"/>
    <rect x="515" y="650" width="530" height="36" rx="18" fill="#15191a"/>
    <path d="M560 668 H1000" stroke="#1ceaff" stroke-width="7" stroke-linecap="round" filter="url(#softGlow)"/>
    ''' + screw(455, 350) + screw(1105, 350) + screw(395, 675) + screw(1148, 675) + screw(545, 455) + screw(980, 455) + '''
  </g>
  <text x="92" y="970" class="label" font-size="30" opacity=".72">背侧结构：大面积背靠板、镂空减重筋、线缆出口和防滑底脚，适合 3D 打印后分色喷涂。</text>
</svg>'''
    return s


def scad():
    return '''// Tactical iPhone StandBy dock concept, units in mm.
// Designed as a printable shell: body, side armor, rear support, cable channel.

width = 190;
depth = 96;
body_h = 74;
slot_w = 38;
wall = 5;

module rounded_block(size=[10,10,10], r=4) {
  hull() {
    for (x=[r, size[0]-r])
      for (y=[r, size[1]-r])
        for (z=[r, size[2]-r])
          translate([x,y,z]) sphere(r=r, $fn=18);
  }
}

difference() {
  union() {
    translate([0,0,0]) rounded_block([depth,width,body_h], 8);
    translate([-8,0,4]) rounded_block([24,44,52], 7);
    translate([-8,width-44,4]) rounded_block([24,44,52], 7);
    translate([22,14,54]) rounded_block([58,width-28,16], 6);
    translate([6,0,0]) rounded_block([18,width,20], 5);
    translate([74,0,0]) rounded_block([22,width,58], 5);
  }

  // Phone pocket, landscape.
  translate([17,25,31]) rounded_block([20,140,38], 10);

  // Center cable gap.
  translate([-2,width/2-slot_w/2,-2]) cube([34,slot_w,32]);

  // Rear lightening cutout.
  translate([36,20,14]) rounded_block([14,width-40,26], 5);
}

// Print strap lugs separately or keep them in the same file.
translate([86,24,72]) rounded_block([14,34,12], 4);
translate([86,width-58,72]) rounded_block([14,34,12], 4);
'''


files = {
    "tactical_dock_effect_01_front.svg": front_render(),
    "tactical_dock_effect_02_perspective.svg": angled_render(),
    "tactical_dock_effect_03_back_side.svg": rear_side_render(),
    "tactical_iphone_dock.scad": scad(),
}

for name, content in files.items():
    (OUT / name).write_text(content, encoding="utf-8")

print(OUT.resolve())
