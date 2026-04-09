from pathlib import Path
import re

path = Path("legal_texts/china_privacy_protection_law.txt")
lines = path.read_text(encoding="utf-8", errors="replace").splitlines()

# 统计各类行数
empty = sum(1 for l in lines if not l.strip())
chapter = sum(1 for l in lines if re.match(r"^第[一二三四五六七八九十百]+章", l.strip()))
section = sum(1 for l in lines if re.match(r"^第[一二三四五六七八九十百]+节", l.strip()))
toc = sum(1 for l in lines if l.strip() in ["目　　录", "中华人民共和国个人信息保护法"])
date = sum(1 for l in lines if re.match(r"^（\d{4}年", l.strip()))
list_item = sum(1 for l in lines if re.match(r"^（[一二三四五六七八九十百]+）", l.strip()))
article = sum(1 for l in lines if re.match(r"^第[一二三四五六七八九十百]+条", l.strip()))
other = sum(1 for l in lines if l.strip() and
            not re.match(r"^第[一二三四五六七八九十百]+[章节条]", l.strip()) and
            not re.match(r"^（[一二三四五六七八九十百]+）", l.strip()) and
            l.strip() not in ["目　　录", "中华人民共和国个人信息保护法"] and
            not re.match(r"^（\d{4}年", l.strip()))

print(f"总行数：{len(lines)}")
print(f"空行：{empty}")
print(f"章标题：{chapter}")
print(f"章标题：{chapter}")
print(f"节标题：{section}")
print(f"文件标题/目录：{toc}")
print(f"通过日期行：{date}")
print(f"列表项（一）（二）：{list_item}")
print(f"条款行（第X条）：{article}")
print(f"其他正文行：{other}")
print(f"\n合计非空行：{len(lines)-empty}")
print(f"删除垃圾后剩余：{chapter+section+toc+date} 行将被删")
print(f"预期句数范围：{article} ~ {article+other} 句")