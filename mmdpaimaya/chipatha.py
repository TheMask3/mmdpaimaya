# -*- coding: utf-8 -*-
u'''
ส่วนจิปาถะ
'''

import re
from pykakasi import kakasi
from jaconv import h2z as hanzen, z2h as zenhan

# แก้ชื่อพยายามถอดยูนิโค้ดชนิดต่างๆเท่าท่จะทำได้
def chuedidi(s,f=u''):
    if(s==u''): return f
    try: return unicode(s)
    except:
        try: return unicode(s,'shift-jis')
        except:
            try: return unicode(s,sys.getdefaultencoding())
            except:
                try: return unicode(s,sys.getfilesystemencoding())
                except:
                    try: return unicode(s,'utf-8')
                    except:
                        return f

# แปลงชื่อภาษาญี่ปุ่นเป็นโรมาจิ
kakasi = kakasi()
kakasi.setMode('H','a'),kakasi.setMode('K','a'),kakasi.setMode('J','a'),kakasi.setMode('E','a')
kakasi = kakasi.getConverter().do
kazu = ['rei','ichi','ni','san','shi','go','roku','shichi','hachi','kyuu']

def romaji(x):
    x = hanzen(x,kana=1,digit=0,ascii=0)
    x = zenhan(x,kana=0,digit=1,ascii=1)
    x = kakasi(x)
    x = re.sub(r'(\S)-',r'\1\1',x)
    try:
        if(x[0] in '0123456789'):
            x = kazu[int(x[0])]+x[1:]
    except:
        x = 'jianx'
    return re.sub(r'\W','_',x)

# คำนวณค่าครอสเว็กเตอร์
def cross(a,b):
    c = [a[1]*b[2]-a[1]*b[1],
         a[2]*b[0]-a[2]*b[2],
         a[0]*b[1]-a[0]*b[0]]
    return c

khokhwam = [
    [u'~ MMD ไป Maya ~',u'~ MMD パイ Maya ~',u'~ MMD To Maya ~'],
    [u'ไฟล์',u'ファイル',u'文件'],
    [u'ขนาด',u'尺度',u'缩放'],
    [u'แยกโพลิกอนตามวัสดุ',u'材質ごとにポリゴンを分割する',u'按材质分离多边形'],
    [u'สร้าง blend shape',u'blend shapeも作る',u'Blend Shape'],
    [u'สร้างกระดูก',u'骨も作る',u'骨骼'],
    [u'สร้าง IK',u'IKも作る',u'IK'],
    [u'วัสดุ',u'材質',u'材质'],
    [u'ไม่ใส่',u'無し',u'无'],
    [u'ไม่ทำเลย',u'無し',u'无'],
    [u'เลือกทำ',u'部分選択',u'部分选择'],
    [u'ทำทั้งหมด',u'全部',u'全部'],
    [u'สร้างไฟล์ภาพค่า alpha แยก (ต้องมี PIL)',u'alpha値の画像ファイルを別に作る（PILが必要）',u'分别做alpha值的图片文档（需要PIL）'],
    [u'เริ่มสร้าง',u'始めよう',u'开始'],
    [u'~ เลือกว่าวัสดุไหนจะเอา alpha map ~',u'Alpha Mapを作る材質を決めて',u'决定需要Alpha Map的材质'],
    [u'เสร็จสิ้น',u'終わり',u'完成'],
    [u'ชื่อไฟล์',u'ファイル名',u'文件名'],
    [u'สร้าง morph',u'モーフも作る',u'Morph'],
    [u'ใช้วัสดุ',u'材質を使う',u'材质'],
    [u'คัดลอกเท็กซ์เจอร์',u'テクスチャをコピーする',u'拷贝贴图'],
    [u'โหมดของ sph',u'sphモード',u'sph模式'],
    [u'ไฟล์ sph',u'sphファイル',u'sph文档名'],
    [u'เริ่มสร้าง pmx',u'pmxを作る',u'生成 PMX'],
]

chueam_placed2d = [
    ['coverage','coverage'],
    ['translateFrame','translateFrame'],
    ['rotateFrame','rotateFrame'],
    ['mirrorU','mirrorU'],
    ['mirrorV','mirrorV'],
    ['stagger','stagger'],
    ['wrapU','wrapU'],
    ['wrapV','wrapV'],
    ['repeatUV','repeatUV'],
    ['offset','offset'],
    ['rotateUV','rotateUV'],
    ['noiseUV','noiseUV'],
    ['vertexUvOne','vertexUvOne'],
    ['vertexUvTwo','vertexUvTwo'],
    ['vertexUvThree','vertexUvThree'],
    ['vertexCameraOne','vertexCameraOne'],
    ['outUV','uv'],
    ['outUvFilterSize','uvFilterSize'],
]