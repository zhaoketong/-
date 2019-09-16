
def write_xlwt(ws):
    first_col=ws.col(0)
    sec_col=ws.col(1)
    four_col=ws.col(4)
    first_col.width=256*15
    sec_col.width = 256*70
    four_col.width = 256*70
    ws.write(0, 0, '商品基本信息')
    ws.write(0, 3, '品牌基本字段')
    ws.write(1, 0, '字段名称')
    ws.write(1, 1, '字段示例说明')
    ws.write(1, 3, '字段名称')
    ws.write(1, 4, '字段示例说明')
    ws.write(2, 0, '商品中文标题')
    ws.write(3, 0, '商品英文标题')
    ws.write(4, 0, '分类')
    ws.write(5, 0, '系列')
    ws.write(6, 0, '型号(色号,香型)')
    ws.write(7, 0, '容量/规格')
    ws.write(8, 0, '价格')
    ws.write(9, 0, '主图片(大图)')
    ws.write(10, 0, '小图')
    ws.write(11, 0, '产品宣称')
    ws.write(12, 0, '产品描述')
    ws.write(13, 0, '使用方法')
    ws.write(14, 0, '注意事项')
    ws.write(15, 0, '产品质地/形态')
    ws.write(16, 0, '适用人群')
    ws.write(17, 0, '主要功效')
    ws.write(18, 0, '彩妆类产品')
    ws.write(19, 0, '产品链接')

    ws.write(2, 3, '品牌名称')
    ws.write(3, 3, 'logo')
    ws.write(4, 3, '描述')
    ws.write(5, 3, '官网链接')
    ws.write(6, 3, '品牌汇总')
    ws.write(7, 3, '品牌slogon')
    ws.write(8, 3, '品牌故事')

def save(xls,name):
    xls.save('./proya_list/%s.xls'%name)















