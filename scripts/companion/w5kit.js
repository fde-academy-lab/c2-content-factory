/* w5kit.js: the components every Week 5 day companion is built from.
 *
 * scripts/build_companion.py inlines this file, w5kit.css and the day's JSON into a page, so the
 * page stays one file that opens from disk with no network. Everything hangs off window.W5. The
 * manual is scripts/companion/W5KIT.md; the stress page that runs every component is
 * scripts/companion/demo/w5kit_demo_INTERNAL.html.
 *
 * Promises the kit keeps for every page built with it:
 *   - nothing animates on arrival, and every animation shows its end state under reduced motion;
 *   - every control writes its readout into the DOM before any animation starts;
 *   - no control is ever disabled; a control with nothing to do at that moment is hidden;
 *   - no storage, no network, no timers left running on a hidden route;
 *   - a page that breaks a rule of the skeleton logs "w5kit:" to the console as an error, which
 *     makes scripts/html_sweep.py fail, and shows the same line in red on the page.
 *
 * Icons are Lucide line icons (ISC licence), rendered from react-icons 5.7.0's lu set on
 * 29 October 2026 and pasted in as path data, the same family the deck draws its icons from.
 */
(function () {
  "use strict";
  /* The SVG namespace, an identifier rather than a link, built in two parts so no checker reads it as one. */
  var NS = "http:" + "//www.w3.org/2000/svg";
  var W5 = window.W5 = { version: "1.0.0" };

  var ICONS = {
    story: "<path d='M20.2 6 3 11l-.9-2.4c-.3-1.1.3-2.2 1.3-2.5l13.5-4c1.1-.3 2.2.3 2.5 1.3Z'></path><path d='m6.2 5.3 3.1 3.9'></path><path d='m12.4 3.4 3.1 4'></path><path d='M3 11h18v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Z'></path>",
    map: "<circle cx='12' cy='4.5' r='2.5'></circle><path d='m10.2 6.3-3.9 3.9'></path><circle cx='4.5' cy='12' r='2.5'></circle><path d='M7 12h10'></path><circle cx='19.5' cy='12' r='2.5'></circle><path d='m13.8 17.7 3.9-3.9'></path><circle cx='12' cy='19.5' r='2.5'></circle>",
    how: "<path d='M12 20a8 8 0 1 0 0-16 8 8 0 0 0 0 16Z'></path><path d='M12 14a2 2 0 1 0 0-4 2 2 0 0 0 0 4Z'></path><path d='M12 2v2'></path><path d='M12 22v-2'></path><path d='m17 20.66-1-1.73'></path><path d='M11 10.27 7 3.34'></path><path d='m20.66 17-1.73-1'></path><path d='m3.34 7 1.73 1'></path><path d='M14 12h8'></path><path d='M2 12h2'></path><path d='m20.66 7-1.73 1'></path><path d='m3.34 17 1.73-1'></path><path d='m17 3.34-1 1.73'></path><path d='m11 13.73-4 6.93'></path>",
    case: "<ellipse cx='12' cy='5' rx='9' ry='3'></ellipse><path d='M3 5V19A9 3 0 0 0 21 19V5'></path><path d='M3 12A9 3 0 0 0 21 12'></path>",
    field: "<path d='M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z'></path><path d='M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2'></path><path d='M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2'></path><path d='M10 6h4'></path><path d='M10 10h4'></path><path d='M10 14h4'></path><path d='M10 18h4'></path>",
    interview: "<path d='M14 9a2 2 0 0 1-2 2H6l-4 4V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2z'></path><path d='M18 9h2a2 2 0 0 1 2 2v11l-4-4h-6a2 2 0 0 1-2-2v-1'></path>",
    check: "<path d='m3 17 2 2 4-4'></path><path d='m3 7 2 2 4-4'></path><path d='M13 6h8'></path><path d='M13 12h8'></path><path d='M13 18h8'></path>",
    bank: "<line x1='3' x2='21' y1='22' y2='22'></line><line x1='6' x2='6' y1='18' y2='11'></line><line x1='10' x2='10' y1='18' y2='11'></line><line x1='14' x2='14' y1='18' y2='11'></line><line x1='18' x2='18' y1='18' y2='11'></line><polygon points='12 2 20 7 4 7'></polygon>",
    phone: "<path d='M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z'></path><path d='M14.05 2a9 9 0 0 1 8 7.94'></path><path d='M14.05 6A5 5 0 0 1 18 10'></path>",
    coin: "<circle cx='8' cy='8' r='6'></circle><path d='M18.09 10.37A6 6 0 1 1 10.34 18'></path><path d='M7 6h1v4'></path><path d='m16.71 13.88.7.71-2.82 2.82'></path>",
    ledger: "<path d='M12 7v14'></path><path d='M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3z'></path>",
    chart: "<path d='M3 3v16a2 2 0 0 0 2 2h16'></path><path d='m19 9-5 5-4-4-3 3'></path>",
    bars: "<path d='M3 3v16a2 2 0 0 0 2 2h16'></path><path d='M18 17V9'></path><path d='M13 17V5'></path><path d='M8 17v-3'></path>",
    tree: "<path d='M8 19a4 4 0 0 1-2.24-7.32A3.5 3.5 0 0 1 9 6.03V6a3 3 0 1 1 6 0v.04a3.5 3.5 0 0 1 3.24 5.65A4 4 0 0 1 16 19Z'></path><path d='M12 19v3'></path>",
    forest: "<path d='M10 10v.2A3 3 0 0 1 8.9 16H5a3 3 0 0 1-1-5.8V10a3 3 0 0 1 6 0Z'></path><path d='M7 16v6'></path><path d='M13 19v3'></path><path d='M12 19h8.3a1 1 0 0 0 .7-1.7L18 14h.3a1 1 0 0 0 .7-1.7L16 9h.2a1 1 0 0 0 .8-1.7L13 3l-1.4 1.5'></path>",
    shield: "<path d='M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z'></path>",
    clock: "<circle cx='12' cy='12' r='10'></circle><polyline points='12 6 12 12 16 14'></polyline>",
    magnifier: "<circle cx='11' cy='11' r='8'></circle><path d='m21 21-4.3-4.3'></path>",
    alarm: "<path d='M7 18v-6a5 5 0 1 1 10 0v6'></path><path d='M5 21a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-1a2 2 0 0 0-2-2H7a2 2 0 0 0-2 2z'></path><path d='M21 12h1'></path><path d='M18.5 4.5 18 5'></path><path d='M2 12h1'></path><path d='M12 2v1'></path><path d='m4.929 4.929.707.707'></path><path d='M12 12v6'></path>",
    owner: "<path d='M16 20V4a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16'></path><rect width='20' height='14' x='2' y='6' rx='2'></rect>",
    pm: "<rect width='8' height='4' x='8' y='2' rx='1' ry='1'></rect><path d='M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2'></path><path d='M12 11h4'></path><path d='M12 16h4'></path><path d='M8 11h.01'></path><path d='M8 16h.01'></path>",
    architect: "<path d='m12.99 6.74 1.93 3.44'></path><path d='M19.136 12a10 10 0 0 1-14.271 0'></path><path d='m21 21-2.16-3.84'></path><path d='m3 21 8.02-14.26'></path><circle cx='12' cy='5' r='2'></circle>",
    ml: "<path d='M12 5a3 3 0 1 0-5.997.125 4 4 0 0 0-2.526 5.77 4 4 0 0 0 .556 6.588A4 4 0 1 0 12 18Z'></path><path d='M12 5a3 3 0 1 1 5.997.125 4 4 0 0 1 2.526 5.77 4 4 0 0 1-.556 6.588A4 4 0 1 1 12 18Z'></path><path d='M15 13a4.5 4.5 0 0 1-3-4 4.5 4.5 0 0 1-3 4'></path><path d='M17.599 6.5a3 3 0 0 0 .399-1.375'></path><path d='M6.003 5.125A3 3 0 0 0 6.401 6.5'></path><path d='M3.477 10.896a4 4 0 0 1 .585-.396'></path><path d='M19.938 10.5a4 4 0 0 1 .585.396'></path><path d='M6 18a4 4 0 0 1-1.967-.516'></path><path d='M19.967 17.484A4 4 0 0 1 18 18'></path>",
    implementation: "<path d='M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z'></path>",
    qa: "<path d='M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z'></path><path d='m9 12 2 2 4-4'></path>",
    memo: "<path d='M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z'></path><path d='M14 2v4a2 2 0 0 0 2 2h4'></path><path d='M10 9H8'></path><path d='M16 13H8'></path><path d='M16 17H8'></path>",
    envelope: "<rect width='20' height='16' x='2' y='4' rx='2'></rect><path d='m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7'></path>",
    lock: "<rect width='18' height='11' x='3' y='11' rx='2' ry='2'></rect><path d='M7 11V7a5 5 0 0 1 10 0v4'></path>",
    play: "<polygon points='6 3 20 12 6 21 6 3'></polygon>",
    pause: "<rect x='14' y='4' width='4' height='16' rx='1'></rect><rect x='6' y='4' width='4' height='16' rx='1'></rect>",
    next: "<polygon points='5 4 15 12 5 20 5 4'></polygon><line x1='19' x2='19' y1='5' y2='19'></line>",
    prev: "<polygon points='19 20 9 12 19 4 19 20'></polygon><line x1='5' x2='5' y1='19' y2='5'></line>",
    chevronLeft: "<path d='m15 18-6-6 6-6'></path>",
    chevronRight: "<path d='m9 18 6-6-6-6'></path>",
    replay: "<path d='M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8'></path><path d='M3 3v5h5'></path>",
    presenter: "<path d='M2 3h20'></path><path d='M21 3v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V3'></path><path d='m7 21 5-5 5 5'></path>",
    tick: "<path d='M20 6 9 17l-5-5'></path>",
    cross: "<path d='M18 6 6 18'></path><path d='m6 6 12 12'></path>",
    arrowRight: "<path d='M5 12h14'></path><path d='m12 5 7 7-7 7'></path>",
    arrowDown: "<path d='M12 5v14'></path><path d='m19 12-7 7-7-7'></path>",
    arrowUp: "<path d='m5 12 7-7 7 7'></path><path d='M12 19V5'></path>",
    rule: "<path d='M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5'></path><path d='M9 18h6'></path><path d='M10 22h4'></path>",
    target: "<circle cx='12' cy='12' r='10'></circle><circle cx='12' cy='12' r='6'></circle><circle cx='12' cy='12' r='2'></circle>",
    eye: "<path d='M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0'></path><circle cx='12' cy='12' r='3'></circle>",
    users: "<path d='M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2'></path><circle cx='9' cy='7' r='4'></circle><path d='M22 21v-2a4 4 0 0 0-3-3.87'></path><path d='M16 3.13a4 4 0 0 1 0 7.75'></path>",
    calendar: "<path d='M8 2v4'></path><path d='M16 2v4'></path><rect width='18' height='18' x='3' y='4' rx='2'></rect><path d='M3 10h18'></path>",
    scale: "<path d='m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z'></path><path d='m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z'></path><path d='M7 21h10'></path><path d='M12 3v18'></path><path d='M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2'></path>",
    sliders: "<line x1='21' x2='14' y1='4' y2='4'></line><line x1='10' x2='3' y1='4' y2='4'></line><line x1='21' x2='12' y1='12' y2='12'></line><line x1='8' x2='3' y1='12' y2='12'></line><line x1='21' x2='16' y1='20' y2='20'></line><line x1='12' x2='3' y1='20' y2='20'></line><line x1='14' x2='14' y1='2' y2='6'></line><line x1='8' x2='8' y1='10' y2='14'></line><line x1='16' x2='16' y1='18' y2='22'></line>",
    trendDown: "<polyline points='22 17 13.5 8.5 8.5 13.5 2 7'></polyline><polyline points='16 17 22 17 22 11'></polyline>",
    trendUp: "<polyline points='22 7 13.5 15.5 8.5 10.5 2 17'></polyline><polyline points='16 7 22 7 22 13'></polyline>",
    flag: "<path d='M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z'></path><line x1='4' x2='4' y1='22' y2='15'></line>",
    gauge: "<path d='m12 14 4-4'></path><path d='M3.34 19a10 10 0 1 1 17.32 0'></path>",
    grip: "<circle cx='9' cy='12' r='1'></circle><circle cx='9' cy='5' r='1'></circle><circle cx='9' cy='19' r='1'></circle><circle cx='15' cy='12' r='1'></circle><circle cx='15' cy='5' r='1'></circle><circle cx='15' cy='19' r='1'></circle>",
    shuffle: "<path d='m18 14 4 4-4 4'></path><path d='m18 2 4 4-4 4'></path><path d='M2 18h1.973a4 4 0 0 0 3.3-1.7l5.454-8.6a4 4 0 0 1 3.3-1.7H22'></path><path d='M2 6h1.972a4 4 0 0 1 3.6 2.2'></path><path d='M22 18h-6.041a4 4 0 0 1-3.3-1.8l-.359-.45'></path>",
    split: "<path d='M16 3h5v5'></path><path d='M8 3H3v5'></path><path d='M12 22v-8.3a4 4 0 0 0-1.172-2.872L3 3'></path><path d='m15 9 6-6'></path>",
    layers: "<path d='m12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83Z'></path><path d='m22 17.65-9.17 4.16a2 2 0 0 1-1.66 0L2 17.65'></path><path d='m22 12.65-9.17 4.16a2 2 0 0 1-1.66 0L2 12.65'></path>",
    table: "<path d='M9 3H5a2 2 0 0 0-2 2v4m6-6h10a2 2 0 0 1 2 2v4M9 3v18m0 0h10a2 2 0 0 0 2-2V9M9 21H5a2 2 0 0 1-2-2V9m0 0h18'></path>",
    quote: "<path d='M16 3a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2 1 1 0 0 1 1 1v1a2 2 0 0 1-2 2 1 1 0 0 0-1 1v2a1 1 0 0 0 1 1 6 6 0 0 0 6-6V5a2 2 0 0 0-2-2z'></path><path d='M5 3a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2 1 1 0 0 1 1 1v1a2 2 0 0 1-2 2 1 1 0 0 0-1 1v2a1 1 0 0 0 1 1 6 6 0 0 0 6-6V5a2 2 0 0 0-2-2z'></path>",
    alert: "<path d='m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3'></path><path d='M12 9v4'></path><path d='M12 17h.01'></path>",
    person: "<path d='M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2'></path><circle cx='12' cy='7' r='4'></circle>",
    cart: "<circle cx='8' cy='21' r='1'></circle><circle cx='19' cy='21' r='1'></circle><path d='M2.05 2.05h2l2.66 12.42a2 2 0 0 0 2 1.58h9.78a2 2 0 0 0 1.95-1.57l1.65-7.43H5.12'></path>",
    store: "<path d='m2 7 4.41-4.41A2 2 0 0 1 7.83 2h8.34a2 2 0 0 1 1.42.59L22 7'></path><path d='M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8'></path><path d='M15 22v-4a2 2 0 0 0-2-2h-2a2 2 0 0 0-2 2v4'></path><path d='M2 7h20'></path><path d='M22 7v3a2 2 0 0 1-2 2a2.7 2.7 0 0 1-1.59-.63.7.7 0 0 0-.82 0A2.7 2.7 0 0 1 16 12a2.7 2.7 0 0 1-1.59-.63.7.7 0 0 0-.82 0A2.7 2.7 0 0 1 12 12a2.7 2.7 0 0 1-1.59-.63.7.7 0 0 0-.82 0A2.7 2.7 0 0 1 8 12a2.7 2.7 0 0 1-1.59-.63.7.7 0 0 0-.82 0A2.7 2.7 0 0 1 4 12a2 2 0 0 1-2-2V7'></path>",
    truck: "<path d='M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2'></path><path d='M15 18H9'></path><path d='M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.624l-3.48-4.35A1 1 0 0 0 17.52 8H14'></path><circle cx='17' cy='18' r='2'></circle><circle cx='7' cy='18' r='2'></circle>",
    heart: "<path d='M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z'></path><path d='M3.22 12H9.5l.5-1 2 4.5 2-7 1.5 3.5h5.27'></path>",
    card: "<rect width='20' height='14' x='2' y='5' rx='2'></rect><line x1='2' x2='22' y1='10' y2='10'></line>",
    home: "<path d='M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8'></path><path d='M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z'></path>",
    filter: "<polygon points='22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3'></polygon>",
    minus: "<path d='M5 12h14'></path>"
  };

  /* ================================================================ small helpers */
  function h(tag, attrs, kids) {
    var node = document.createElement(tag);
    setAttrs(node, attrs);
    addKids(node, kids);
    return node;
  }
  function s(tag, attrs, kids) {
    var node = document.createElementNS(NS, tag);
    setAttrs(node, attrs);
    addKids(node, kids);
    return node;
  }
  function setAttrs(node, attrs) {
    if (!attrs) return;
    Object.keys(attrs).forEach(function (k) {
      var v = attrs[k];
      if (v === undefined || v === null || v === false) return;
      if (k === "text") node.textContent = v;
      else if (k === "rich") node.appendChild(rich(v));
      else if (k === "on") Object.keys(v).forEach(function (ev) { node.addEventListener(ev, v[ev]); });
      else if (k === "style" && typeof v === "object") Object.keys(v).forEach(function (p) { node.style[p] = v[p]; });
      else node.setAttribute(k, v === true ? "" : v);
    });
  }
  function addKids(node, kids) {
    if (kids === undefined || kids === null) return;
    (Array.isArray(kids) ? kids : [kids]).forEach(function (k) {
      if (k === null || k === undefined || k === false) return;
      node.appendChild(typeof k === "string" || typeof k === "number" ? document.createTextNode(String(k)) : k);
    });
  }
  /* Authored text may carry **bold**; nothing else is read as markup, so data can never inject HTML. */
  function rich(text) {
    var frag = document.createDocumentFragment();
    String(text === undefined ? "" : text).split(/(\*\*[^*]+\*\*)/).forEach(function (part) {
      if (/^\*\*[^*]+\*\*$/.test(part)) frag.appendChild(h("b", { text: part.slice(2, -2) }));
      else if (part) frag.appendChild(document.createTextNode(part));
    });
    return frag;
  }
  function setRich(node, text) { node.textContent = ""; node.appendChild(rich(text)); }
  function icon(name, cls) {
    var svg = s("svg", { viewBox: "0 0 24 24", "class": "w5-ico" + (cls ? " " + cls : ""), "aria-hidden": "true", focusable: "false" });
    svg.innerHTML = ICONS[name] || ICONS.target;
    return svg;
  }
  function clamp(v, a, b) { return Math.max(a, Math.min(b, v)); }
  function lerp(a, b, t) { return a + (b - a) * t; }
  function ease(t) { return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; }
  function rootPx() { return parseFloat(getComputedStyle(document.documentElement).fontSize) || 17; }
  function off(node, yes) { if (yes) node.setAttribute("data-off", ""); else node.removeAttribute("data-off"); }
  function seeded(seed) {
    var a = seed >>> 0 || 1;
    return function () {
      a = (a + 0x6D2B79F5) >>> 0;
      var t = a;
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  W5.h = h; W5.s = s; W5.icon = icon; W5.rich = rich; W5.clamp = clamp; W5.lerp = lerp; W5.ease = ease;
  W5.seeded = seeded; W5.icons = Object.keys(ICONS);

  W5.reduced = function () {
    return !!(window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches);
  };

  /* ================================================================ numbers in words */
  function group(n) {
    var neg = n < 0, str = String(Math.round(Math.abs(n)));
    return (neg ? "−" : "") + str.replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  }
  W5.fmt = {
    int: group,
    dp: function (n, d) { var t = Number(n).toFixed(d === undefined ? 2 : d); return t.charAt(0) === "-" ? "−" + t.slice(1) : t; },
    pct: function (x, d) { return (x * 100).toFixed(d === undefined ? 1 : d) + "%"; },
    share: function (k, n, d) { return group(k) + " of " + group(n) + (n ? " (" + (k / n * 100).toFixed(d === undefined ? 1 : d) + "%)" : ""); },
    rs: function (n) { return "Rs " + group(n); },
    signed: function (n, d) { var t = Math.abs(n).toFixed(d === undefined ? 2 : d); return (n > 0 ? "+" : n < 0 ? "−" : "") + t; }
  };

  /* ================================================================ the lint line */
  var lintBox = null;
  function lint(msg) {
    console.error("w5kit: " + msg);
    var main = document.querySelector("[data-w5-main]") || document.body;
    if (!lintBox) { lintBox = h("div", { "class": "w5-lint", role: "alert" }); main.insertBefore(lintBox, main.firstChild); }
    lintBox.appendChild(h("div", { text: "Kit check: " + msg }));
  }
  W5.lint = lint;

  /* ================================================================ motion */
  var live = [];
  function tween(ms, fn, done) {
    if (W5.reduced() || !(ms > 0)) { fn(1, 1); if (done) done(); return { cancel: function () {}, finish: function () {} }; }
    var t0 = performance.now(), id = 0, on = true, handle;
    function frame(now) {
      if (!on) return;
      var p = Math.min(1, (now - t0) / ms);
      fn(ease(p), p);
      if (p < 1) id = requestAnimationFrame(frame);
      else stop(true);
    }
    function stop(ran) {
      if (!on) return;
      on = false; cancelAnimationFrame(id);
      var i = live.indexOf(handle); if (i >= 0) live.splice(i, 1);
      if (ran && done) done();
    }
    handle = {
      cancel: function () { stop(false); },
      finish: function () { if (on) { fn(1, 1); stop(true); } }
    };
    live.push(handle);
    id = requestAnimationFrame(frame);
    return handle;
  }
  W5.tween = tween;
  function finishAll() { live.slice().forEach(function (t) { t.finish(); }); }

  /* ================================================================ layout registry */
  var layouts = [];
  function onLayout(el, fn) {
    var rec = { el: el, fn: fn, w: -1 };
    layouts.push(rec);
    if (window.ResizeObserver) {
      new ResizeObserver(function () {
        var w = el.clientWidth;
        if (w > 0 && Math.abs(w - rec.w) > 0.5) { rec.w = w; fn(w); }
      }).observe(el);
    }
    var w0 = el.clientWidth;
    if (w0 > 0) { rec.w = w0; fn(w0); }
    return rec;
  }
  function relayout(scope, force) {
    layouts.forEach(function (rec) {
      if (scope && !scope.contains(rec.el)) return;
      var w = rec.el.clientWidth;
      if (w > 0 && (force || Math.abs(w - rec.w) > 0.5)) { rec.w = w; rec.fn(w); }
    });
  }
  W5.onLayout = onLayout;
  W5.relayout = relayout;

  /* ================================================================ the data block */
  var dataCache = null;
  function readData() {
    if (dataCache) return dataCache;
    var tag = document.querySelector("script[type='application/json'][data-w5data]");
    if (!tag) { dataCache = {}; return dataCache; }
    var text = tag.textContent.trim();
    if (!text) { lint("the data block is empty; run python3 scripts/build_companion.py on this page"); dataCache = {}; return dataCache; }
    try { dataCache = JSON.parse(text); }
    catch (e) { lint("the data block is not valid JSON (" + e.message + ")"); dataCache = {}; }
    return dataCache;
  }
  Object.defineProperty(W5, "data", { get: readData });
  W5.get = function (path) {
    var cur = readData(), parts = String(path).split(".");
    for (var i = 0; i < parts.length; i++) {
      if (cur === null || typeof cur !== "object" || !(parts[i] in cur)) { lint("the data block has no value at '" + path + "'"); return undefined; }
      cur = cur[parts[i]];
    }
    return cur;
  };

  /* ================================================================ the app shell and the router */
  var ROUTE_META = {
    story: { label: "The story", icon: "story" },
    map: { label: "The map", icon: "map" },
    "case": { label: "The case", icon: "case" },
    field: { label: "In the field", icon: "field" },
    interview: { label: "Interview room", icon: "interview" },
    check: { label: "Check yourself", icon: "check" }
  };
  var ROUTE_ORDER = ["story", "map", "p", "case", "field", "interview", "check"];
  var app = { routes: [], byId: {}, current: null, seen: {}, players: [], active: null };
  W5._app = app;

  function routeKind(id) { return /^p[1-9]$/.test(id) ? "p" : id; }

  W5.app = function (cfg) {
    cfg = cfg || {};
    var main = document.querySelector("[data-w5-main]");
    if (!main) { main = document.querySelector("main"); if (main) main.setAttribute("data-w5-main", ""); }
    if (!main) { lint("the page has no <main data-w5-main> holding its sections"); return; }
    document.body.classList.add("w5");
    main.classList.add("w5-main");
    var sections = Array.prototype.slice.call(main.querySelectorAll("section[data-route]"));
    var lastKind = -1;
    sections.forEach(function (sec) {
      var id = sec.getAttribute("data-route"), kind = routeKind(id), order = ROUTE_ORDER.indexOf(kind);
      if (order < 0) { lint("unknown route '" + id + "'; the routes are story, map, p1 to p9, case, field, interview and check"); return; }
      if (app.byId[id]) { lint("route '" + id + "' appears twice"); return; }
      if (order < lastKind) lint("route '" + id + "' is out of the skeleton's order (story, map, p1 to pn, case, field, interview, check)");
      lastKind = order;
      var meta = ROUTE_META[id] || { label: sec.getAttribute("data-nav") || ("How it works " + id.slice(1)), icon: "how" };
      if (kind === "p" && !sec.getAttribute("data-nav")) lint("section " + id + " needs a short data-nav label naming its subtopic");
      sec.classList.add("w5-route");
      sec.setAttribute("tabindex", "-1");
      var r = { id: id, kind: kind, el: sec, label: meta.label, icon: meta.icon, num: kind === "p" ? id.slice(1) : "" };
      app.routes.push(r); app.byId[id] = r;
    });
    ["story", "map", "p1", "case", "field", "interview", "check"].forEach(function (need) {
      if (!app.byId[need]) lint("the skeleton's route '" + need + "' is missing");
    });

    /* the top bar */
    var top = h("header", { "class": "w5-top", "data-w5-shell": "" }, [
      h("div", { "class": "w5-day", text: (cfg.week ? "Week " + cfg.week + " · " : "") + (cfg.day || "") }),
      h("p", { "class": "w5-q", text: cfg.question || "" })
    ]);
    var pres = h("button", { type: "button", "class": "w5-tbtn", "aria-pressed": "false", title: "Presenter mode enlarges the type (key P)" },
      [icon("presenter"), h("span", { "class": "w5-tlabel", text: "Presenter" })]);
    pres.addEventListener("click", function () { setPresenter(!document.documentElement.classList.contains("w5-present")); });
    top.appendChild(pres);
    app.presBtn = pres;

    /* the nav */
    var nav = h("nav", { "class": "w5-nav", "data-w5-nav": "", "data-w5-shell": "", "aria-label": "Pages of this companion" });
    var grouped = false;
    app.routes.forEach(function (r) {
      if (r.kind === "p" && !grouped) { nav.appendChild(h("div", { "class": "w5-navgroup", text: "How it works" })); grouped = true; }
      var kids = r.kind === "p" ? [h("span", { "class": "w5-navnum", text: r.num })] : [icon(r.icon)];
      kids.push(h("span", { "class": "w5-navtext", text: r.label }), h("span", { "class": "w5-seen", "aria-hidden": "true" }));
      r.link = h("a", { "class": "w5-navlink", href: "#" + r.id, title: r.label }, kids);
      nav.appendChild(r.link);
    });

    /* the progress rail */
    var dots = h("div", { "class": "w5-dots", "aria-hidden": "true" });
    app.routes.forEach(function (r) { r.dot = h("span", { "class": "w5-dot", title: r.label }); dots.appendChild(r.dot); });
    app.progress = h("p", { "class": "w5-progress", "aria-live": "polite" });
    app.prevBtn = h("button", { type: "button", "class": "w5-pnbtn prev" }, [icon("chevronLeft"), h("span", { text: "Previous" })]);
    app.nextBtn = h("button", { type: "button", "class": "w5-pnbtn next" }, [h("span", { text: "Next" }), icon("chevronRight")]);
    app.prevBtn.addEventListener("click", function () { goRel(-1); });
    app.nextBtn.addEventListener("click", function () { goRel(1); });
    var rail = h("div", { "class": "w5-rail", "data-w5-shell": "" }, [app.progress, dots, h("div", { "class": "w5-pn" }, [app.prevBtn, app.nextBtn])]);
    var keys = h("p", { "class": "w5-keys", text: "Keys: left and right arrows step the animation you last used, or the page; shift with an arrow always turns the page; 1 to 9 jump to a page; P is presenter mode." });
    var side = h("aside", { "class": "w5-side" }, [nav, rail, keys]);
    var shell = h("div", { "class": "w5-shell" });
    main.parentNode.insertBefore(top, main);
    main.parentNode.insertBefore(shell, main);
    shell.appendChild(side);
    shell.appendChild(main);
    app.main = main;

    window.addEventListener("hashchange", function () { go(location.hash.slice(1)); });
    document.addEventListener("keydown", onKey);
    var start = location.hash.slice(1);
    go(app.byId[start] ? start : (app.routes[0] && app.routes[0].id), true);
    return app;
  };

  function setPresenter(on) {
    document.documentElement.classList.toggle("w5-present", on);
    if (app.presBtn) app.presBtn.setAttribute("aria-pressed", on ? "true" : "false");
    relayout(app.current && app.current.el, true);
  }
  W5.presenter = setPresenter;

  function go(id, first) {
    var r = app.byId[id] || app.routes[0];
    if (!r) return;
    if (app.current === r && !first) return;
    app.players.forEach(function (p) { p.pause(); });
    app.active = null;
    app.routes.forEach(function (x) {
      var on = x === r;
      x.el.hidden = !on;
      if (on) x.link.setAttribute("aria-current", "page"); else x.link.removeAttribute("aria-current");
    });
    app.current = r;
    app.seen[r.id] = true;
    var idx = app.routes.indexOf(r), n = app.routes.length, seenCount = 0;
    app.routes.forEach(function (x) {
      var seen = !!app.seen[x.id];
      if (seen) seenCount++;
      x.link.classList.toggle("seen", seen);
      x.dot.classList.toggle("seen", seen);
      x.dot.classList.toggle("here", x === r);
    });
    app.progress.textContent = "Page " + (idx + 1) + " of " + n + ", " + r.label + ". You have opened " + seenCount + " of " + n + ".";
    var prev = app.routes[idx - 1], next = app.routes[idx + 1];
    off(app.prevBtn, !prev); off(app.nextBtn, !next);
    app.prevBtn.title = prev ? "Previous: " + prev.label : "";
    app.nextBtn.title = next ? "Next: " + next.label : "";
    if (!first) window.scrollTo(0, 0);
    if (location.hash.slice(1) !== r.id) {
      if (history.replaceState) history.replaceState(null, "", "#" + r.id); else location.hash = r.id;
    }
    relayout(r.el);
    if (r.link.scrollIntoView && window.innerWidth <= 760) {
      var navEl = r.link.parentNode, left = r.link.offsetLeft - 16;
      navEl.scrollLeft = left;
    }
  }
  function goRel(d) {
    var idx = app.routes.indexOf(app.current), next = app.routes[idx + d];
    if (next) location.hash = next.id;
  }
  W5.go = function (id) { location.hash = id; };

  function onKey(e) {
    if (e.defaultPrevented || e.altKey || e.ctrlKey || e.metaKey) return;
    var t = e.target, tag = t && t.tagName ? t.tagName.toLowerCase() : "";
    if (tag === "input" || tag === "textarea" || tag === "select" || (t && t.isContentEditable)) return;
    if (e.key === "ArrowRight" || e.key === "ArrowLeft") {
      var d = e.key === "ArrowRight" ? 1 : -1;
      var p = app.active;
      if (!e.shiftKey && p && app.current && app.current.el.contains(p.el) && p.el.offsetParent !== null) { p.step(d); }
      else goRel(d);
      e.preventDefault();
    } else if (/^[0-9]$/.test(e.key)) {
      var n = e.key === "0" ? 10 : Number(e.key), r = app.routes[n - 1];
      if (r) { location.hash = r.id; e.preventDefault(); }
    } else if (e.key === "p" || e.key === "P") {
      setPresenter(!document.documentElement.classList.contains("w5-present"));
    }
  }

  /* ================================================================ controls */
  function ack(node, text) { node.textContent = text; }

  W5.button = function (container, o) {
    var b = h("button", { type: "button", "class": "w5-btn" + (o.primary ? " primary" : o.quiet ? " quiet" : ""), title: o.title },
      [o.icon ? icon(o.icon) : null, o.label ? h("span", { text: o.label }) : null]);
    b.addEventListener("click", function (e) { o.onClick && o.onClick(e, b); });
    if (container) container.appendChild(b);
    return b;
  };

  var sliderSeq = 0;
  W5.slider = function (container, o) {
    var id = o.id || ("w5s" + (++sliderSeq));
    var fmt = o.fmt || function (v) { return String(v); };
    var input = h("input", { type: "range", id: id, min: o.min, max: o.max, step: o.step || 1, value: o.value });
    var out = h("output", { "for": id, text: fmt(Number(o.value)) });
    var wrap = h("div", { "class": "w5-slider" }, [h("label", { "for": id, text: o.label }), input, out]);
    var api = {
      el: wrap, input: input,
      get value() { return Number(input.value); },
      set: function (v, silent) { input.value = v; out.textContent = fmt(Number(input.value)); if (!silent && o.onInput) o.onInput(Number(input.value), api); }
    };
    input.addEventListener("input", function () {
      out.textContent = fmt(Number(input.value));
      if (o.onInput) o.onInput(Number(input.value), api);
    });
    if (container) container.appendChild(wrap);
    return api;
  };

  W5.toggle = function (container, o) {
    var value = o.value !== undefined ? o.value : o.options[0].value;
    var seg = h("div", { "class": "w5-seg", role: "group", "aria-label": o.label || "Choose one" });
    var note = h("span", { "class": "w5-pstate", style: { margin: "0" }, "aria-live": "polite" });
    var btns = o.options.map(function (opt) {
      var b = h("button", { type: "button", "aria-pressed": opt.value === value ? "true" : "false", text: opt.label });
      b.addEventListener("click", function () {
        if (opt.value === value) { ack(note, opt.label + " is already showing."); return; }
        value = opt.value;
        btns.forEach(function (x, i) { x.setAttribute("aria-pressed", o.options[i].value === value ? "true" : "false"); });
        ack(note, "Showing " + opt.label + ".");
        if (o.onChange) o.onChange(value);
      });
      seg.appendChild(b);
      return b;
    });
    var wrap = h("div", { "class": "w5-numrow" }, [o.label ? h("span", { "class": "w5-unit", text: o.label }) : null, seg, note]);
    if (container) container.appendChild(wrap);
    return { el: wrap, get value() { return value; } };
  };

  /* ================================================================ the readout panel */
  function Readout(el) {
    this.el = el;
    this.list = h("div", { "class": "w5-ritems" });
    this.sayEl = h("p", { "class": "w5-rsay", "aria-live": "polite" });
    el.appendChild(this.list); el.appendChild(this.sayEl);
  }
  Readout.prototype.set = function (items, say) {
    var list = this.list;
    list.textContent = "";
    (items || []).forEach(function (it) {
      list.appendChild(h("div", { "class": "w5-ritem" + (it.tone ? " " + it.tone : "") }, [
        h("span", { "class": "w5-rv", text: it.value }),
        h("span", { "class": "w5-rl", rich: it.label }),
        it.sub ? h("span", { "class": "w5-rs", rich: it.sub }) : null
      ]));
    });
    if (say !== undefined) setRich(this.sayEl, say);
  };
  Readout.prototype.say = function (text) { setRich(this.sayEl, text); };
  W5.readout = function (container, o) {
    var card = h("div", { "class": "w5-card w5-readout" }, [h("div", { "class": "w5-label" }, [icon("gauge"), (o && o.title) || "What the numbers say"])]);
    container.appendChild(card);
    var r = new Readout(card);
    if (o && o.items) r.set(o.items, o.say);
    return r;
  };

  /* ================================================================ the prediction card */
  W5.predict = function (container, o) {
    var type = o.type || (o.options ? "choice" : "number");
    var card = h("div", { "class": "w5-card w5-predict" });
    card.appendChild(h("div", { "class": "w5-label" }, [icon("target"), o.title || "Predict first"]));
    card.appendChild(h("p", { "class": "w5-pq", rich: o.q }));
    var state = { pick: null, committed: false, revealed: false, tries: 0 };
    var pstate = h("p", { "class": "w5-pstate", "aria-live": "polite", text: "No prediction yet." });
    var optBtns = [], input = null;
    var opts = o.options;
    if (type === "direction") opts = opts || ["It goes up", "It goes down", "It stays the same"];
    if (type === "choice" || type === "direction") {
      var box = h("div", { "class": type === "direction" ? "w5-dirs" : "w5-opts" });
      opts.forEach(function (text, i) {
        var key = type === "direction" ? icon(["trendUp", "trendDown", "minus"][i] || "target") : h("span", { "class": "w5-optkey", text: String.fromCharCode(65 + i) });
        var b = h("button", { type: "button", "class": "w5-opt", "aria-pressed": "false" }, [key, h("span", { rich: text })]);
        b.addEventListener("click", function () {
          state.pick = i;
          optBtns.forEach(function (x, j) { x.setAttribute("aria-pressed", j === i ? "true" : "false"); });
          pstate.textContent = state.revealed ? "You changed your pick to " + label(i) + ". Commit again to score it." : "You picked " + label(i) + ". Commit it to see the answer.";
        });
        optBtns.push(b); box.appendChild(b);
      });
      card.appendChild(box);
    } else {
      input = h("input", { type: "number", step: o.step || "any", "aria-label": "Your prediction", inputmode: "decimal" });
      if (o.min !== undefined) input.min = o.min;
      if (o.max !== undefined) input.max = o.max;
      input.addEventListener("input", function () {
        state.pick = input.value === "" ? null : Number(input.value);
        pstate.textContent = state.pick === null ? "No prediction yet." : "Your guess: " + fmtN(state.pick) + (o.unit ? " " + o.unit : "") + ". Commit it to see the answer.";
      });
      card.appendChild(h("div", { "class": "w5-numrow" }, [input, o.unit ? h("span", { "class": "w5-unit", text: o.unit }) : null]));
    }
    function fmtN(v) { return o.fmt ? o.fmt(v) : String(v); }
    function label(i) { return type === "direction" ? "“" + opts[i] + "”" : String.fromCharCode(65 + i); }
    var commit = h("button", { type: "button", "class": "w5-btn primary" }, [icon("tick"), h("span", { text: "Commit my prediction" })]);
    var show = h("button", { type: "button", "class": "w5-btn quiet" }, [icon("eye"), h("span", { text: o.skipLabel || "Show me without predicting" })]);
    card.appendChild(h("div", { "class": "w5-pbtns" }, [commit, show]));
    card.appendChild(pstate);
    var rev = h("div", { "class": "w5-reveal", hidden: true });
    card.appendChild(rev);

    function verdict() {
      if (state.pick === null || !state.committed) return { cls: "none", text: o.noneText || "You revealed it without a prediction, so there is nothing to score. Read the answer and its reason below." };
      var right;
      if (type === "number") {
        var tol = o.tolerance !== undefined ? o.tolerance : Math.abs(o.answer) * 0.1;
        var gap = state.pick - o.answer;
        right = Math.abs(gap) <= tol;
        var near = right ? "close enough to count" : (gap > 0 ? fmtN(Math.abs(gap)) + " too high" : fmtN(Math.abs(gap)) + " too low");
        return { cls: right ? "right" : "wrong", text: "Your " + fmtN(state.pick) + " is " + near + "; the answer is " + fmtN(o.answer) + (o.unit ? " " + o.unit : "") + "." };
      }
      right = state.pick === o.answer;
      return { cls: right ? "right" : "wrong", text: (right ? "You called it: " : "Not this time: you picked " + label(state.pick) + " and the answer is ") + label(o.answer) + "." };
    }
    function reveal() {
      state.revealed = true; state.tries++;
      var v = verdict();
      rev.hidden = false; rev.textContent = "";
      rev.appendChild(h("p", { "class": "w5-verdict " + v.cls }, [icon(v.cls === "right" ? "tick" : v.cls === "wrong" ? "cross" : "eye"), h("span", { text: v.text })]));
      if (o.why) rev.appendChild(h("p", { rich: o.why }));
      optBtns.forEach(function (b, j) {
        b.classList.toggle("right", j === o.answer);
        b.classList.toggle("wrong", state.committed && j === state.pick && j !== o.answer);
      });
      show.hidden = true;
      commit.lastChild.textContent = "Commit again";
      if (o.onReveal) o.onReveal({ committed: state.committed, pick: state.pick, right: v.cls === "right" });
    }
    commit.addEventListener("click", function () {
      if (state.pick === null) { pstate.textContent = type === "number" ? "Type a number first, or press Show me." : "Pick an option first, or press Show me."; return; }
      state.committed = true;
      pstate.textContent = "Committed: " + (type === "number" ? fmtN(state.pick) + (o.unit ? " " + o.unit : "") : label(state.pick)) + (state.tries ? " (try " + (state.tries + 1) + ")." : ".");
      reveal();
    });
    show.addEventListener("click", function () {
      pstate.textContent = "Revealed without a prediction.";
      reveal();
    });
    container.appendChild(card);
    var api = { el: card, state: state, reveal: function () { if (!state.revealed) { pstate.textContent = "Revealed without a prediction."; reveal(); } } };
    revealers.push(api);
    return api;
  };
  var revealers = [];

  /* ================================================================ the rule card and the footer */
  W5.rule = function (container, o) {
    if (!o || !o.text) lint("a rule card has no rule");
    if (!o || !o.flips) lint("the rule '" + ((o && o.text) || "").slice(0, 40) + "' has no 'flips when' line");
    var card = h("div", { "class": "w5-card w5-rule" }, [
      h("div", { "class": "w5-ruleico" }, [icon("rule")]),
      h("p", { "class": "w5-ruletext", rich: (o && o.text) || "" }),
      h("p", { "class": "w5-flips" }, [h("b", { text: "It flips when " }), rich(((o && o.flips) || "").replace(/^it flips when\s*/i, ""))])
    ]);
    container.appendChild(card);
    return card;
  };
  W5.where = function (container, o) {
    var row = h("div", { "class": "w5-where" }, [
      h("span", {}, [h("b", { text: "Where you met it: " }), rich(o.deck || "")]),
      o.notebook ? h("span", {}, [h("b", { text: "Notebook: " }), h("code", { text: o.notebook })]) : null
    ]);
    container.appendChild(row);
    return row;
  };

  /* ================================================================ the player */
  function Player(container, o) {
    var self = this;
    this.o = o;
    this.frames = o.frames || [];
    this.n = this.frames.length;
    this.i = 0;
    this.playing = false;
    this.el = h("div", { "class": "w5-player" });
    this.stage = o.stage || h("div", { "class": "w5-stage" });
    if (!o.stage) this.el.appendChild(this.stage);
    var word = o.word || "Step";
    this.word = word;
    this.back = h("button", { type: "button", "class": "w5-btn icon quiet", title: "Step back", "aria-label": "Step back" }, [icon("prev")]);
    this.playBtn = h("button", { type: "button", "class": "w5-btn primary" }, [icon("play"), h("span", { text: "Play" })]);
    this.fwd = h("button", { type: "button", "class": "w5-btn icon quiet", title: "Step forward", "aria-label": "Step forward" }, [icon("next")]);
    this.scrub = h("input", { type: "range", min: 0, max: Math.max(0, this.n - 1), step: 1, value: 0, "aria-label": "Scrub through the steps" });
    this.count = h("span", { "class": "w5-pcount" });
    this.capStep = h("span", { "class": "w5-cstep" });
    this.capText = h("span", { "class": "w5-ctext" });
    this.caption = h("div", { "class": "w5-caption", "aria-live": "polite" }, [this.capStep, this.capText]);
    var bar = h("div", { "class": "w5-pbar" }, [this.back, this.playBtn, this.fwd, this.scrub, this.count]);
    if (o.captionFirst) { this.el.appendChild(this.caption); this.el.appendChild(bar); }
    else { this.el.appendChild(bar); this.el.appendChild(this.caption); }
    function touch() { app.active = self; }
    this.back.addEventListener("click", function () { touch(); self.pause(); self.go(self.i - 1, false); });
    this.fwd.addEventListener("click", function () { touch(); self.pause(); self.go(self.i + 1, true); });
    this.playBtn.addEventListener("click", function () { touch(); if (self.playing) self.pause(); else self.play(); });
    this.scrub.addEventListener("input", function () { touch(); self.pause(); self.go(Number(self.scrub.value), false); });
    container.appendChild(this.el);
    app.players.push(this);
    this.label();
    this.render(0, 1);
  }
  Player.prototype.render = function (i, p) {
    if (this.o.render) this.o.render(i, p, this);
  };
  Player.prototype.label = function () {
    var f = this.frames[this.i] || {};
    this.count.textContent = this.word + " " + (this.i + 1) + " of " + this.n;
    this.capStep.textContent = this.word + " " + (this.i + 1);
    setRich(this.capText, f.caption || "");
    this.scrub.value = this.i;
    off(this.back, this.i <= 0);
    off(this.fwd, this.i >= this.n - 1);
    var last = this.i >= this.n - 1;
    this.playBtn.replaceChild(icon(this.playing ? "pause" : last ? "replay" : "play"), this.playBtn.firstChild);
    this.playBtn.lastChild.textContent = this.playing ? "Pause" : last ? "Play again" : "Play";
    if (this.o.onFrame) this.o.onFrame(this.i, this);
  };
  Player.prototype.go = function (i, animate) {
    i = clamp(i, 0, this.n - 1);
    if (this.tw) this.tw.finish();
    this.i = i;
    this.label();
    var self = this;
    if (animate) this.tw = tween(this.frames[i].ms || this.o.stepMs || 700, function (p) { self.render(i, p); });
    else this.render(i, 1);
  };
  Player.prototype.step = function (d) { this.pause(); this.go(this.i + d, d > 0); };
  Player.prototype.play = function () {
    var self = this;
    if (W5.reduced()) { this.go(this.n - 1, false); return; }
    if (this.i >= this.n - 1) this.go(0, false);
    this.playing = true;
    this.label();
    function next() {
      if (!self.playing) return;
      if (self.i >= self.n - 1) { self.playing = false; self.label(); return; }
      self.go(self.i + 1, true);
      var f = self.frames[self.i] || {};
      self.timer = setTimeout(next, (f.ms || self.o.stepMs || 700) + (self.o.holdMs !== undefined ? self.o.holdMs : 900));
    }
    next();
  };
  Player.prototype.pause = function () {
    if (this.timer) clearTimeout(this.timer);
    this.timer = 0;
    if (this.tw) this.tw.finish();
    if (this.playing) { this.playing = false; this.label(); }
  };
  Player.prototype.end = function () { this.pause(); this.go(this.n - 1, false); };
  W5.player = function (container, o) { return new Player(container, o); };

  /* ================================================================ scales and ticks */
  function nice(step) {
    var p = Math.pow(10, Math.floor(Math.log10(step))), f = step / p;
    return (f <= 1 ? 1 : f <= 2 ? 2 : f <= 2.5 ? 2.5 : f <= 5 ? 5 : 10) * p;
  }
  function ticks(min, max, n) {
    if (Array.isArray(n)) return n;
    var step = nice((max - min) / Math.max(1, n || 5)), out = [];
    var start = Math.ceil(min / step - 1e-9) * step;
    for (var v = start; v <= max + step * 1e-6; v += step) out.push(Math.round(v / step) * step);
    return out;
  }
  W5.ticks = ticks;
  function linear(d0, d1, r0, r1) {
    var f = function (v) { return r0 + (v - d0) / (d1 - d0 || 1) * (r1 - r0); };
    f.invert = function (px) { return d0 + (px - r0) / (r1 - r0 || 1) * (d1 - d0); };
    return f;
  }
  W5.bin = function (values, lo, hi, nb) {
    var out = new Array(nb).fill(0), w = (hi - lo) / nb;
    for (var i = 0; i < values.length; i++) {
      var k = Math.floor((values[i] - lo) / w);
      if (k >= 0 && k <= nb) out[Math.min(nb - 1, k)]++;
    }
    return out;
  };
  var COLORS = {
    violet: "#5B3FD6", amber: "#C96A00", teal: "#00A0A0", rest: "#BDB7DD", ink: "#1A0F5C",
    green: "#1F8A5B", rose: "#D63A6A", lilac: "#CFC9EE", muted: "#6B6690", lav: "#D9A7FF", night: "#1A1440"
  };
  W5.colors = COLORS;
  function col(c) { return COLORS[c] || c || COLORS.violet; }

  /* ================================================================ charts */
  function Chart(container, o) {
    this.o = o;
    this.series = [];
    this.byKey = {};
    this.el = h("div", { "class": "w5-chart" });
    this.svg = s("svg", { "class": "w5-svg", role: "img", "aria-label": o.label || o.title || "Chart" });
    this.el.appendChild(this.svg);
    this.tip = h("div", { "class": "w5-tip", hidden: true });
    this.el.appendChild(this.tip);
    if (o.legend) {
      var lg = h("div", { "class": "w5-legend" });
      o.legend.forEach(function (it) {
        var sw = h("i", { "class": it.kind === "line" ? "line" : it.kind === "hollow" ? "hollow" : "", style: { background: col(it.color), color: col(it.color) } });
        lg.appendChild(h("span", {}, [sw, it.label]));
      });
      this.el.appendChild(lg);
    }
    if (o.numbers !== false) {
      this.numBody = h("div", { "class": "w5-tablewrap" });
      this.el.appendChild(h("details", { "class": "w5-numbers" }, [h("summary", { text: o.numbersLabel || "Show the numbers behind this chart" }), this.numBody]));
    }
    container.appendChild(this.el);
    var self = this;
    onLayout(this.el, function (w) { self.layout(w); });
  }
  Chart.prototype.layout = function (w) {
    var o = this.o, fs = rootPx() * 0.8;
    this.fs = fs;
    var hgt = o.height || 300;
    if (w < 520) hgt = Math.max(o.minHeight || 210, Math.min(hgt, Math.round(w * (o.phoneRatio || 0.82))));
    this.w = w; this.h = hgt;
    var yt = o.y ? ticks(o.y.min, o.y.max, o.y.ticks) : [];
    var yfmt = (o.y && o.y.fmt) || String;
    var widest = yt.reduce(function (m, v) { return Math.max(m, String(yfmt(v)).length); }, 1);
    var m = this.m = {
      l: o.y && o.y.hide ? 10 : Math.round(widest * fs * 0.62 + 14),
      r: o.right !== undefined ? o.right : 16,
      t: o.y && o.y.label ? Math.round(fs * 2.1) : Math.round(fs * 0.9),
      b: Math.round(fs * (o.x && o.x.label ? 3.2 : 1.9))
    };
    this.pw = Math.max(40, w - m.l - m.r); this.ph = Math.max(40, hgt - m.t - m.b);
    this.svg.setAttribute("viewBox", "0 0 " + w + " " + hgt);
    this.svg.setAttribute("width", w); this.svg.setAttribute("height", hgt);
    if (o.x && o.x.band) {
      var bands = o.x.band, pw = this.pw, ml = m.l;
      this.sx = function (i) { return ml + (i + 0.5) * pw / bands.length; };
      this.bandW = pw / bands.length;
    } else this.sx = linear(o.x.min, o.x.max, m.l, m.l + this.pw);
    this.sy = linear(o.y.min, o.y.max, m.t + this.ph, m.t);
    this.svg.textContent = "";
    this.gGrid = s("g", { "class": "w5-grid" });
    this.gAxis = s("g", { "class": "w5-axis" });
    this.gPlot = s("g", {});
    this.gTop = s("g", {});
    this.svg.appendChild(this.gGrid); this.svg.appendChild(this.gAxis); this.svg.appendChild(this.gPlot); this.svg.appendChild(this.gTop);
    this.axes();
    var self = this;
    this.series.forEach(function (ser) { ser.g = s("g", {}); (ser.top ? self.gTop : self.gPlot).appendChild(ser.g); self.draw(ser, ser.data); });
    this.hover();
  };
  Chart.prototype.axes = function () {
    var o = this.o, m = this.m, fs = this.fs, self = this;
    var x0 = m.l, x1 = m.l + this.pw, y0 = m.t + this.ph, y1 = m.t;
    if (!(o.y && o.y.hide)) {
      ticks(o.y.min, o.y.max, o.y.ticks).forEach(function (v) {
        var y = self.sy(v);
        self.gGrid.appendChild(s("line", { x1: x0, x2: x1, y1: y, y2: y }));
        self.gAxis.appendChild(s("text", { x: x0 - 6, y: y + fs * 0.35, "text-anchor": "end", text: (o.y.fmt || String)(v) }));
      });
    }
    if (o.y && o.y.label) self.gAxis.appendChild(s("text", { "class": "w5-axtitle", x: 0, y: fs * 1.05, text: o.y.label }));
    self.gAxis.appendChild(s("line", { x1: x0, x2: x1, y1: y0, y2: y0 }));
    if (o.x.band) {
      var maxChars = Math.max(4, Math.floor(this.bandW / (fs * 0.56)));
      o.x.band.forEach(function (lab, i) {
        var t = String(lab); if (t.length > maxChars) t = t.slice(0, maxChars - 1) + ".";
        self.gAxis.appendChild(s("text", { x: self.sx(i), y: y0 + fs * 1.35, "text-anchor": "middle", text: t }));
      });
    } else {
      var xt = ticks(o.x.min, o.x.max, o.x.ticks);
      var room = this.pw / Math.max(1, xt.length - 1), fmtx = o.x.fmt || String;
      var widest = xt.reduce(function (mm, v) { return Math.max(mm, String(fmtx(v)).length); }, 1) * fs * 0.6 + 8;
      var every = Math.max(1, Math.ceil(widest / room));
      xt.forEach(function (v, i) {
        var x = self.sx(v);
        self.gAxis.appendChild(s("line", { x1: x, x2: x, y1: y0, y2: y0 + 4 }));
        if (i % every === 0) self.gAxis.appendChild(s("text", { x: x, y: y0 + fs * 1.35, "text-anchor": "middle", text: fmtx(v) }));
      });
    }
    if (o.x.label) self.gAxis.appendChild(s("text", { "class": "w5-axtitle", x: x1, y: y0 + fs * 2.75, "text-anchor": "end", text: o.x.label }));
  };
  Chart.prototype.add = function (type, key, data, opts) {
    var ser = this.byKey[key];
    if (ser) { this.set(key, data, 0); return ser; }
    ser = { type: type, key: key, data: data, opts: opts || {}, top: type === "vline" || type === "hline" || type === "text" || (opts && opts.top) };
    this.series.push(ser); this.byKey[key] = ser;
    if (this.w) { ser.g = s("g", {}); (ser.top ? this.gTop : this.gPlot).appendChild(ser.g); this.draw(ser, data); }
    this.numbers();
    return ser;
  };
  function flat(d) { return typeof d === "number" ? [d] : Array.prototype.concat.apply([], d.map(function (x) { return Array.isArray(x) ? x : [x]; })); }
  function unflat(arr, like) {
    if (typeof like === "number") return arr[0];
    var k = 0;
    return like.map(function (x) { if (Array.isArray(x)) { var r = arr.slice(k, k + x.length); k += x.length; return r; } return arr[k++]; });
  }
  Chart.prototype.set = function (key, data, ms) {
    var ser = this.byKey[key], self = this;
    if (!ser) return;
    var old = ser.data;
    ser.data = data;
    this.numbers();
    if (!this.w) return;
    if (ser.tw) ser.tw.cancel();
    var a = flat(ser.shown || old), b = flat(data);
    if (ms === 0 || a.length !== b.length) { ser.shown = data; this.draw(ser, data); return; }
    ser.tw = tween(ms === undefined ? 600 : ms, function (p) {
      var cur = a.map(function (v, i) { return lerp(v, b[i], p); });
      ser.shown = unflat(cur, data);
      self.draw(ser, ser.shown);
    });
  };
  Chart.prototype.draw = function (ser, d) {
    var g = ser.g, o = ser.opts, self = this, c = col(o.color), fs = this.fs;
    if (!g) return;
    g.textContent = "";
    ser.shown = d;
    var y0 = this.m.t + this.ph;
    if (ser.type === "line" || ser.type === "area") {
      if (!d.length) return;
      var path = d.map(function (pt, i) { return (i ? "L" : "M") + self.sx(pt[0]).toFixed(1) + " " + self.sy(pt[1]).toFixed(1); }).join("");
      if (ser.type === "area") {
        g.appendChild(s("path", { d: path + "L" + self.sx(d[d.length - 1][0]).toFixed(1) + " " + y0 + "L" + self.sx(d[0][0]).toFixed(1) + " " + y0 + "Z", fill: c, "fill-opacity": o.opacity || 0.12 }));
      }
      g.appendChild(s("path", { d: path, fill: "none", stroke: c, "stroke-width": o.width || 2.2, "stroke-linejoin": "round", "stroke-linecap": "round", "stroke-dasharray": o.dash || null }));
      if (o.dots) d.forEach(function (pt) { g.appendChild(s("circle", { cx: self.sx(pt[0]), cy: self.sy(pt[1]), r: 4, fill: c, stroke: "#fff", "stroke-width": 2 })); });
      if (o.end) {
        var last = d[d.length - 1];
        g.appendChild(s("circle", { cx: self.sx(last[0]), cy: self.sy(last[1]), r: 4.5, fill: c, stroke: "#fff", "stroke-width": 2 }));
        g.appendChild(s("text", { "class": "w5-mlabel w5-halo", x: self.sx(last[0]) + 8, y: self.sy(last[1]) + fs * 0.35, text: typeof o.end === "function" ? o.end(last) : o.end }));
      }
    } else if (ser.type === "scatter") {
      var r = o.r || 5;
      d.forEach(function (pt, i) {
        var st = o.style ? o.style(i) || {} : {};
        var cc = col(st.color || o.color), hollow = st.hollow !== undefined ? st.hollow : o.hollow;
        var dot = s("circle", { cx: self.sx(pt[0]), cy: self.sy(pt[1]), r: st.r || r, fill: hollow ? "#fff" : cc, stroke: hollow ? cc : "#fff", "stroke-width": 2 });
        dot.appendChild(s("title", { text: (o.name ? o.name(i) + ": " : "") + (o.fmtX || String)(pt[0]) + ", " + (o.fmtY || String)(pt[1]) }));
        g.appendChild(dot);
      });
    } else if (ser.type === "bars") {
      var bw = Math.min(o.maxWidth || 46, this.bandW * 0.62);
      d.forEach(function (v, i) {
        var x = self.sx(i) - bw / 2, y = self.sy(Math.max(v, self.o.y.min)), base = self.sy(self.o.y.min);
        var hh = Math.max(0, base - y), cc = col(o.colors ? o.colors[i] : o.color);
        var rr = Math.min(4, hh / 2, bw / 2);
        var p = "M" + x + " " + base + "V" + (y + rr) + "Q" + x + " " + y + " " + (x + rr) + " " + y + "H" + (x + bw - rr) + "Q" + (x + bw) + " " + y + " " + (x + bw) + " " + (y + rr) + "V" + base + "Z";
        var bar = s("path", { d: p, fill: cc });
        bar.appendChild(s("title", { text: (self.o.x.band[i] || "") + ": " + (o.fmt || String)(v) }));
        g.appendChild(bar);
        if (o.labels !== false) g.appendChild(s("text", { "class": "w5-mlabel", x: self.sx(i), y: y - 6, "text-anchor": "middle", text: (o.fmt || String)(v) }));
      });
    } else if (ser.type === "hist") {
      var lo = o.lo !== undefined ? o.lo : this.o.x.min, hi = o.hi !== undefined ? o.hi : this.o.x.max, nb = d.length, bwPx = (self.sx(hi) - self.sx(lo)) / nb;
      d.forEach(function (v, i) {
        var x = self.sx(lo) + i * bwPx, y = self.sy(v), hh = Math.max(0, y0 - y);
        if (hh <= 0) return;
        g.appendChild(s("rect", { x: x + 1, y: y, width: Math.max(0.5, bwPx - 2), height: hh, fill: c, "fill-opacity": o.opacity || 0.85, rx: Math.min(3, bwPx / 4) }));
      });
    } else if (ser.type === "segments") {
      d.forEach(function (sg) {
        g.appendChild(s("line", { x1: self.sx(sg[0]), y1: self.sy(sg[1]), x2: self.sx(sg[2]), y2: self.sy(sg[3]), stroke: c, "stroke-width": o.width || 2, "stroke-linecap": "round" }));
      });
    } else if (ser.type === "squares") {
      d.forEach(function (q) {
        var px = self.sx(q[0]), py = self.sy(q[1]), pf = self.sy(q[2]), side = Math.abs(py - pf);
        var left = o.side === "left" ? px - side : px;
        g.appendChild(s("rect", { x: left, y: Math.min(py, pf), width: side, height: side, fill: c, "fill-opacity": o.opacity || 0.16, stroke: c, "stroke-width": 1.2 }));
      });
    } else if (ser.type === "vline") {
      var vx = self.sx(typeof d === "number" ? d : d[0]);
      g.appendChild(s("line", { x1: vx, x2: vx, y1: this.m.t - 4, y2: y0, stroke: c || COLORS.ink, "stroke-width": o.width || 2.5 }));
      if (o.label) {
        var txt = typeof o.label === "function" ? o.label(typeof d === "number" ? d : d[0]) : o.label;
        var anchor = vx > this.m.l + this.pw * 0.7 ? "end" : "start";
        g.appendChild(s("text", { "class": "w5-mlabel w5-halo", x: vx + (anchor === "end" ? -7 : 7), y: this.m.t + fs * 0.9, "text-anchor": anchor, text: txt }));
      }
      if (o.drag) this.dragger(ser, vx);
    } else if (ser.type === "hline") {
      var hy = self.sy(typeof d === "number" ? d : d[0]);
      g.appendChild(s("line", { x1: this.m.l, x2: this.m.l + this.pw, y1: hy, y2: hy, stroke: c || COLORS.ink, "stroke-width": o.width || 1.6, "stroke-dasharray": o.dash || null }));
      if (o.label) g.appendChild(s("text", { "class": "w5-mlabel w5-halo", x: this.m.l + this.pw - 4, y: hy - 6, "text-anchor": "end", text: typeof o.label === "function" ? o.label(d) : o.label }));
    } else if (ser.type === "band") {
      var bx0 = self.sx(d[0]), bx1 = self.sx(d[1]);
      if (o.axis === "y") {
        var by0 = self.sy(d[0]), by1 = self.sy(d[1]);
        g.appendChild(s("rect", { x: this.m.l, y: Math.min(by0, by1), width: this.pw, height: Math.abs(by1 - by0), fill: c, "fill-opacity": o.opacity || 0.12 }));
        if (o.label) g.appendChild(s("text", { "class": "w5-mlabel", x: this.m.l + 6, y: Math.min(by0, by1) + fs * 1.1, text: o.label }));
      } else {
        g.appendChild(s("rect", { x: Math.min(bx0, bx1), y: this.m.t, width: Math.abs(bx1 - bx0), height: this.ph, fill: c, "fill-opacity": o.opacity || 0.12 }));
        if (o.label) g.appendChild(s("text", { "class": "w5-mlabel", x: Math.min(bx0, bx1) + 6, y: this.m.t + fs * 1.1, text: o.label }));
      }
    } else if (ser.type === "text") {
      g.appendChild(s("text", { "class": "w5-mlabel w5-halo", x: self.sx(d[0]), y: self.sy(d[1]), "text-anchor": o.anchor || "start", text: o.text }));
    }
  };
  Chart.prototype.dragger = function (ser, vx) {
    var self = this, o = ser.opts;
    var hit = s("rect", { "class": "w5-hit w5-drag", x: vx - 14, y: this.m.t - 6, width: 28, height: this.ph + 8, tabindex: "0", role: "slider",
      "aria-label": o.dragLabel || "Drag the line", "aria-valuenow": ser.data });
    var knob = s("circle", { cx: vx, cy: this.m.t - 4, r: 7, fill: "#fff", stroke: col(o.color) || COLORS.ink, "stroke-width": 2.5 });
    ser.g.appendChild(knob); ser.g.appendChild(hit);
    function move(clientX) {
      var r = self.svg.getBoundingClientRect(), x = clientX - r.left;
      var v = clamp(self.sx.invert(x), self.o.x.min, self.o.x.max);
      if (o.snap) v = Math.round(v / o.snap) * o.snap;
      o.drag(v);
    }
    hit.addEventListener("pointerdown", function (e) {
      hit.setPointerCapture(e.pointerId); move(e.clientX);
      function mv(ev) { move(ev.clientX); }
      function up() { hit.removeEventListener("pointermove", mv); hit.removeEventListener("pointerup", up); }
      hit.addEventListener("pointermove", mv); hit.addEventListener("pointerup", up);
    });
    hit.addEventListener("keydown", function (e) {
      var step = o.snap || (self.o.x.max - self.o.x.min) / 100;
      if (e.key === "ArrowRight" || e.key === "ArrowUp") { o.drag(clamp(Number(ser.data) + step, self.o.x.min, self.o.x.max)); e.preventDefault(); e.stopPropagation(); }
      if (e.key === "ArrowLeft" || e.key === "ArrowDown") { o.drag(clamp(Number(ser.data) - step, self.o.x.min, self.o.x.max)); e.preventDefault(); e.stopPropagation(); }
    });
  };
  Chart.prototype.hover = function () {
    var self = this, lines = this.series.filter(function (sr) { return sr.type === "line"; });
    if (!lines.length || this.o.hover === false) return;
    var cross = s("line", { x1: 0, x2: 0, y1: this.m.t, y2: this.m.t + this.ph, stroke: COLORS.ink, "stroke-width": 1, opacity: 0 });
    this.gTop.appendChild(cross);
    var zone = s("rect", { x: this.m.l, y: this.m.t, width: this.pw, height: this.ph, fill: "transparent" });
    this.gTop.insertBefore(zone, this.gTop.firstChild);
    var fmtx = this.o.x.fmt || String, fmty = this.o.y.fmt || String;
    zone.addEventListener("pointermove", function (e) {
      var r = self.svg.getBoundingClientRect(), x = self.sx.invert(e.clientX - r.left);
      var rows = [], snapX = null;
      lines.forEach(function (sr) {
        var best = null;
        (sr.data || []).forEach(function (pt) { if (!best || Math.abs(pt[0] - x) < Math.abs(best[0] - x)) best = pt; });
        if (best) { snapX = best[0]; rows.push([sr.opts.name || sr.key, fmty(best[1])]); }
      });
      if (snapX === null) return;
      var px = self.sx(snapX);
      cross.setAttribute("x1", px); cross.setAttribute("x2", px); cross.setAttribute("opacity", 0.5);
      self.tip.hidden = false; self.tip.textContent = "";
      self.tip.appendChild(h("div", { text: (self.o.x.label || "x") + ": " + fmtx(snapX) }));
      rows.forEach(function (rw) { self.tip.appendChild(h("div", {}, [h("b", { text: rw[1] }), " " + rw[0]])); });
      self.tip.style.left = clamp(px, 70, self.w - 70) + "px"; self.tip.style.top = (self.m.t + 10) + "px";
    });
    zone.addEventListener("pointerleave", function () { cross.setAttribute("opacity", 0); self.tip.hidden = true; });
  };
  Chart.prototype.numbers = function () {
    if (!this.numBody) return;
    var o = this.o, body = this.numBody;
    body.textContent = "";
    if (o.table) { body.appendChild(tableOf(o.table())); return; }
    var fx = (o.x && o.x.fmt) || function (v) { return typeof v === "number" ? +v.toFixed(3) : v; };
    var fy = (o.y && o.y.fmt) || function (v) { return typeof v === "number" ? +v.toFixed(3) : v; };
    this.series.forEach(function (ser) {
      var rows = [], name = ser.opts.name || ser.key, d = ser.data;
      if (ser.type === "line" || ser.type === "scatter" || ser.type === "area") d.forEach(function (pt) { rows.push([fx(pt[0]), fy(pt[1])]); });
      else if (ser.type === "bars") d.forEach(function (v, i) { rows.push([o.x.band[i], fy(v)]); });
      else if (ser.type === "hist") {
        var lo = ser.opts.lo !== undefined ? ser.opts.lo : o.x.min, hi = ser.opts.hi !== undefined ? ser.opts.hi : o.x.max, w = (hi - lo) / d.length;
        d.forEach(function (v, i) { rows.push([fx(lo + i * w) + " to " + fx(lo + (i + 1) * w), v]); });
      } else if (ser.type === "vline" || ser.type === "hline") rows.push([ser.type === "vline" ? "at x" : "at y", typeof d === "number" ? +d.toFixed(4) : d]);
      else return;
      body.appendChild(tableOf({ head: [name, ser.type === "hist" ? "Count" : (o.y && o.y.label) || "Value"], rows: rows.slice(0, 120) }));
    });
  };
  function tableOf(t) {
    var table = h("table", { "class": "w5-table" });
    var tr = h("tr");
    t.head.forEach(function (c, i) { tr.appendChild(h("th", { "class": i ? "n" : "", text: c })); });
    table.appendChild(tr);
    t.rows.forEach(function (r) {
      var row = h("tr");
      r.forEach(function (c, i) { row.appendChild(h("td", { "class": i ? "n" : "", text: c })); });
      table.appendChild(row);
    });
    return table;
  }
  W5.table = function (container, t) { var tb = tableOf(t); container.appendChild(h("div", { "class": "w5-tablewrap" }, [tb])); return tb; };
  ["line", "area", "scatter", "bars", "hist", "segments", "squares", "vline", "hline", "band", "text"].forEach(function (type) {
    Chart.prototype[type] = function (key, data, opts) { return this.add(type, key, data, opts); };
  });
  Chart.prototype.remove = function (key) {
    var ser = this.byKey[key]; if (!ser) return;
    if (ser.g && ser.g.parentNode) ser.g.parentNode.removeChild(ser.g);
    this.series.splice(this.series.indexOf(ser), 1); delete this.byKey[key];
    this.numbers();
  };
  W5.chart = function (container, o) { return new Chart(container, o); };

  /* ================================================================ the 2 by 2 matrix */
  W5.matrix = function (container, o) {
    var names = o.names || { tp: "True positive", fp: "False positive", fn: "False negative", tn: "True negative" };
    var grid = h("div", { "class": "w5-matrix" });
    grid.appendChild(h("div", { "class": "w5-mcorner", text: o.corner || "" }));
    var cols = o.cols || ["Predicted yes", "Predicted no"], rows = o.rows || ["Actually yes", "Actually no"];
    grid.appendChild(h("div", { "class": "w5-mhead", text: (o.colTitle ? o.colTitle + ": " : "") + cols[0] }));
    grid.appendChild(h("div", { "class": "w5-mhead", text: (o.colTitle ? o.colTitle + ": " : "") + cols[1] }));
    var cells = {};
    [["tp", "fn"], ["fp", "tn"]].forEach(function (pair, r) {
      grid.appendChild(h("div", { "class": "w5-mside", text: (o.rowTitle ? o.rowTitle + ": " : "") + rows[r] }));
      pair.forEach(function (k) {
        var right = k === "tp" || k === "tn";
        var count = h("span", { "class": "w5-ccount", text: "0" }), words = h("span", { "class": "w5-cwords" });
        var cell = h("div", { "class": "w5-cell " + (right ? "right" : "wrong"), "data-cell": k }, [
          h("span", { "class": "w5-cname" }, [icon(right ? "tick" : "cross"), names[k]]), count, words]);
        cells[k] = { el: cell, count: count, words: words };
        grid.appendChild(cell);
      });
    });
    var foot = h("div", { "class": "w5-mfoot", "aria-live": "polite" });
    grid.appendChild(foot);
    container.appendChild(grid);
    var counts = { tp: 0, fp: 0, fn: 0, tn: 0 };
    var api = {
      el: grid, cells: cells,
      set: function (c) {
        ["tp", "fp", "fn", "tn"].forEach(function (k) {
          var v = c[k] || 0;
          cells[k].count.textContent = group(v);
          var wv = o.words && o.words[k];
          setRich(cells[k].words, typeof wv === "function" ? wv(v, c) : (wv || ""));
          if (v !== counts[k] && !W5.reduced()) {
            cells[k].el.style.boxShadow = "0 0 0 3px #D9A7FF";
            setTimeout(function () { cells[k].el.style.boxShadow = ""; }, 420);
          }
        });
        counts = { tp: c.tp || 0, fp: c.fp || 0, fn: c.fn || 0, tn: c.tn || 0 };
        var n = counts.tp + counts.fp + counts.fn + counts.tn;
        foot.textContent = o.foot ? o.foot(counts) : group(n) + " in all: " + group(counts.tp + counts.tn) + " right and " + group(counts.fp + counts.fn) + " wrong.";
      },
      light: function (mode) {
        grid.classList.remove("lit-col", "lit-row");
        Object.keys(cells).forEach(function (k) { cells[k].el.classList.remove("lit"); });
        var keys = mode === "precision" ? ["tp", "fp"] : mode === "recall" ? ["tp", "fn"] : mode === "accuracy" ? ["tp", "tn"] : [];
        if (keys.length) { grid.classList.add(mode === "recall" ? "lit-row" : "lit-col"); keys.forEach(function (k) { cells[k].el.classList.add("lit"); }); }
      }
    };
    if (o.counts) api.set(o.counts);
    return api;
  };

  /* ================================================================ the dot grid of countable marks */
  var DOTS = {
    yes: { fill: COLORS.violet, stroke: COLORS.violet }, no: { fill: COLORS.rest, stroke: COLORS.rest },
    hit: { fill: COLORS.green, stroke: COLORS.green }, miss: { fill: COLORS.rose, stroke: COLORS.rose },
    amber: { fill: COLORS.amber, stroke: COLORS.amber }, teal: { fill: COLORS.teal, stroke: COLORS.teal },
    empty: { fill: "#FFFFFF", stroke: COLORS.lilac }, hollow: { fill: "#FFFFFF", stroke: COLORS.violet }, ink: { fill: COLORS.ink, stroke: COLORS.ink }
  };
  W5.dotgrid = function (container, o) {
    var wrap = h("div", { "class": "w5-dotgrid" });
    var svg = s("svg", { "class": "w5-svg", role: "img", "aria-label": o.label || "A grid of countable marks" });
    var legend = h("div", { "class": "w5-legend", "aria-live": "polite" });
    wrap.appendChild(svg); wrap.appendChild(legend);
    container.appendChild(wrap);
    var n = o.n, states = typeof o.states === "function" ? Array.from({ length: n }, function (_, i) { return o.states(i); }) : (o.states || new Array(n).fill("empty"));
    var marks = [];
    function legendUpdate() {
      var counts = {};
      states.forEach(function (st) { counts[st] = (counts[st] || 0) + 1; });
      legend.textContent = "";
      Object.keys(o.legend || counts).forEach(function (k) {
        if (!counts[k] && !(o.legend && o.legend[k])) return;
        var st = DOTS[k] || DOTS.empty;
        legend.appendChild(h("span", {}, [h("i", { style: { background: st.fill, border: "1.5px solid " + st.stroke, borderRadius: o.shape === "square" ? "3px" : "50%" } }),
          ((o.legend && o.legend[k]) || k) + ": " + group(counts[k] || 0)]));
      });
    }
    function layout(w) {
      var cols = o.cols || Math.ceil(Math.sqrt(n)), gap = o.gap !== undefined ? o.gap : 3;
      var size = Math.min(o.maxSize || 22, (w - (cols - 1) * gap) / cols);
      var rows = Math.ceil(n / cols), hh = rows * (size + gap) - gap;
      svg.setAttribute("viewBox", "0 0 " + w + " " + hh); svg.setAttribute("height", hh); svg.setAttribute("width", w);
      svg.textContent = ""; marks = [];
      var used = cols * (size + gap) - gap, x0 = o.align === "left" ? 0 : (w - used) / 2;
      for (var i = 0; i < n; i++) {
        var cx = x0 + (i % cols) * (size + gap), cy = Math.floor(i / cols) * (size + gap);
        var st = DOTS[states[i]] || DOTS.empty;
        var m = o.shape === "square" ? s("rect", { x: cx + 0.75, y: cy + 0.75, width: size - 1.5, height: size - 1.5, rx: Math.min(3, size / 5) })
          : s("circle", { cx: cx + size / 2, cy: cy + size / 2, r: Math.max(0.8, size / 2 - 0.9) });
        m.style.fill = st.fill; m.style.stroke = st.stroke; m.style.strokeWidth = size > 8 ? 1.6 : 0.8;
        m.style.transition = "fill .45s cubic-bezier(.45,0,.25,1), stroke .45s cubic-bezier(.45,0,.25,1)";
        svg.appendChild(m); marks.push(m);
      }
    }
    var api = {
      el: wrap,
      set: function (next, opts) {
        states = typeof next === "function" ? states.map(function (_, i) { return next(i); }) : next.slice();
        legendUpdate();
        var stagger = (opts && opts.stagger) || 0, reduced = W5.reduced();
        marks.forEach(function (m, i) {
          var st = DOTS[states[i]] || DOTS.empty;
          m.style.transitionDelay = reduced ? "0s" : (stagger * i / n).toFixed(3) + "s";
          m.style.fill = st.fill; m.style.stroke = st.stroke;
        });
      },
      states: function () { return states.slice(); }
    };
    legendUpdate();
    onLayout(wrap, layout);
    return api;
  };

  /* ================================================================ the canvas dot cloud */
  function Cloud(container, o) {
    this.o = o;
    this.n = o.n;
    this.palette = o.palette || { yes: COLORS.violet, no: COLORS.rest };
    this.keys = Object.keys(this.palette);
    this.cIdx = new Uint8Array(this.n);
    this.cur = new Float32Array(this.n * 2);
    this.to = new Float32Array(this.n * 2);
    this.from = new Float32Array(this.n * 2);
    this.delay = new Float32Array(this.n);
    this.r = 2;
    this.el = h("div", { "class": "w5-cloud" });
    this.canvas = h("canvas", { role: "img", "aria-label": o.label || "A cloud of dots, one per record" });
    this.under = h("div", { "class": "w5-under" });
    this.over = h("div", { "class": "w5-over" });
    this.el.appendChild(this.under); this.el.appendChild(this.canvas); this.el.appendChild(this.over);
    container.appendChild(this.el);
    this.place = o.place;
    if (o.color) this.recolor(o.color, true);
    var self = this, rng = seeded(o.seed || 7);
    for (var i = 0; i < this.n; i++) this.delay[i] = rng();
    onLayout(this.el, function (w) { self.layout(w); });
  }
  Cloud.prototype.layout = function (w) {
    var hh = typeof this.o.height === "function" ? this.o.height(w) : (this.o.height || 320);
    if (w < 520 && this.o.phoneHeight) hh = typeof this.o.phoneHeight === "function" ? this.o.phoneHeight(w) : this.o.phoneHeight;
    this.w = w; this.h = hh;
    var dpr = this.dpr = Math.min(window.devicePixelRatio || 1, 2.5);
    this.canvas.width = Math.round(w * dpr); this.canvas.height = Math.round(hh * dpr);
    this.canvas.style.height = hh + "px";
    this.ctx = this.canvas.getContext("2d");
    if (this.place) { this.computeTargets(); this.cur.set(this.to); }
    this.sprites();
    this.draw();
    if (this.o.onLayout) this.o.onLayout(this);
  };
  Cloud.prototype.computeTargets = function () {
    var r = this.place(this.w, this.h, this.to, this);
    if (r) this.r = r;
  };
  Cloud.prototype.sprites = function () {
    var self = this, dpr = this.dpr, rr = this.r * dpr, size = Math.ceil(rr * 2 + 2);
    this.spr = this.keys.map(function (k) {
      var c = document.createElement("canvas"); c.width = c.height = size;
      var x = c.getContext("2d"); x.fillStyle = self.palette[k];
      x.beginPath(); x.arc(size / 2, size / 2, rr, 0, Math.PI * 2); x.fill();
      return c;
    });
    this.sprSize = size;
  };
  Cloud.prototype.draw = function () {
    var ctx = this.ctx; if (!ctx) return;
    ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    var dpr = this.dpr, half = this.sprSize / 2, cur = this.cur, idx = this.cIdx, spr = this.spr;
    for (var i = 0; i < this.n; i++) ctx.drawImage(spr[idx[i]], cur[2 * i] * dpr - half, cur[2 * i + 1] * dpr - half);
  };
  Cloud.prototype.recolor = function (fn, silent) {
    var keys = this.keys;
    for (var i = 0; i < this.n; i++) { var k = keys.indexOf(fn(i)); this.cIdx[i] = k < 0 ? 0 : k; }
    if (!silent) this.draw();
  };
  Cloud.prototype.go = function (place, opts) {
    opts = opts || {};
    var self = this, oldR = this.r;
    if (place) this.place = place;
    if (opts.color) this.recolor(opts.color, true);
    if (!this.w) return;
    this.computeTargets();
    if (this.r !== oldR) this.sprites();
    if (this.tw) this.tw.cancel();
    this.from.set(this.cur);
    var st = opts.stagger || 0, from = this.from, to = this.to, cur = this.cur, delay = this.delay, n = this.n;
    this.tw = tween(opts.ms === undefined ? 700 : opts.ms, function (p, raw) {
      for (var i = 0; i < n; i++) {
        var q = st ? ease(clamp((raw - delay[i] * st) / (1 - st), 0, 1)) : p;
        cur[2 * i] = from[2 * i] + (to[2 * i] - from[2 * i]) * q;
        cur[2 * i + 1] = from[2 * i + 1] + (to[2 * i + 1] - from[2 * i + 1]) * q;
      }
      self.draw();
    });
  };
  Cloud.prototype.box = function (key, x, y, w, hh, cls) {
    this.boxes = this.boxes || {};
    var b = this.boxes[key];
    if (!b) { b = this.boxes[key] = h("div", { "class": "w5-cbox" }); this.under.appendChild(b); }
    b.className = "w5-cbox" + (cls ? " " + cls : "");
    b.style.left = x + "px"; b.style.top = y + "px"; b.style.width = w + "px"; b.style.height = hh + "px";
    return b;
  };
  Cloud.prototype.label = function (key, x, y, content, cls) {
    this.labels = this.labels || {};
    var lab = this.labels[key];
    if (!lab) { lab = this.labels[key] = h("div", { "class": "w5-boxlabel" }); this.over.appendChild(lab); }
    lab.className = "w5-boxlabel" + (cls ? " " + cls : "");
    lab.style.left = x + "px"; lab.style.top = y + "px";
    lab.textContent = "";
    (Array.isArray(content) ? content : [content]).forEach(function (c) { lab.appendChild(typeof c === "string" ? rich(c) : c); });
    return lab;
  };
  W5.cloud = function (container, o) { return new Cloud(container, o); };

  /* Placement helpers for the cloud: each fills out[2i], out[2i+1] for the ids it is given. */
  W5.pack = {
    pitch: function (box, count) {
      if (count <= 0) return Math.min(box.w, box.h);
      var p = Math.sqrt(box.w * box.h / count);
      while (p > 0.5 && Math.floor(box.w / p) * Math.floor(box.h / p) < count) p *= 0.97;
      return p;
    },
    grid: function (ids, box, out, opts) {
      opts = opts || {};
      var p = opts.pitch || W5.pack.pitch(box, opts.capacity || ids.length);
      var cols = Math.max(1, Math.floor(box.w / p)), x0 = box.x + (box.w - cols * p) / 2 + p / 2;
      for (var k = 0; k < ids.length; k++) {
        var c = k % cols, r = Math.floor(k / cols), i = ids[k];
        out[2 * i] = x0 + c * p;
        out[2 * i + 1] = opts.from === "bottom" ? box.y + box.h - p / 2 - r * p : box.y + p / 2 + r * p;
      }
      return p;
    },
    columns: function (ids, values, box, out, opts) {
      opts = opts || {};
      var nb = opts.bins || 20, lo = opts.lo !== undefined ? opts.lo : 0, hi = opts.hi !== undefined ? opts.hi : 1;
      var buckets = []; for (var b = 0; b < nb; b++) buckets.push([]);
      ids.forEach(function (i) { var k = Math.floor((values[i] - lo) / (hi - lo) * nb); buckets[clamp(k, 0, nb - 1)].push(i); });
      var tallest = buckets.reduce(function (m, bk) { return Math.max(m, bk.length); }, 1);
      var bw = box.w / nb;
      var p = opts.pitch || Math.max(0.6, Math.min(bw, Math.sqrt(bw * box.h / tallest)));
      while (p > 0.6 && Math.max(1, Math.floor(bw / p)) * Math.floor(box.h / p) < tallest) p *= 0.96;
      var per = Math.max(1, Math.floor(bw / p));
      buckets.forEach(function (bk, b2) {
        var x0 = box.x + b2 * bw + (bw - per * p) / 2 + p / 2;
        bk.forEach(function (i, k) {
          out[2 * i] = x0 + (k % per) * p;
          out[2 * i + 1] = box.y + box.h - p / 2 - Math.floor(k / per) * p;
        });
      });
      return { pitch: p, counts: buckets.map(function (bk) { return bk.length; }) };
    }
  };

  /* ================================================================ a plain SVG stage for custom drawing */
  W5.svgStage = function (container, o) {
    var svg = s("svg", { "class": "w5-svg", role: "img", "aria-label": o.label || "Diagram" });
    container.appendChild(svg);
    var api = { svg: svg, w: 0, h: 0, el: svg };
    onLayout(container, function (w) {
      var hh = typeof o.height === "function" ? o.height(w) : (o.height || 300);
      api.w = w; api.h = hh;
      svg.setAttribute("viewBox", "0 0 " + w + " " + hh); svg.setAttribute("width", w); svg.setAttribute("height", hh);
      svg.textContent = "";
      if (o.draw) o.draw(api);
    });
    api.redraw = function () { if (api.w) { svg.textContent = ""; o.draw(api); } };
    return api;
  };

  /* ================================================================ the week line */
  W5.weekline = function (container, o) {
    var wrap = h("div", { "class": "w5-week" });
    var ol = h("ol");
    o.days.forEach(function (d, i) {
      var cls = i < o.today ? "done" : i === o.today ? "today" : "later";
      ol.appendChild(h("li", { "class": cls, "aria-current": i === o.today ? "step" : null }, [
        h("span", { "class": "w5-wdot" }, [i < o.today ? icon("tick") : String(i + 1)]),
        h("span", { "class": "w5-wname", text: d.name }),
        h("span", { "class": "w5-wq", text: d.q })
      ]));
    });
    wrap.appendChild(ol);
    wrap.appendChild(h("p", { "class": "w5-todayq", text: (o.days[o.today] || {}).q || "" }));
    container.appendChild(wrap);
    return wrap;
  };

  /* ================================================================ the concept map */
  function wrapText(text, perLine) {
    var words = String(text).split(/\s+/), lines = [], line = "";
    words.forEach(function (w) {
      if (line && (line + " " + w).length > perLine) { lines.push(line); line = w; }
      else line = line ? line + " " + w : w;
    });
    if (line) lines.push(line);
    return lines;
  }
  W5.conceptMap = function (container, o) {
    var wrap = h("div", { "class": "w5-map" });
    var svgHost = h("div", {});
    wrap.appendChild(svgHost);
    var panel = h("div", { "class": "w5-mappanel", "aria-live": "polite" });
    var key = h("div", { "class": "w5-mapkey" }, [
      h("span", {}, [h("i", { style: { background: "#1A0F5C" } }), "Today"]),
      h("span", {}, [h("i", { style: { background: "#EEEAFB", border: "1.5px solid #5B3FD6" } }), "Met earlier"]),
      h("span", {}, [h("i", { style: { background: "#fff", border: "1.5px dashed #6B6690" } }), "Comes later"])
    ]);
    container.appendChild(wrap);
    var nodes = o.nodes, byId = {};
    nodes.forEach(function (n) { byId[n.id] = n; });
    var path = o.path || nodes.filter(function (n) { return n.kind === "today"; }).map(function (n) { return n.id; });
    var svg = s("svg", { "class": "w5-svg", role: "img", "aria-label": o.label || "Concept map of today's ideas" });
    svgHost.appendChild(svg);
    var litUpTo = path.length;
    var els = {};
    o.edges.forEach(function (e) {
      if (!byId[e.from] || !byId[e.to]) lint("a map edge names a node that does not exist: " + e.from + " to " + e.to);
      if (!e.label) lint("the map edge " + e.from + " to " + e.to + " has no label");
      else if (e.label.length > 26) console.warn("w5kit: map edge label longer than 26 characters: " + e.label);
    });

    function setPanel(n, stepNo) {
      panel.textContent = "";
      if (!n) {
        panel.appendChild(h("div", { "class": "w5-mpnum" }, [icon("map")]));
        panel.appendChild(h("div", { "class": "w5-mptitle", text: o.intro || "Today's ideas, in the order the day climbs them." }));
        panel.appendChild(h("div", { "class": "w5-mptext", text: "Press play to walk the path, or pick any idea. Today's ideas open their own page." }));
        return;
      }
      var rel = [];
      o.edges.forEach(function (e) {
        if (e.to === n.id) rel.push(byId[e.from].label + " " + e.label + " " + n.label + ".");
        else if (e.from === n.id) rel.push(n.label + " " + e.label + " " + byId[e.to].label + ".");
      });
      panel.appendChild(h("div", { "class": "w5-mpnum" }, [stepNo ? String(stepNo) : icon(n.kind === "earlier" ? "ledger" : "flag")]));
      panel.appendChild(h("div", { "class": "w5-mptitle", text: n.label + (n.sub ? " · " + n.sub : "") }));
      var txt = h("div", { "class": "w5-mptext" });
      if (n.story) txt.appendChild(h("div", { rich: n.story }));
      if (rel.length) txt.appendChild(h("div", { text: rel.join(" ") }));
      panel.appendChild(txt);
    }

    function nodeBox(n, x, y, w, fs, step) {
      var per = Math.max(10, Math.floor((w - 24 - (step ? 26 : 0)) / (fs * 0.55)));
      var lines = wrapText(n.label, per), subH = n.sub ? fs * 1.15 : 0;
      var hh = Math.round(lines.length * fs * 1.25 + subH + 20);
      return { n: n, x: x, y: y, w: w, h: hh, lines: lines, fs: fs, step: step };
    }
    function drawNode(b) {
      var n = b.n, g = s("g", { "class": "w5-node", tabindex: "0", role: "link", "aria-label": n.label + (n.route ? ", opens its page" : "") });
      if (n.route) {
        var a = s("a", { href: "#" + n.route, "aria-label": n.label });
        a.appendChild(g); svg.appendChild(a);
      } else {
        g.setAttribute("role", "button");
        svg.appendChild(g);
      }
      var fill = n.kind === "today" ? "#1A0F5C" : n.kind === "earlier" ? "#EEEAFB" : "#FFFFFF";
      var stroke = n.kind === "today" ? "#1A0F5C" : n.kind === "earlier" ? "#5B3FD6" : "#6B6690";
      var ink = n.kind === "today" ? "#FFFFFF" : "#1A0F5C";
      g.appendChild(s("rect", { x: b.x, y: b.y, width: b.w, height: b.h, rx: 10, fill: fill, stroke: stroke, "stroke-width": 1.6, "stroke-dasharray": n.kind === "later" ? "5 4" : null }));
      var tx = b.x + 12;
      if (b.step) {
        g.appendChild(s("circle", { cx: b.x + 18, cy: b.y + b.h / 2, r: 11, fill: "#5B3FD6" }));
        g.appendChild(s("text", { x: b.x + 18, y: b.y + b.h / 2 + b.fs * 0.36, "text-anchor": "middle", fill: "#fff", "font-weight": 700, "font-size": b.fs * 0.9, text: String(b.step) }));
        tx = b.x + 38;
      }
      var ty = b.y + 10 + b.fs;
      b.lines.forEach(function (ln, i) {
        g.appendChild(s("text", { x: tx, y: ty + i * b.fs * 1.25, fill: ink, "font-weight": 600, "font-size": b.fs, text: ln }));
      });
      if (n.sub) g.appendChild(s("text", { x: tx, y: ty + b.lines.length * b.fs * 1.25, fill: n.kind === "today" ? "#D9A7FF" : "#4E38AB", "font-size": b.fs * 0.82, text: n.sub }));
      if (!n.route) {
        g.addEventListener("click", function () { setPanel(n); });
        g.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { setPanel(n); e.preventDefault(); } });
      }
      els[n.id] = g;
      return g;
    }
    function curve(x1, y1, x2, y2) {
      var dx = (x2 - x1) * 0.5;
      return { d: "M" + x1 + " " + y1 + "C" + (x1 + dx) + " " + y1 + " " + (x2 - dx) + " " + y2 + " " + x2 + " " + y2,
        at: function (t) {
          var mt = 1 - t;
          return [mt * mt * mt * x1 + 3 * mt * mt * t * (x1 + dx) + 3 * mt * t * t * (x2 - dx) + t * t * t * x2,
            mt * mt * mt * y1 + 3 * mt * mt * t * y1 + 3 * mt * t * t * y2 + t * t * t * y2];
        } };
    }
    var placed = [];
    function overlaps(r) {
      return placed.some(function (q) { return r.x < q.x + q.w && q.x < r.x + r.w && r.y < q.y + q.h && q.y < r.y + r.h; });
    }
    function edgeLabel(text, c, fs, edgeEl) {
      var w = text.length * fs * 0.56 + 12, hgt = fs * 1.45, best = null;
      [0.5, 0.42, 0.58, 0.34, 0.66, 0.26, 0.74].some(function (t) {
        var pt = c.at(t), r = { x: pt[0] - w / 2, y: pt[1] - hgt / 2, w: w, h: hgt };
        if (!overlaps(r)) { best = r; return true; }
        return false;
      });
      if (!best) { var p0 = c.at(0.5); best = { x: p0[0] - w / 2, y: p0[1] - hgt / 2, w: w, h: hgt }; }
      placed.push(best);
      var g = s("g", {});
      g.appendChild(s("rect", { x: best.x, y: best.y, width: best.w, height: best.h, rx: hgt / 2, fill: "#FFFFFF", stroke: "#E4E1F1" }));
      g.appendChild(s("text", { "class": "w5-elabel", x: best.x + best.w / 2, y: best.y + hgt / 2 + fs * 0.35, "text-anchor": "middle", text: text, "font-size": fs }));
      edgeEl.label = g;
      return g;
    }
    var boxes = {}, edgeEls = [];
    function layout(w) {
      svg.textContent = ""; placed = []; boxes = {}; edgeEls = []; els = {};
      var fs = rootPx() * (w < 720 ? 0.84 : 0.8);
      var defs = s("defs");
      var mk = s("marker", { id: "w5arrow", viewBox: "0 0 10 10", refX: 9, refY: 5, markerWidth: 7, markerHeight: 7, orient: "auto-start-reverse" });
      mk.appendChild(s("path", { d: "M0 0L10 5L0 10z", fill: "#5B3FD6" }));
      var mk2 = s("marker", { id: "w5arrowSoft", viewBox: "0 0 10 10", refX: 9, refY: 5, markerWidth: 6, markerHeight: 6, orient: "auto-start-reverse" });
      mk2.appendChild(s("path", { d: "M0 0L10 5L0 10z", fill: "#A9A3D2" }));
      defs.appendChild(mk); defs.appendChild(mk2); svg.appendChild(defs);
      var today = path.map(function (id) { return byId[id]; }).filter(Boolean);
      var earlier = nodes.filter(function (n) { return n.kind === "earlier"; }), later = nodes.filter(function (n) { return n.kind === "later"; });
      var hh;
      if (w >= 720) {
        var sideW = Math.round(w * 0.2), gapW = Math.round(w * 0.14), midW = w - 2 * sideW - 2 * gapW;
        var xE = 0, xT = sideW + gapW, xL = xT + midW + gapW, y = 6, gap = Math.round(fs * 2.6);
        today.forEach(function (n, i) { var b = nodeBox(n, xT, y, midW, fs, i + 1); boxes[n.id] = b; y += b.h + gap; });
        var tBottom = y - gap;
        function side(list, x) {
          var bs = list.map(function (n) {
            var ys = o.edges.filter(function (e) { return e.from === n.id || e.to === n.id; }).map(function (e) { var b = boxes[e.from === n.id ? e.to : e.from]; return b ? b.y + b.h / 2 : null; }).filter(function (v) { return v !== null; });
            var b = nodeBox(n, x, 0, sideW, fs * 0.92, 0);
            b.want = ys.length ? ys.reduce(function (a, c) { return a + c; }, 0) / ys.length - b.h / 2 : 0;
            return b;
          });
          bs.sort(function (a, b) { return a.want - b.want; });
          var cursor = 0;
          bs.forEach(function (b) { b.y = Math.max(cursor, b.want); cursor = b.y + b.h + 14; });
          var over = cursor - 14 - Math.max(tBottom, 0);
          if (over > 0) { for (var k = bs.length - 1, lim = tBottom; k >= 0; k--) { if (bs[k].y + bs[k].h > lim) bs[k].y = lim - bs[k].h; lim = bs[k].y - 14; } }
          bs.forEach(function (b) { b.y = Math.max(0, b.y); boxes[b.n.id] = b; });
          return bs.reduce(function (m, b) { return Math.max(m, b.y + b.h); }, 0);
        }
        hh = Math.max(tBottom, side(earlier, xE), side(later, xL)) + 8;
        o.edges.forEach(function (e) {
          var a = boxes[e.from], b = boxes[e.to]; if (!a || !b) return;
          var onPath = a.n.kind === "today" && b.n.kind === "today";
          var el = { e: e }, c;
          if (onPath) {
            var x = a.x + a.w / 2, y1 = a.y + a.h, y2 = b.y;
            if (b.y < a.y) { y1 = a.y; y2 = b.y + b.h; }
            el.path = s("path", { d: "M" + x + " " + y1 + "L" + x + " " + (y2 - 2), stroke: "#5B3FD6", "stroke-width": 2.4, fill: "none", "marker-end": "url(#w5arrow)" });
            c = { at: function (t) { return [x + (e.label.length * fs * 0.28) + 16, lerp(y1, y2, t)]; } };
          } else {
            var fromRight = a.x < b.x, x1 = fromRight ? a.x + a.w : a.x, x2 = fromRight ? b.x : b.x + b.w;
            c = curve(x1, a.y + a.h / 2, x2 - (fromRight ? 2 : -2), b.y + b.h / 2);
            el.path = s("path", { d: c.d, stroke: "#A9A3D2", "stroke-width": 1.6, fill: "none", "marker-end": "url(#w5arrowSoft)" });
          }
          svg.appendChild(el.path);
          el.c = c; el.onPath = onPath; edgeEls.push(el);
        });
        Object.keys(boxes).forEach(function (id) { placed.push({ x: boxes[id].x, y: boxes[id].y, w: boxes[id].w, h: boxes[id].h }); });
        edgeEls.forEach(function (el) { svg.appendChild(edgeLabel(el.e.label, el.c, fs * 0.86, el)); });
        Object.keys(boxes).forEach(function (id) { drawNode(boxes[id]); });
      } else {
        var y2 = 4, chipGap = 8, pad = 26;
        function chips(list, label) {
          if (!list.length) return;
          svg.appendChild(s("text", { x: 0, y: y2 + fs, "font-size": fs * 0.84, "font-weight": 700, fill: "#4E38AB", text: label }));
          y2 += fs * 1.6;
          var x = 0, rowH = 0;
          list.forEach(function (n) {
            var cw = Math.min(w, n.label.length * fs * 0.84 * 0.56 + 28 + (n.sub ? n.sub.length * fs * 0.84 * 0.5 : 0));
            var b = nodeBox(n, 0, 0, Math.max(cw, 90), fs * 0.84, 0);
            if (x > 0 && x + b.w > w) { x = 0; y2 += rowH + chipGap; rowH = 0; }
            b.x = x; b.y = y2; x += b.w + chipGap; rowH = Math.max(rowH, b.h);
            boxes[n.id] = b;
          });
          y2 += rowH + 14;
        }
        chips(earlier, "Met earlier");
        var top = y2;
        today.forEach(function (n, i) {
          var rel = o.edges.filter(function (e) { return e.to === n.id && byId[e.from] && byId[e.from].kind === "earlier"; }).map(function (e) { return byId[e.from].label; });
          var fwd = o.edges.filter(function (e) { return e.from === n.id && byId[e.to] && byId[e.to].kind === "later"; }).map(function (e) { return byId[e.to].label; });
          var b = nodeBox(n, pad, y2, w - pad, fs, i + 1);
          b.rel = rel; b.fwd = fwd;
          var extra = (rel.length ? 1 : 0) + (fwd.length ? 1 : 0);
          var relLines = 0;
          [rel, fwd].forEach(function (lst, k) { if (lst.length) relLines += wrapText((k ? "Feeds " : "Rests on ") + lst.join(", "), Math.floor((w - pad - 50) / (fs * 0.8 * 0.55))).length; });
          b.h += relLines * fs * 0.8 * 1.3 + (extra ? 6 : 0);
          boxes[n.id] = b; y2 += b.h + fs * 2.2;
        });
        y2 -= fs * 2.2; y2 += 14;
        svg.appendChild(s("line", { x1: 10, x2: 10, y1: top, y2: y2 - 14, stroke: "#5B3FD6", "stroke-width": 2.4 }));
        chips(later, "Comes later");
        hh = y2 + 4;
        o.edges.forEach(function (e) {
          var a = boxes[e.from], b = boxes[e.to];
          if (!a || !b || a.n.kind !== "today" || b.n.kind !== "today") return;
          var mid = (a.y + a.h + b.y) / 2;
          svg.appendChild(s("text", { x: pad + 10, y: mid + fs * 0.32, "font-size": fs * 0.8, fill: "#4E38AB", "font-weight": 600, text: e.label }));
        });
        Object.keys(boxes).forEach(function (id) {
          var b = boxes[id], g = drawNode(b);
          if (b.n.kind === "today") {
            var fsr = fs * 0.8, yy = b.y + 10 + b.fs + b.lines.length * b.fs * 1.25 + 4;
            [[b.rel, "Rests on "], [b.fwd, "Feeds "]].forEach(function (pair) {
              if (!pair[0] || !pair[0].length) return;
              wrapText(pair[1] + pair[0].join(", "), Math.floor((w - pad - 50) / (fsr * 0.55))).forEach(function (ln) {
                g.appendChild(s("text", { x: b.x + 38, y: yy + fsr, fill: "#D9A7FF", "font-size": fsr, text: ln }));
                yy += fsr * 1.3;
              });
            });
          }
        });
      }
      svg.setAttribute("viewBox", "0 0 " + w + " " + Math.ceil(hh)); svg.setAttribute("width", w); svg.setAttribute("height", Math.ceil(hh));
      paint(1);
    }
    function paint(p) {
      var lit = {};
      path.forEach(function (id, i) { if (i < litUpTo) lit[id] = 1; });
      var showAll = litUpTo >= path.length;
      Object.keys(els).forEach(function (id) {
        var n = byId[id], on = showAll || lit[id] || (n.kind === "earlier" && o.edges.some(function (e) { return e.from === id && lit[e.to]; }));
        els[id].style.opacity = on ? 1 : 0.22;
      });
      edgeEls.forEach(function (el) {
        var on = showAll || (lit[el.e.to] && (lit[el.e.from] || byId[el.e.from].kind === "earlier"));
        var o2 = on ? 1 : 0.15;
        el.path.style.opacity = o2; if (el.label) el.label.style.opacity = o2;
      });
    }
    var frames = [{ caption: o.intro || "The whole day on one picture: what today's ideas rest on, the order the day climbs them, and what they feed next." }];
    path.forEach(function (id, i) { frames.push({ caption: (o.steps && o.steps[i]) || byId[id].story || byId[id].label }); });
    var player = null;
    if (o.player !== false) {
      player = W5.player(wrap, { frames: frames, word: "Step", stepMs: 500, holdMs: 1400, render: function (i) {
        litUpTo = i === 0 ? path.length : i;
        paint(1);
        if (i > 0) setPanel(byId[path[i - 1]], i); else setPanel(null);
      } });
    }
    wrap.appendChild(panel);
    wrap.appendChild(key);
    setPanel(null);
    onLayout(svgHost, layout);
    return { el: wrap, player: player };
  };

  /* ================================================================ ordering and bins (drag, with buttons and clicks as the fallback) */
  W5.orderList = function (container, o) {
    var items = o.items.slice();
    var order = o.start ? o.start.slice() : shuffledIndex(items.length, o.seed || 3);
    var ol = h("ol", { "class": "w5-order" });
    var status = h("p", { "class": "w5-pstate", "aria-live": "polite", text: o.prompt || "Drag the cards, or use the arrows, until the order is right." });
    container.appendChild(ol);
    function render() {
      ol.textContent = "";
      order.forEach(function (idx, pos) {
        var up = h("button", { type: "button", "class": "w5-mv", "aria-label": "Move up", title: "Move up" }, [icon("arrowUp")]);
        var dn = h("button", { type: "button", "class": "w5-mv", "aria-label": "Move down", title: "Move down" }, [icon("arrowDown")]);
        off(up, pos === 0); off(dn, pos === order.length - 1);
        up.addEventListener("click", function () { move(pos, pos - 1); });
        dn.addEventListener("click", function () { move(pos, pos + 1); });
        var li = h("li", { "data-idx": idx }, [h("span", { "class": "w5-grip", "aria-hidden": "true" }, [icon("grip")]), h("span", { "class": "w5-onum", text: String(pos + 1) }),
          h("span", { "class": "w5-otext", rich: items[idx] }), up, dn]);
        drag(li, pos);
        ol.appendChild(li);
      });
    }
    function move(a, b) {
      if (b < 0 || b >= order.length) return;
      var x = order.splice(a, 1)[0]; order.splice(b, 0, x);
      render();
      status.textContent = "Moved “" + strip(items[x]) + "” to place " + (b + 1) + ".";
      if (o.onChange) o.onChange(order.slice());
    }
    function drag(li, pos) {
      li.addEventListener("pointerdown", function (e) {
        if (e.target.closest("button")) return;
        var startY = e.clientY, moved = false, target = pos;
        li.setPointerCapture(e.pointerId);
        function mv(ev) {
          if (!moved && Math.abs(ev.clientY - startY) < 6) return;
          moved = true; li.classList.add("dragging");
          var lis = Array.prototype.slice.call(ol.children);
          target = lis.length - 1;
          for (var k = 0; k < lis.length; k++) { var r = lis[k].getBoundingClientRect(); if (ev.clientY < r.top + r.height / 2) { target = k; break; } }
        }
        function up() {
          li.removeEventListener("pointermove", mv); li.removeEventListener("pointerup", up); li.removeEventListener("pointercancel", up);
          li.classList.remove("dragging");
          if (moved && target !== pos) move(pos, target > pos ? target : target);
        }
        li.addEventListener("pointermove", mv); li.addEventListener("pointerup", up); li.addEventListener("pointercancel", up);
      });
    }
    container.appendChild(status);
    render();
    return {
      el: ol, status: status,
      order: function () { return order.slice(); },
      mark: function () {
        var right = 0;
        Array.prototype.forEach.call(ol.children, function (li, pos) {
          var ok = order[pos] === pos; if (ok) right++;
          li.classList.toggle("right", ok); li.classList.toggle("wrong", !ok);
        });
        return right;
      },
      solve: function () { order = items.map(function (_, i) { return i; }); render(); }
    };
  };
  function strip(t) { return String(t).replace(/\*\*/g, ""); }
  function shuffledIndex(n, seed) {
    var a = [], rng = seeded(seed);
    for (var i = 0; i < n; i++) a.push(i);
    for (var tries = 0; tries < 8; tries++) {
      for (var j = n - 1; j > 0; j--) { var k = Math.floor(rng() * (j + 1)), t = a[j]; a[j] = a[k]; a[k] = t; }
      if (a.some(function (v, idx) { return v !== idx; })) break;
    }
    return a;
  }

  W5.bins = function (container, o) {
    var place = o.cards.map(function () { return -1; });
    var picked = -1;
    var pool = h("div", { "class": "w5-pool" });
    var binsEl = h("div", { "class": "w5-bins" });
    var status = h("p", { "class": "w5-pstate", "aria-live": "polite", text: "Drag each card into a bin, or tap a card and then a bin." });
    container.appendChild(pool); container.appendChild(binsEl); container.appendChild(status);
    var binEls = o.bins.map(function (name, b) {
      var count = h("span", { text: "0" });
      var el = h("button", { type: "button", "class": "w5-bin", "data-bin": b }, [h("span", { "class": "w5-binname" }, [h("span", { text: name }), count])]);
      el.addEventListener("click", function (e) {
        if (e.target.closest(".w5-card2")) return;
        if (picked < 0) { status.textContent = "Pick a card first, then tap “" + name + "”."; return; }
        put(picked, b);
      });
      binsEl.appendChild(el);
      return { el: el, count: count };
    });
    var cardEls = o.cards.map(function (c, i) {
      var el = h("button", { type: "button", "class": "w5-card2", "aria-pressed": "false", rich: c.text });
      el.addEventListener("click", function (e) {
        e.stopPropagation();
        if (el._dragged) { el._dragged = false; return; }
        picked = picked === i ? -1 : i;
        cardEls.forEach(function (x, j) { x.setAttribute("aria-pressed", j === picked ? "true" : "false"); });
        status.textContent = picked === i ? "Picked “" + strip(c.text) + "”. Now tap a bin." : "Put down “" + strip(c.text) + "”.";
      });
      el.addEventListener("pointerdown", function (e) {
        var sx = e.clientX, sy = e.clientY, ghost = null, over = -1;
        el.setPointerCapture(e.pointerId);
        function mv(ev) {
          if (!ghost && Math.hypot(ev.clientX - sx, ev.clientY - sy) < 7) return;
          if (!ghost) { ghost = el.cloneNode(true); ghost.classList.add("w5-ghost"); document.body.appendChild(ghost); }
          ghost.style.left = (ev.clientX - 30) + "px"; ghost.style.top = (ev.clientY - 18) + "px";
          over = -1;
          binEls.forEach(function (b, k) { var r = b.el.getBoundingClientRect(); var inside = ev.clientX > r.left && ev.clientX < r.right && ev.clientY > r.top && ev.clientY < r.bottom; b.el.classList.toggle("over", inside); if (inside) over = k; });
        }
        function up() {
          el.removeEventListener("pointermove", mv); el.removeEventListener("pointerup", up); el.removeEventListener("pointercancel", up);
          if (ghost) { ghost.remove(); el._dragged = true; binEls.forEach(function (b) { b.el.classList.remove("over"); }); if (over >= 0) put(i, over); setTimeout(function () { el._dragged = false; }, 0); }
        }
        el.addEventListener("pointermove", mv); el.addEventListener("pointerup", up); el.addEventListener("pointercancel", up);
      });
      return el;
    });
    function put(i, b) {
      place[i] = b; picked = -1;
      cardEls.forEach(function (x) { x.setAttribute("aria-pressed", "false"); x.classList.remove("right", "wrong"); });
      status.textContent = "Put “" + strip(o.cards[i].text) + "” in “" + o.bins[b] + "”.";
      render();
      if (o.onChange) o.onChange(place.slice());
    }
    function render() {
      cardEls.forEach(function (el, i) { (place[i] < 0 ? pool : binEls[place[i]].el).appendChild(el); });
      binEls.forEach(function (b, k) { b.count.textContent = String(place.filter(function (p) { return p === k; }).length); });
    }
    render();
    return {
      status: status, place: function () { return place.slice(); },
      mark: function () {
        var right = 0;
        cardEls.forEach(function (el, i) {
          var ok = place[i] === o.cards[i].bin; if (ok) right++;
          el.classList.toggle("right", place[i] >= 0 && ok); el.classList.toggle("wrong", place[i] >= 0 && !ok);
        });
        return right;
      },
      solve: function () { o.cards.forEach(function (c, i) { place[i] = c.bin; }); render(); }
    };
  };

  /* ================================================================ tabs (for case steps, scenes and interview situations) */
  function tabs(container, labels, onPick, word) {
    var bar = h("div", { "class": "w5-tabs", role: "tablist" });
    var note = h("span", { "class": "w5-pstate", style: { margin: "0 0 0 .3rem", alignSelf: "center" }, "aria-live": "polite" });
    var cur = 0;
    var btns = labels.map(function (lab, i) {
      var b = h("button", { type: "button", "class": "w5-tab", role: "tab", "aria-selected": i === 0 ? "true" : "false" },
        [lab.icon ? icon(lab.icon) : h("span", { "class": "w5-tabnum", text: String(i + 1) }), h("span", { text: lab.text })]);
      b.addEventListener("click", function () {
        if (i === cur) { note.textContent = lab.text + " is already open."; return; }
        cur = i;
        btns.forEach(function (x, j) { x.setAttribute("aria-selected", j === i ? "true" : "false"); });
        note.textContent = (word || "Showing") + " " + (i + 1) + " of " + labels.length + ".";
        onPick(i);
      });
      bar.appendChild(b);
      return b;
    });
    bar.appendChild(note);
    container.appendChild(bar);
    return { el: bar, pick: function (i) { if (i !== cur) btns[i].click(); } };
  }
  W5.tabs = tabs;

  /* ================================================================ page builders */
  function sectionOf(id) {
    var sec = document.querySelector("section[data-route='" + id + "']");
    if (!sec) lint("no <section data-route='" + id + "'> for this builder");
    return sec;
  }
  function head(sec, o, iconName) {
    var hd = h("header", { "class": "w5-head" });
    if (o.kicker) hd.appendChild(h("div", { "class": "w5-kicker" }, [icon(iconName || "how"), h("span", { text: o.kicker })]));
    if (!o.heading) lint("route " + sec.getAttribute("data-route") + " has no heading");
    else if (o.heading.indexOf("?") < 0) lint("the heading '" + o.heading + "' is not a question");
    hd.appendChild(h("h2", { rich: o.heading || "" }));
    if (o.lede) hd.appendChild(h("p", { "class": "w5-lede", rich: o.lede }));
    sec.appendChild(hd);
    return hd;
  }
  function dataBadge(o, where) {
    var d = o.data;
    if (!d) { lint("a stage on '" + where + "' does not say whether its numbers are invented, real or demo (data: 'invented' | 'real' | 'demo')"); return null; }
    if (d === "real" && !o.source) lint("a stage on '" + where + "' draws real numbers with no source named");
    var text = d === "invented" ? "Invented numbers, for teaching" : d === "demo" ? "Demo data" : "Real data: " + (o.source || "");
    return h("span", { "class": "w5-badge " + (d === "real" ? "real" : d === "demo" ? "demo" : "") }, [icon(d === "real" ? "table" : "sliders"), text]);
  }
  function stageApi(stageEl, controlsEl, readout, sayEl) {
    return {
      el: stageEl, controls: controlsEl, readout: readout,
      say: function (t) { if (sayEl) setRich(sayEl, t); },
      slider: function (o) { return W5.slider(controlsEl, o); },
      toggle: function (o) { return W5.toggle(controlsEl, o); },
      button: function (o) { return W5.button(controlsEl, o); },
      chart: function (o) { return W5.chart(stageEl, o); },
      cloud: function (o) { return W5.cloud(stageEl, o); },
      dotgrid: function (o) { return W5.dotgrid(stageEl, o); },
      matrix: function (o) { return W5.matrix(stageEl, o); },
      player: function (o) { return W5.player(stageEl, o); },
      svg: function (o) { return W5.svgStage(stageEl, o); },
      data: readData()
    };
  }
  function stageCard(container, o, where) {
    var card = h("div", { "class": "w5-card w5-stagecard" });
    var headRow = h("div", { "class": "w5-stagehead" }, [h("p", { "class": "w5-stagetitle", rich: o.stageTitle || "" }), dataBadge(o, where)]);
    var stage = h("div", { "class": "w5-stage" });
    var controls = h("div", { "class": "w5-controls" });
    var say = h("div", { "class": "w5-say", "aria-live": "polite" });
    card.appendChild(headRow); card.appendChild(stage); card.appendChild(controls); card.appendChild(say);
    container.appendChild(card);
    return { card: card, stage: stage, controls: controls, say: say };
  }

  W5.howItWorks = function (id, o) {
    var sec = sectionOf(id); if (!sec) return null;
    if (!o.kicker) lint(id + " has no kicker: the row's subtopic, verbatim");
    if (!o.predict) lint(id + " has no prediction card");
    if (!o.rule) lint(id + " has no rule card");
    if (!o.where || !o.where.deck || !o.where.notebook) lint(id + " has no footer naming the deck chapter and the notebook");
    head(sec, o, "how");
    var grid = h("div", { "class": "w5-hiw" });
    var left = h("div", { "class": "w5-col" }), right = h("div", { "class": "w5-col" });
    grid.appendChild(left); grid.appendChild(right);
    sec.appendChild(grid);
    var pr = o.predict ? W5.predict(right, o.predict) : null;
    var sc = stageCard(left, o, id);
    var ro = W5.readout(right, { title: o.readoutTitle });
    var api = stageApi(sc.stage, sc.controls, ro, sc.say);
    api.predict = pr;
    if (o.stage) o.stage(api);
    if (o.rule) W5.rule(sec, o.rule);
    if (o.where) W5.where(sec, o.where);
    return api;
  };

  W5.storyPage = function (id, o) {
    var sec = sectionOf(id); if (!sec) return null;
    if (!o.predict) lint("the story has no predict-then-reveal of its headline number");
    head(sec, o, "story");
    if (o.week) W5.weekline(sec, o.week);
    var grid = h("div", { "class": "w5-story" });
    var left = h("div", { "class": "w5-col" }), right = h("div", { "class": "w5-col" });
    grid.appendChild(left); grid.appendChild(right); sec.appendChild(grid);
    var sc = stageCard(left, o, id);
    var heroNum = h("span", { "class": "w5-heronum", text: "?" });
    var heroLab = h("span", { "class": "w5-herolabel", rich: (o.headline && o.headline.hidden) || "Commit a prediction to see the number." });
    var predictCfg = Object.assign({}, o.predict, {
      onReveal: function (st) {
        heroNum.textContent = o.headline ? o.headline.value : "";
        setRich(heroLab, o.headline ? o.headline.label : "");
        if (o.predict.onReveal) o.predict.onReveal(st);
        if (o.onReveal) o.onReveal(st);
      }
    });
    var pr = W5.predict(right, predictCfg);
    right.appendChild(h("div", { "class": "w5-card w5-hero" }, [h("div", { "class": "w5-label" }, [icon("flag"), (o.headline && o.headline.title) || "The headline number"]), heroNum, heroLab]));
    var ro = o.readout ? W5.readout(right, { title: o.readoutTitle }) : null;
    var scene = h("div", { "class": "w5-scene" });
    sc.stage.appendChild(scene);
    var api = stageApi(scene, sc.controls, ro, sc.say);
    api.predict = pr;
    if (o.setup) o.setup(api);
    if (o.scenes) {
      api.player = W5.player(sc.stage, { frames: o.scenes, word: "Scene", stepMs: o.stepMs || 900, holdMs: o.holdMs, render: function (i, p) {
        if (o.render) o.render(i, p, api);
      } });
    } else if (o.stage) o.stage(api);
    if (o.rule) W5.rule(sec, o.rule);
    return api;
  };

  W5.mapPage = function (id, o) {
    var sec = sectionOf(id); if (!sec) return null;
    head(sec, o, "map");
    var card = h("div", { "class": "w5-card" });
    sec.appendChild(card);
    var map = W5.conceptMap(card, o);
    if (o.predict) { var row = h("div", { style: { marginTop: "1rem" } }); sec.appendChild(row); map.predict = W5.predict(row, o.predict); }
    return map;
  };

  W5.casePage = function (id, o) {
    var sec = sectionOf(id); if (!sec) return null;
    head(sec, o, "case");
    var panes = [];
    var t = tabs(sec, o.steps.map(function (st) { return { text: st.chapter || st.title }; }), function (i) {
      panes.forEach(function (p, j) { p.hidden = j !== i; });
      relayout(panes[i], true);
    }, "Chapter");
    var apis = o.steps.map(function (st, i) {
      var pane = h("div", { hidden: i !== 0 });
      panes.push(pane); sec.appendChild(pane);
      pane.appendChild(h("h3", { "class": "w5-steptitle", rich: st.title }));
      if (st.applies && st.applies.length) {
        var ap = h("div", { "class": "w5-applies" });
        st.applies.forEach(function (a) { ap.appendChild(h("span", { "class": "w5-chip" }, [icon("layers"), a])); });
        pane.appendChild(ap);
      } else lint("case step '" + st.title + "' does not name the subtopics it applies");
      if (st.text) pane.appendChild(h("p", { "class": "w5-lede", rich: st.text, style: { marginBottom: ".8rem" } }));
      var grid = h("div", { "class": "w5-hiw" });
      var left = h("div", { "class": "w5-col" }), right = h("div", { "class": "w5-col" });
      grid.appendChild(left); grid.appendChild(right); pane.appendChild(grid);
      var pr = st.predict ? W5.predict(right, st.predict) : null;
      var sc = stageCard(left, Object.assign({ data: o.data, source: o.source }, st), id + " " + (st.chapter || ""));
      var ro = W5.readout(right, { title: st.readoutTitle });
      var api = stageApi(sc.stage, sc.controls, ro, sc.say);
      api.predict = pr;
      if (st.stage) st.stage(api);
      if (st.trap) api.trap = W5.trap(pane, st.trap);
      return api;
    });
    if (o.rule) W5.rule(sec, o.rule);
    return { steps: apis, tabs: t };
  };

  W5.trap = function (container, o) {
    ["wrong", "misled", "check", "fix"].forEach(function (k) { if (!o[k]) lint("a trap card has no '" + k + "'"); });
    var box = h("div", { "class": "w5-trap" });
    box.appendChild(h("div", { "class": "w5-label" }, [icon("alert"), o.title || "The trap, shown exactly"]));
    box.appendChild(h("div", { "class": "w5-trapnum" }, [h("b", { text: o.wrong }), h("span", { rich: o.context || "" })]));
    box.appendChild(h("p", {}, [h("b", { text: "The decision it would have misled: " }), rich(o.misled)]));
    var hold = h("div", {});
    box.appendChild(hold);
    var grid = h("div", { "class": "w5-trapgrid", hidden: true }, [
      h("div", {}, [h("div", { "class": "w5-label" }, [icon("magnifier"), "The check that catches it"]), h("div", { rich: o.check })]),
      h("div", {}, [h("div", { "class": "w5-label" }, [icon("implementation"), "The fix"]), h("div", { rich: o.fix })]),
      h("div", {}, [h("div", { "class": "w5-label" }, [icon("tick"), "The honest number"]), h("div", { rich: o.honest || "" })])
    ]);
    box.appendChild(grid);
    var pr = W5.predict(hold, {
      title: "Would you ship it?", q: o.q || "Is this number safe to put in front of the decision?",
      options: o.options || ["Yes, ship it", "No, something is wrong with it"], answer: o.answer !== undefined ? o.answer : 1,
      why: o.why || "", onReveal: function () { grid.hidden = false; box.classList.add("caught"); }
    });
    pr.el.classList.remove("w5-card");
    pr.el.style.padding = "0"; pr.el.style.borderLeft = "0"; pr.el.style.boxShadow = "none";
    container.appendChild(box);
    return { el: box, predict: pr };
  };

  var SEATS = [
    ["owner", "Business owner", "owner"], ["pm", "Product manager", "pm"], ["architect", "Solution architect", "architect"],
    ["ml", "Senior ML engineer", "ml"], ["implementation", "Implementation engineer", "implementation"], ["qa", "QA", "qa"]
  ];
  W5.seats = function (container, o) {
    SEATS.forEach(function (st) {
      if (!o.seats || !o.seats[st[0]] || !o.seats[st[0]].does || !o.seats[st[0]].asks) lint("the six seats need '" + st[0] + "' with 'does' and 'asks'");
    });
    var wrap = h("div", {});
    var seats = h("div", { "class": "w5-seats" });
    var wheel = h("div", { "class": "w5-wheel" }, [h("div", { "class": "w5-hub", rich: o.hub || "The idea" })]);
    var card = h("div", { "class": "w5-card w5-seatcard", "aria-live": "polite" });
    var btns = SEATS.map(function (st, i) {
      var a = -Math.PI / 2 + i * Math.PI / 3;
      var b = h("button", { type: "button", "class": "w5-seat", "aria-pressed": "false", style: { left: (50 + 40 * Math.cos(a)) + "%", top: (50 + 40 * Math.sin(a)) + "%" } },
        [h("span", { "class": "w5-seatico" }, [icon(st[2])]), h("span", { text: st[1] })]);
      b.addEventListener("click", function () { pick(i); });
      wheel.appendChild(b);
      return b;
    });
    function pick(i) {
      btns.forEach(function (b, j) { b.setAttribute("aria-pressed", j === i ? "true" : "false"); });
      var st = SEATS[i], d = (o.seats && o.seats[st[0]]) || {};
      card.textContent = "";
      card.appendChild(h("div", { "class": "w5-label" }, [icon(st[2]), "Seat " + (i + 1) + " of 6"]));
      card.appendChild(h("h4", { text: st[1] }));
      card.appendChild(h("p", { rich: d.does || "" }));
      card.appendChild(h("p", { "class": "w5-seatq", rich: d.asks || "" }));
    }
    card.appendChild(h("div", { "class": "w5-label" }, [icon("users"), "Six seats, one idea"]));
    card.appendChild(h("p", { rich: o.intro || "Pick a seat on the wheel to read what that person does with today's idea and the question they ask about it." }));
    seats.appendChild(wheel); seats.appendChild(card);
    wrap.appendChild(seats);
    var all = h("div", { "class": "w5-allseats", hidden: true });
    SEATS.forEach(function (st) {
      var d = (o.seats && o.seats[st[0]]) || {};
      all.appendChild(h("div", { "class": "w5-card" }, [h("h4", {}, [icon(st[2]), st[1]]), h("p", { rich: d.does || "" }), h("p", { "class": "w5-seatq", rich: d.asks || "" })]));
    });
    var allBtn = W5.button(null, { label: "Show all six at once", icon: "users", quiet: true, onClick: function (e, b) {
      all.hidden = !all.hidden;
      b.lastChild.textContent = all.hidden ? "Show all six at once" : "Hide the six cards";
    } });
    wrap.appendChild(h("div", { style: { marginTop: ".8rem" } }, [allBtn]));
    wrap.appendChild(all);
    container.appendChild(wrap);
    return { el: wrap, pick: pick };
  };

  W5.fieldPage = function (id, o) {
    var sec = sectionOf(id); if (!sec) return null;
    head(sec, o, "field");
    var panes = [];
    var t = tabs(sec, o.scenes.map(function (sc) { return { text: sc.company, icon: sc.icon || "field" }; }), function (i) {
      panes.forEach(function (p, j) { p.hidden = j !== i; });
      relayout(panes[i], true);
    }, "Scene");
    var apis = o.scenes.map(function (sc, i) {
      var src = parseSource(sc.source);
      if (!src.checked) lint("the scene '" + sc.company + "' needs a source line ending 'checked <day> <month> <year>'");
      var pane = h("div", { hidden: i !== 0 });
      panes.push(pane); sec.appendChild(pane);
      var grid = h("div", { "class": "w5-hiw" });
      var left = h("div", { "class": "w5-col" }), right = h("div", { "class": "w5-col" });
      grid.appendChild(left); grid.appendChild(right); pane.appendChild(grid);
      var story = h("div", { "class": "w5-card" }, [
        h("div", { "class": "w5-company" }, [h("span", { "class": "w5-cico" }, [icon(sc.icon || "field")]), h("span", {}, [h("span", { "class": "w5-cname2", text: sc.company }), h("br"), h("span", { "class": "w5-cangle", text: sc.angle || "" })])]),
        h("h3", { rich: sc.title }), h("p", { rich: sc.situation || "" })
      ]);
      if (sc.source) {
        story.appendChild(h("div", { "class": "w5-src" }, [icon("ledger"), h("span", {}, [h("b", { text: "Source: " }), rich(src.name + (src.checked ? ", checked " + src.checked : "")),
          src.url ? h("span", {}, [". ", h("a", { href: src.url, target: "_blank", rel: "noopener", text: src.url })]) : null])]));
      }
      right.appendChild(story);
      var pr = sc.predict ? W5.predict(right, sc.predict) : null;
      var stc = stageCard(left, Object.assign({}, sc, { data: sc.data || "real", source: sc.company }), id + " " + sc.company);
      var ro = W5.readout(right, { title: sc.readoutTitle });
      right.insertBefore(ro.el, pr ? pr.el.nextSibling : story.nextSibling);
      var api = stageApi(stc.stage, stc.controls, ro, stc.say);
      api.predict = pr;
      if (sc.stage) sc.stage(api);
      return api;
    });
    var seatsApi = null;
    if (o.seats) {
      sec.appendChild(h("h3", { "class": "w5-steptitle", style: { marginTop: "1.6rem" }, rich: o.seatsHeading || "Six seats: what does each person do with this idea?" }));
      seatsApi = W5.seats(sec, o.seats);
    } else lint("the field page has no six seats");
    return { scenes: apis, seats: seatsApi, tabs: t };
  };

  function parseSource(text) {
    text = String(text || "");
    var url = (text.match(/https?:\/\/[^\s,)]+/) || [""])[0];
    var checked = (text.match(/checked\s+(\d{1,2}\s+\w+\s+\d{4})/i) || [null, ""])[1];
    var name = text.replace(url, "").replace(/,?\s*checked\s+\d{1,2}\s+\w+\s+\d{4}/i, "").replace(/[\s,]+$/, "").replace(/,\s*,/g, ",");
    return { name: name, url: url, checked: checked };
  }
  W5.parseSource = parseSource;

  var KIND_ICON = { technical: "ml", "techno-functional": "architect", scenario: "case", "client-facing": "users" };
  W5.interviewPage = function (id, o) {
    var sec = sectionOf(id); if (!sec) return null;
    head(sec, o, "interview");
    if (o.items.length < 4 || o.items.length > 6) console.warn("w5kit: the interview room asks for four to six situations; this page has " + o.items.length);
    var panes = [];
    var t = tabs(sec, o.items.map(function (it, i) { return { text: "Situation " + (i + 1) }; }), function (i) {
      panes.forEach(function (p, j) { p.hidden = j !== i; });
      relayout(panes[i], true);
    }, "Situation");
    var apis = o.items.map(function (it, i) {
      ["question", "clarify", "steps", "answer", "model", "followups", "wrong"].forEach(function (k) { if (!it[k]) lint("interview situation " + (i + 1) + " has no '" + k + "'"); });
      if (it.followups && it.followups.length !== 2) lint("interview situation " + (i + 1) + " needs exactly two follow-ups");
      var pane = h("div", { "class": "w5-iv", hidden: i !== 0 });
      panes.push(pane); sec.appendChild(pane);
      pane.appendChild(h("div", { "class": "w5-ivq" }, [h("span", { "class": "w5-ivico" }, [icon(KIND_ICON[it.kind] || "interview")]),
        h("span", { "class": "w5-ivkind", text: (it.kind || "technical") + (it.company ? " · " + it.company : "") }),
        h("p", { "class": "w5-ivtext", rich: it.question || "" })]));
      var steps = h("div", { "class": "w5-ivsteps" });
      pane.appendChild(steps);
      function stepCard(n, title) {
        var c = h("div", { "class": "w5-card w5-ivstep" }, [h("h3", {}, [h("span", { "class": "w5-stepno", text: String(n) }), title])]);
        steps.appendChild(c); return c;
      }
      var c1 = stepCard(1, "Ask the clarifying question");
      var clar = W5.predict(c1, { title: "Which question do you ask first?", q: it.clarify ? it.clarify.q || "Before answering, which one question would you ask?" : "", options: it.clarify ? it.clarify.options : [], answer: it.clarify ? it.clarify.best : 0, why: it.clarify ? it.clarify.why : "", skipLabel: "Show the best question" });
      plain(clar);
      var c2 = stepCard(2, "Order the whiteboard steps");
      var ol = W5.orderList(c2, { items: it.steps || [], seed: 11 + i * 7 });
      var markLine = h("p", { "class": "w5-pstate", "aria-live": "polite" });
      var checkBtn = W5.button(null, { label: "Check my order", icon: "tick", onClick: function () {
        var k = ol.mark();
        markLine.textContent = k + " of " + ol.order().length + " steps are in the right place." + (k === ol.order().length ? " That is the order an interviewer listens for." : " The model answer below draws the order step by step.");
      } });
      c2.appendChild(h("div", { "class": "w5-pbtns" }, [checkBtn])); c2.appendChild(markLine);
      var c3 = stepCard(3, "Commit your answer");
      var ans = W5.predict(c3, { title: "Your answer", q: it.answer ? it.answer.q || "Which answer would you give?" : "", options: it.answer ? it.answer.options : [], answer: it.answer ? it.answer.best : 0, why: it.answer ? it.answer.why : "", skipLabel: "Skip to the model answer" , onReveal: function () { showModel(true); } });
      plain(ans);
      var model = h("div", { "class": "w5-card w5-model", hidden: true });
      var showBtn = W5.button(null, { label: "Show the model answer", icon: "eye", primary: true, onClick: function () { showModel(false); } });
      var note = h("p", { "class": "w5-pstate", "aria-live": "polite" });
      pane.appendChild(h("div", {}, [showBtn, note]));
      pane.appendChild(model);
      var built = false, boardPlayer = null;
      function showModel(fromAnswer) {
        if (!ans.state.committed && !fromAnswer) note.textContent = "You opened the model answer before committing your own, so compare as you read.";
        else note.textContent = "Here is the answer an interviewer hopes to hear, built step by step.";
        showBtn.hidden = true;
        model.hidden = false;
        if (built) return;
        built = true;
        model.appendChild(h("div", { "class": "w5-label" }, [icon("quote"), "The 30-second answer"]));
        model.appendChild(h("p", { "class": "w5-thirty", rich: it.model || "" }));
        var board = h("div", { "class": "w5-board" });
        var boardSteps = (it.board || (it.steps || []).map(function (st) { return { title: st }; }));
        var stepEls = boardSteps.map(function (b, k) {
          var el = h("div", { "class": "w5-bstep off" }, [
            k ? h("span", { "class": "w5-barrow", "aria-hidden": "true" }, [icon("arrowRight")]) : null,
            h("div", { "class": "w5-bbox" }, [h("div", { "class": "w5-btitle" }, [b.icon ? icon(b.icon) : null, h("span", { rich: b.title })]), b.note ? h("div", { "class": "w5-bnote", rich: b.note }) : null])]);
          board.appendChild(el);
          return el;
        });
        var bw = h("div", { "class": "w5-boardwrap" }, [h("div", { "class": "w5-label" }, [icon("chart"), "The whiteboard, step by step"]), board]);
        model.appendChild(bw);
        boardPlayer = W5.player(bw, { frames: [{ caption: "The board starts empty. Press play, or step, to draw the answer the way you would say it." }].concat(boardSteps.map(function (b, k) { return { caption: b.say || ("Step " + (k + 1) + ": " + strip(b.title) + (b.note ? ". " + strip(b.note) : "")) }; })),
          word: "Board step", stepMs: 500, holdMs: 1100, render: function (k) { stepEls.forEach(function (el, j) { el.classList.toggle("off", j >= k); }); } });
        var lower = h("div", { "class": "w5-ivgrid", style: { marginTop: ".9rem" } });
        var fu = h("div", {}, [h("div", { "class": "w5-label" }, [icon("interview"), "The interviewer's two follow-ups"])]);
        var ul = h("ol", { "class": "w5-follow" });
        (it.followups || []).forEach(function (f) { ul.appendChild(h("li", { rich: f })); });
        fu.appendChild(ul);
        var wr = h("div", {}, [h("div", { "class": "w5-label", style: { color: "#A3214B" } }, [icon("cross"), "This room's usual wrong answers"])]);
        var wl = h("div", { "class": "w5-wrongs" });
        (it.wrong || []).forEach(function (w) { wl.appendChild(h("div", {}, [h("s", { rich: w.text }), h("span", { "class": "w5-why", rich: w.why })])); });
        wr.appendChild(wl);
        lower.appendChild(fu); lower.appendChild(wr);
        model.appendChild(lower);
      }
      function plain(p) { p.el.classList.remove("w5-card"); p.el.style.padding = "0"; p.el.style.border = "0"; p.el.style.boxShadow = "none"; }
      return { pane: pane, clarify: clar, order: ol, answer: ans, showModel: showModel, board: function () { return boardPlayer; } };
    });
    return { items: apis, tabs: t };
  };

  var CHECK_TYPES = { number: "Predict a number", pick: "Pick one", order: "Put in order", bins: "Sort into bins" };
  W5.checkPage = function (id, o) {
    var sec = sectionOf(id); if (!sec) return null;
    head(sec, o, "check");
    if (o.items.length < 6 || o.items.length > 8) console.warn("w5kit: check yourself asks for six to eight items; this page has " + o.items.length);
    var results = o.items.map(function () { return null; });
    var scoreB = h("b", { text: "0" });
    var scoreText = h("span", { text: " right out of " + o.items.length + ". Nothing checked yet." });
    sec.appendChild(h("div", { "class": "w5-score", "aria-live": "polite" }, [icon("check"), h("span", {}, [scoreB, scoreText])]));
    function score() {
      var done = results.filter(function (r) { return r !== null; }).length, right = results.filter(function (r) { return r === true; }).length;
      scoreB.textContent = String(right);
      scoreText.textContent = " right out of " + o.items.length + ", with " + done + " checked so far.";
    }
    var list = h("div", { "class": "w5-checks" });
    sec.appendChild(list);
    var apis = o.items.map(function (it, i) {
      if (!CHECK_TYPES[it.type]) lint("check item " + (i + 1) + " has an unknown type '" + it.type + "'; use number, pick, order or bins");
      var card = h("div", { "class": "w5-card w5-check" });
      card.appendChild(h("p", { "class": "w5-cnum" }, ["Check " + (i + 1), h("span", { "class": "w5-ctype", text: CHECK_TYPES[it.type] || "" })]));
      card.appendChild(h("p", { "class": "w5-cq", rich: it.q }));
      if (it.figure) { var fig = h("div", { "class": "w5-figure" }); card.appendChild(fig); it.figure(fig); }
      list.appendChild(card);
      var why = h("div", { "class": "w5-reveal", hidden: true });
      function done(ok, text) {
        results[i] = ok; score();
        why.hidden = false; why.textContent = "";
        why.appendChild(h("p", { "class": "w5-verdict " + (ok ? "right" : "wrong") }, [icon(ok ? "tick" : "cross"), h("span", { text: text })]));
        if (it.why) why.appendChild(h("p", { rich: it.why }));
      }
      if (it.type === "number" || it.type === "pick") {
        var p = W5.predict(card, { title: " ", q: "", type: it.type === "number" ? "number" : "choice", options: it.options, answer: it.answer, tolerance: it.tolerance, unit: it.unit, fmt: it.fmt, why: it.why,
          skipLabel: "Show the answer", onReveal: function (st) { results[i] = st.committed ? st.right : false; score(); } });
        p.el.classList.remove("w5-card"); p.el.style.padding = "0"; p.el.style.border = "0"; p.el.style.boxShadow = "none";
        p.el.querySelector(".w5-label").remove(); p.el.querySelector(".w5-pq").remove();
        p.el.querySelector(".w5-pbtns .w5-btn.primary span").textContent = "Check";
        return p;
      }
      var widget = it.type === "order" ? W5.orderList(card, { items: it.items, seed: 5 + i }) : W5.bins(card, { bins: it.bins, cards: it.cards });
      var btn = W5.button(null, { label: "Check", icon: "tick", primary: true, onClick: function () {
        var k = widget.mark(), total = it.type === "order" ? it.items.length : it.cards.length;
        done(k === total, k + " of " + total + " in the right place." + (k === total ? " All right." : " Read why below, then move the rest."));
      } });
      card.appendChild(h("div", { "class": "w5-pbtns" }, [btn]));
      card.appendChild(why);
      return widget;
    });
    if (o.map) {
      sec.appendChild(h("h3", { "class": "w5-steptitle", style: { marginTop: "1.6rem" }, rich: o.mapHeading || "Where does today sit now that you have climbed it?" }));
      var mc = h("div", { "class": "w5-card" }); sec.appendChild(mc);
      W5.conceptMap(mc, Object.assign({ player: false }, o.map));
    }
    if (o.tomorrow) sec.appendChild(h("div", { "class": "w5-tomorrow" }, [h("div", { "class": "w5-label" }, [icon("calendar"), "Tomorrow's question"]), h("p", { rich: o.tomorrow })]));
    else lint("check yourself does not end on tomorrow's question");
    return { items: apis };
  };

  /* A generic route for anything the builders do not cover: the head, then an empty body to fill. */
  W5.route = function (id, o) {
    var sec = sectionOf(id); if (!sec) return null;
    head(sec, o, ROUTE_META[id] ? ROUTE_META[id].icon : "how");
    var body = h("div", {}); sec.appendChild(body);
    return body;
  };

  /* ================================================================ hooks for the screenshot script */
  W5.debug = {
    finishAll: finishAll,
    endState: function (scope) {
      scope = scope || (app.current && app.current.el) || document;
      revealers.forEach(function (r) { if (scope.contains(r.el)) r.reveal(); });
      app.players.forEach(function (p) { if (scope.contains(p.el)) p.end(); });
      finishAll();
    }
  };
})();
