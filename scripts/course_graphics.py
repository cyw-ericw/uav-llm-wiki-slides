"""Original offline diagrams for the complete course, derived from the approved cards."""
from pathlib import Path
from batch_one import panel_title

QUAD = (Path(__file__).parent / 'figures/quad-body.svg').read_text()

def course_map():
    chapters = [('02','硬體與感測','辨認飛控與估測來源'),('06','三種飛行模式','對照姿態、高度與位置'),('10','解鎖前檢查','用完整訊息查原因')]
    links=''.join(f'<a href="#p{page}"><small>第 {page} 頁起</small><strong>{title}</strong><span>{detail} ↗</span></a>' for page,title,detail in chapters)
    drawing=f'<svg viewBox="0 0 300 130" aria-hidden="true"><g fill="none" stroke="#4d6157"><ellipse cx="150" cy="85" rx="109" ry="25"/><ellipse cx="150" cy="85" rx="72" ry="16"/><path d="M15 85h269M150 14v100" stroke-dasharray="2 5"/></g><g transform="translate(150 52) scale(1.3)">{QUAD}</g></svg>'
    return '<div class="atlas"><header><div><small>UAV LAB / FIELD GUIDE</small><h2>課程地圖</h2></div>'+drawing+'</header><nav aria-label="課程章節">'+links+'</nav></div>'

def hardware():
    return panel_title('先辨認硬體，再確認韌體','S01 · S02 · S03')+'''<div class="pair">
    <div><small>HARDWARE</small><strong>Pixhawk 6C</strong><p>處理器、板載感測器與外接介面</p><footer>查 Holybro 硬體規格</footer></div>
    <span aria-hidden="true">⇄</span><div><small>FIRMWARE</small><strong>飛控程式</strong><p>以目前安裝的韌體辨認模式行為</p><footer>使用 Copter 時查 ArduPilot 文件</footer></div></div>'''

def sensors():
    items=[('IMU','慣性量測單元','加速度計 ＋ 陀螺儀'),('MAG','磁力計','羅盤 → 航向估測'),('BARO','氣壓計','氣壓 → 高度估測')]
    return panel_title('感測器與它提供的線索','S02 · S08')+'<dl class="sensor-list">'+''.join(f'<div><dt><small>{abbr}</small>{name}</dt><dd>{use}</dd></div>' for abbr,name,use in items)+'</dl>'

def ekf():
    lanes=[('氣壓計','氣壓資料','垂直位置','預設來源'),('羅盤','航向參考','航向','通常預設'),('光流','水平速度資料','水平速度','官方配置範例')]
    rows=''.join(f'<li><div><strong>{sensor}</strong><small>{measure}</small></div><i aria-hidden="true"></i><div><strong>{state}</strong><small>{note}</small></div></li>' for sensor,measure,state,note in lanes)
    return panel_title('EKF3 的量測資料流','S08.1 · S08.3 · S08.4')+f'''<div class="fusion">
    <div class="lanes"><div class="lane-head"><b>量測來源</b><b>對應估測項目</b></div><ul>{rows}</ul></div>
    <span class="bus" aria-hidden="true"></span>
    <div class="estimator"><small>狀態估測</small><strong>EKF3</strong><p>依配置取用量測，更新飛行狀態。</p></div></div>
    <p class="condition"><b>光流範例</b>　水平速度是輸入；該配置的水平位置是估出的相對位置。</p>'''

SCENES={
 '07':('Stabilize','姿態回平','橫滾、俯仰桿回中','飛控使機身回平，水平位置仍可能漂移。','S04.1 · S04.2'),
 '08':('AltHold','高度保持','油門桿回到中立區','飛控嘗試維持目前高度，水平位置仍由飛手修正。','S05.1 · S05.3'),
 '09':('Loiter','位置保持','位置估測有效、水平桿回中','減速後嘗試維持水平位置。圖中十字標示這次的定點。','S03.2 · S06.1–3 · S08.3')
}

def mode_scene(page):
    mode,feature,condition,detail,facts=SCENES[page]
    x=146 if page=='09' else 324
    ghost=''
    if page!='09':
        tilt=-17 if page=='07' else 0
        ghost=f'<g opacity=".37" transform="translate(146 88) rotate({tilt})">{QUAD}</g>'
    if page=='07':
        guides='<path class="trace" d="M215 95 Q235 112 255 98m-8 0 8 0 -2 7"/><path class="datum" d="M261 89h126"/>'
    elif page=='08':
        guides='<path class="datum" d="M42 88h382"/><path class="trace" d="M99 92v81m-6 -81h12m-12 81h12"/>'
    else:
        guides='<path class="datum" d="M42 88h218M146 105v64"/><ellipse class="trace" cx="146" cy="178" rx="33" ry="8"/>'
    grid=''.join(f'<path d="M{j} 147l-46 55"/>' for j in range(-20,550,32))
    svg=f'''<svg class="flight-view" viewBox="0 0 460 205" role="img" aria-label="{mode}，{detail}">
    <g fill="none" stroke="#34454b" stroke-width=".85">{grid}<path d="M0 149h460M0 158h460M0 171h460M0 189h460M0 202h460"/></g>
    <g fill="none" stroke="#bfcfc5" stroke-width="1.7"><ellipse cx="146" cy="178" rx="18" ry="5"/><path d="M122 178h48m-24 -8v16"/></g>
    {guides}{ghost}<g transform="translate({x} 88)">{QUAD}</g></svg>'''
    legend={'07':'淡色為傾斜姿態，亮色為回平後可能的位置。','08':'水平虛線標示保持高度；兩架輪廓示意同機的不同位置。','09':'垂直虛線連接機體與地面定點。'}[page]
    return panel_title('同一架四旋翼｜'+feature,facts)+f'<div class="flight-split"><figure>{svg}<figcaption>地面十字為共同參考點。{legend}</figcaption></figure><div class="flight-note"><small>{mode}</small><h2>{feature}</h2><b>{condition}</b><p>{detail}</p></div></div>'

def recap():
    links=[('07','回平','Stabilize'),('08','定高','AltHold'),('09','定點','Loiter')]
    return panel_title('回看三種保持行為','S04 · S05 · S06')+'<nav class="recap" aria-label="回看模式圖解">'+''.join(f'<a href="#p{page}"><small>{mode}</small><strong>{feature}</strong><span>回看第 {page} 頁 ↗</span></a>' for page,feature,mode in links)+'</nav>'

def course_body(page, rows):
    if page in SCENES:
        graphic=mode_scene(page)
    else:
        graphic={'01':course_map,'02':hardware,'04':sensors,'05':ekf,'11':recap}[page]()
    return '<div class="tech-panel">'+graphic+'</div><div class="rows">'+rows+'</div>'
