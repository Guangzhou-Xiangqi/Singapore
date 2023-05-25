import re

a_structure = """
[DhtmlXQ]
[DhtmlXQ_title]RADTAI LOKUTARAPOL先胜安吉洛.杨[/DhtmlXQ_title]
[DhtmlXQ_event]第32届东南亚运动会象棋比赛男子个人赛[/DhtmlXQ_event]
[DhtmlXQ_redteam]泰国THA[/DhtmlXQ_redteam]
[DhtmlXQ_redname]RADTAI LOKUTARAPOL[/DhtmlXQ_redname]
[DhtmlXQ_blackteam]菲律宾PHI[/DhtmlXQ_blackteam]
[DhtmlXQ_blackname]安吉洛.杨[/DhtmlXQ_blackname]
[DhtmlXQ_ecco]E03[/DhtmlXQ_ecco]
[DhtmlXQ_open]仙人指路对中炮[/DhtmlXQ_open]
[DhtmlXQ_result]红胜[/DhtmlXQ_result]
[DhtmlXQ_author]刘亿豪[/DhtmlXQ_author]
[DhtmlXQ_group]Men Single Standard [/DhtmlXQ_group]
[DhtmlXQ_date]2023-05-12[/DhtmlXQ_date]
[DhtmlXQ_place]Royal University of Phnom Penh[/DhtmlXQ_place]
[DhtmlXQ_round]3[/DhtmlXQ_round]
[DhtmlXQ_table]6[/DhtmlXQ_table]
[DhtmlXQ_binit]0919293949596979891777062646668600102030405060708012720323436383[/DhtmlXQ_binit]
[DhtmlXQ_movelist]2625124219271022091900101713706279676364777362541914434473745466744450418979726279736082736380602735625263536062[/DhtmlXQ_movelist]
[/DhtmlXQ]
"""


a_structure = a_structure.strip()

a_structure = re.sub(r'\[\s*\/\s*DhtmlXQ_(\w+)\s*\]',
                     r'[/DhtmlXQ_\1]', a_structure)  # fix closing tags

# move DhtmlXQ_binit after DhtmlXQ_init
a_structure = re.sub(r'\[DhtmlXQ_init\].+?\[\/DhtmlXQ_init\]',
                     r'[DhtmlXQ_init]500,350[/DhtmlXQ_init][DhtmlXQ_binit]0919293949596979891777062646668600102030405060708012720323436383[/DhtmlXQ_binit]', a_structure)

iframe_name_value = f'NoFile_[DhtmlXQiFrame][DhtmlXQ_ver]www_dpxq_com[/DhtmlXQ_ver]{a_structure}[/DhtmlXQ_binit]'

b_structure = f'''<iframe
    src="https://www.wxf-xiangqi.org/DhtmlXQ/DhtmlXQ_www_dpxq_com_Eng.htm"
    frameborder="0"
    scrolling="no"
    width="500"
    height="350"
    style="width: 500px; height: 350px"
    name="{iframe_name_value}"
></iframe>'''

print(b_structure)
