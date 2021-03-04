import requests
import xlwt

file = xlwt.Workbook()
nation_list = []

table = file.add_sheet('sheet1', cell_overwrite_ok = True)

table.write( 0, 0, "排名")
table.write( 0, 1, "电影中文名")
table.write( 0, 2, "电影其他名")
table.write( 0, 3, "时间")
table.write( 0, 4, "导演")
table.write( 0, 5, "国家或地区")
table.write( 0, 6, "评分")
table.write( 0, 7, "评分人数")
table.write( 0, 8, "电影类型")
table.write( 0, 9, '代表性评论')
# for i in range(len(nation_list)):
#     table.write(i + 1, 0, i + 1)
#     table.write(i + 1, 1, movie_list_chinese_name[i])
#     table.write(i + 1, 2, movie_list_english_name[i])
#     table.write(i + 1, 3, time_list[i])
#     table.write(i + 1, 4, director_list[i])
#     table.write(i + 1, 5, nation_list[i])
#     table.write(i + 1, 6, star_list[i])
#     table.write(i + 1, 7, reviewNum_list[i])
#     table.write(i + 1, 8, category_list[i])
#     table.write(i + 1, 9, quote_list[i])
#      # 导出到 xls 文件里   
file.save('豆瓣 top 10 电影爬虫抓取.xls')
print("保存完成")