"""Presentation-only layouts for the three reviewed teaching examples."""
from pathlib import Path
ROOT = Path(__file__).resolve().parent

def panel_title(title, sources):
    return f'<header class="panel-title"><b>{title}</b><small>{sources}</small></header>'

def chip(text):
    return '<span class="part">'+text+'</span>'

def graphic_board(rows):
    board=(ROOT/'figures/pixhawk-logic.svg').read_text()
    groups=[('板載','處理器 加速度計 陀螺儀 磁力計 氣壓計'),('外接介面','遙測埠 GPS埠 遙控輸入')]
    labels=''.join('<div class="part-group"><h3>'+title+'</h3><div>'+''.join(chip(part) for part in parts.split())+'</div></div>' for title,parts in groups)
    return (panel_title('板載與外接的邏輯架構','S01 · S02')+
            '<div class="board-layout"><figure class="board-grid">'+board+
            '<figcaption>功能分層示意 · 不表示實際接腳或元件位置</figcaption></figure>'+
            '<div class="parts">'+labels+'</div></div>'),rows

def graphic_modes(rows):
    labels=['姿態與水平桿','高度','水平位置']
    values=[('Stabilize','姿態穩定','桿回中時回平','飛手控制','飛手修正'),
            ('AltHold','高度保持','桿回中時回平','油門中立區定高','飛手修正'),
            ('Loiter','位置保持','水平桿調整位置','嘗試維持高度','嘗試定點¹')]
    buttons=''.join(f'<button type="button" data-col="{i}" aria-pressed="false">{t}</button>' for i,t in enumerate(labels,1))
    head=''.join('<th scope="col">'+t+'</th>' for t in labels)
    body=''
    for mode,cn,*cells in values:
        body+=f'<tr><th scope="row"><b>{mode}</b><small>{cn}</small></th>'+''.join('<td>'+v+'</td>' for v in cells)+'</tr>'
    cards=[]
    for mode,cn,*cells in values:
        details=''.join(f'<div data-field="{i}"><dt>{label}</dt><dd>{value}</dd></div>'
                        for i,(label,value) in enumerate(zip(labels,cells),1))
        cards.append(f'<section><h3>{mode} <small>{cn}</small></h3><dl>{details}</dl></section>')
    mobile='<div class="mobile-modes">'+''.join(cards)+'</div>'
    matrix=(panel_title('三種模式的控制分工','S03 · S04 · S05 · S06')+
            '<div class="focus-cols" aria-label="強調比較欄位"><span>強調欄位</span>'+buttons+'</div>'+
            '<table class="mode-matrix" aria-label="姿態、高度與水平位置控制分工"><thead><tr><th scope="col">模式</th>'+head+'</tr></thead><tbody>'+body+
            '</tbody></table>'+mobile+'<p class="condition"><b>¹ 定點條件</b>　Loiter 需要有效的水平位置估測。</p>')
    return matrix,rows

def graphic_case(rows):
    return (panel_title('從地面站訊息查對官方條目','S07')+
            '<div class="error-sample"><span class="warn-icon" aria-hidden="true">!</span><div><small>官方文件範例 · 解鎖前檢查</small><code>3D Accel calibration needed</code></div></div>'+
            '<div class="lookup"><div><small>官方錯誤表　S07.4</small><b>查相同的完整訊息</b></div><span class="arrow" aria-hidden="true">→</span><div><small>對應原因</small><b>加速度計尚未完成校正</b></div></div>'),rows

LAYOUTS={'03':graphic_board,'06':graphic_modes,'10':graphic_case}
def teaching_body(page,rows):
    graphic,rows=LAYOUTS[page](rows)
    return '<div class="tech-panel">'+graphic+'</div><div class="rows">'+rows+'</div>'
