import re
import string
import json
import requests
import discord
from discord.ext import commands

txt_link_RU = 'Создаём будущее здесь и сейчас! \n \n' + \
              '<:imperial:660243430177243136> [Официальный сайт компании](https://imperialvtc.com/) \n \n' + \
              '<:vccom:660243428734664706> [Группа компании в vk.com](https://vk.com/imperialvtc) \n \n' + \
              '<:Steam:660244494112784405> [Группа компании в сообществе Steam](https://steamcommunity.com/groups/imperialvtc) \n \n' + \
              '<:truckersmp:658823474025857034> [Страница ВТК на сайте проекта TruckersMP](https://truckersmp.com/vtc/1221) \n \n' + '[]() \n'

txt_info_RU = 'Виртуальная транспортная компания «IMPERIAL TRUCKING COMPANY» специализируется на грузоперевозках различной сложности по территориям Европы, Польши, Франции, Англии и Скандинавии, Италии и Америки! \n \n' + \
              'В нашей команде исключительно профессиональные водители мира ETS2/ATS, способные выполнить доставку любой сложности в любую точку игрового мира. Мы на постоянной основе проводим внутренние конвои, мы всегда в пути! ' \
              'Высокая квалификация наших водителей подтверждена временем и сотнями тысяч пройденных километров! \n \n' + \
              'В нашей компании вас ждут большие конвои, различные мероприятия! Наша Компания отличается высокой дисциплиной, качеством выполнения грузоперевозок и взаимопониманием между водителями компании и администрацией. \n \n' + \
              'Если ты ответственный, компанейский и считаешь себя профессиональным водителем, либо хочешь им стать, то добро пожаловать в ряды сотрудников компании «IMPERIAL TRUCKING COMPANY»! \n \n' + \
              'Для вступления в нашу компанию заполните заявку на нашем официальном сайте в разделе "присоединиться" https://imperialvtc.com/ \n \n'

txt_link_EN = 'Creating the future here and now! \n \n' + \
              '<:imperial:660243430177243136> [Official website of the company](https://imperialvtc.com/) \n \n' + \
              '<:vccom:660243428734664706> [Company group in vk.com](https://vk.com/imperialvtc) \n \n' + \
              '<:Steam:660244494112784405> [Company group in Steam](https://steamcommunity.com/groups/imperialvtc) \n \n' + \
              '<:truckersmp:658823474025857034> [VTC page on the TruckersMP project website](https://truckersmp.com/vtc/1221) \n \n' + \
              '<:ts3:660243429875384366> [Company TeamSpeak 3 server](http://imperialvtc.ts3v.top/) \n \n' + '[]() \n'

txt_info_EN = 'The virtual trucking company "IMPERIAL" specializes in cargo transportation of various complexity across the territories of Europe, Poland, France, England and Scandinavia, Italy and America! \n \n' + \
              'Our team consists of exclusively professional drivers from the ETS2/ATS world who can deliver any complexity to any point in the game world. We constantly conduct internal convoys, we are always on the way! ' \
              'The high qualification of our drivers is confirmed by time and a large count of kilometers traveled! \n \n' + \
              'In our company, you will find large convoys, various events! Our Company is distinguished by high discipline, quality of cargo transportation and mutual understanding between the companys drivers and the administration. \n \n' + \
              'If you are responsible, sociable and consider yourself a professional driver, or want to become one, then welcome to "IMPERIAL TRUCKING COMPANY"! \n \n' + \
              'To join our company, fill the application form on our official website in the section " join" https://imperialvtc.com/application-for-joining/ \n \n'

txt_help = "Доступные комманды: \n1. /clear {количество сообщений} - удаление n-количества сообщений в чате. \n\n2. /echo_() , где () можно использовать:" + \
           "\n2.1 kr - сообщение от имени состава координаторов \n2.2 km - сообщение от имении состава Конвой Менеджмент \n 2.3 mm - сообщение от имени Медиа Менеджмента" + \
           "\n\n3. /print_list_admins - команда для печати состава администрации \n\n4. /print_welcome_1 и /print_welcome_2  - печать приветсвенного сообщения"

txt_info_1 = 'Данный Discord сервер - это место для внутренней коммуникации между всем персоналом компании. То, что происходит здесь, всегда должно оставаться здесь и не коим образом не выходить за пределы компании и данного Discord сервера. \n \n'

txt_info_2 = 'На этом сервере много каналов, но не все из них имеют первостепенное значение. Ниже будет список важных каналов с кратким описанием, чтобы прояснить их назначение. \n \n' + \
              '<#602844193286782979>; <#756999901933600809> - в данных каналах будут публиковаться все важные новости, обновления и изменения связанные с компанией \n \n' + \
              '<#684699605027389451> - в данном канале отображен список всех наших сотрудников разделенный по должностям и водительским категориям \n \n' + \
              '<#658796638285987841>; <#710271101284122626> - данные каналы отвечают за управление дополнительными ролями с использованием emoji сервера \n \n' + \
              '<#603214268308914187> - в данном канале вы можете использовать различные доступные вам команды для управлением discord ботами данного сервера \n \n' + \
              '<#602626957544259584> - приватный чат для всех действующих сотрудников компании \n \n' + \
              '<#734526327620763749> - канал для сообщений о различных технических проблемах на стороне компании для штата разработчиков и сотрудников старшего звена \n \n' + \
              'В дополнение к этому, вы иногда будете видеть каналы собраний персонала. Это те каналы, в которых у нас будут проводиться различные беседы связанные с компанией, доступные для всего действующего персонала, несколько раз в год. \n \n'

txt_info_3 =  '<@&668240472090738709> - глобальное управление компанией, всеми направлениями и всеми ее ресурсами \n \n' + \
              '<@&697181704753905665> - глобальное управление компанией, управление внутренними ресурсами и всем штатным персоналом \n \n' + \
              '<@&711339597086326834> - сотрудник руководящего состава, отвечающий за все проводимые мероприятия внутри компании и со стороны TruckersMP, руководит составом операторов транспортной логистики \n \n' + \
              '<@&669801637702795264> - сотрудник руководящего состава, отвечающий за все медиа-платформы относящиеся к компании, руководит составом медиа специалистов \n \n' + \
              '<@&602631192180817929> - сотрудник старшего состава администрации, отвечающий за кадровые операции и кураторскую деятельность связанную с водителями компании, руководит кадровым отделом \n \n' + \
              '<@&602805893020647434> - сотрудник старшего состава администрации, отвечающий за техническую разработку и поддержку всех ресурсов компании \n \n' + \
              '<@&739118581614247966> - сотрудник состава администрации, отвечающий за прием водителей в штат компании и вербовочную деятельность \n \n' + \
              '<@&675797820388933663> - сотрудник состава администрации, отвечающий за создание, проведение и управление внутренними мероприятиями и ивентами со стороны TruckersMP \n \n' + \
              '<@&675798265509183508> - сотрудник состава администрации, отвечающий за предоставление и управление медиа контентом используемом в публичных ресурсах компании \n \n'

txt_info_4 =  'Водительские категории разделены на несколько классов, каждый из которых соответствует определенным навыкам, которыми должен обладать участник претендующий на определенную категорию. \n \n' + \
              '<@&675799409728159792>; <@&676752983446388736>; <@&676752984201232384> - категории, относящиеся к высшему водительскому классу \n \n' + \
              '<@&676751936577339423>; <@&675799439155396620>; <@&676751940163600403> - категории, относящиеся к старшему водительскому классу \n \n' + \
              '<@&675799437104250900>; <@&675799435573461072>; <@&675799441005084682> - категории, относящиеся к младшему водительскому классу \n \n'

txt_links =   '<:imperial:660243430177243136> [Официальный сайт компании](https://imperialvtc.com/) \n \n' + \
              '<:imperial:660243430177243136> [Страница компании на TruckersMP](https://truckersmp.com/vtc/1221) \n \n' + \
              '<:imperial:660243430177243136> [Официальный instagram компании](https://www.instagram.com/imperial.trucking.company/) \n \n' + \
              '<:imperial:660243430177243136> [Discord сервер компании](https://discord.com/invite/geQG8KH) \n \n' + \
              '<:vccom:660243428734664706> [Официальная публичная группа vk.com](https://vk.com/imperialvtc) \n \n' + \
              '<:Steam:660244494112784405> [Группа компании в сообществе Steam](https://steamcommunity.com/groups/imperialvtc) \n \n' + \
              '<:truckersmp:658823474025857034> [Cайт проекта TruckersMP](https://truckersmp.com/) \n \n' + \
              '<:truckersmp:658823474025857034> [Форум проетка TruckersMP](https://forum.truckersmp.com/) \n \n' + \
              '<:truckersmp:658823474025857034> [Раздел техподдержки TruckersMP](https://truckersmp.com/support) \n \n' + \
              '---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- \n \n' + \
              '**© 2020 IMPERIAL TRUCKING COMPANY** \n \n'

emj_Russia = "\N{REGIONAL INDICATOR SYMBOL LETTER R}\N{REGIONAL INDICATOR SYMBOL LETTER U}"
emj_Kazakhstan = "\N{REGIONAL INDICATOR SYMBOL LETTER K}\N{REGIONAL INDICATOR SYMBOL LETTER Z}"
emj_Ukraine = "\N{REGIONAL INDICATOR SYMBOL LETTER U}\N{REGIONAL INDICATOR SYMBOL LETTER A}"
emj_Belarus = "\N{REGIONAL INDICATOR SYMBOL LETTER B}\N{REGIONAL INDICATOR SYMBOL LETTER Y}"
emj_Uzbekistan = "\N{REGIONAL INDICATOR SYMBOL LETTER U}\N{REGIONAL INDICATOR SYMBOL LETTER Z}"

emj_Portugal = "\N{REGIONAL INDICATOR SYMBOL LETTER P}\N{REGIONAL INDICATOR SYMBOL LETTER T}"
emj_Canada = "\N{REGIONAL INDICATOR SYMBOL LETTER C}\N{REGIONAL INDICATOR SYMBOL LETTER A}"
emj_Bulgaria = "\N{REGIONAL INDICATOR SYMBOL LETTER B}\N{REGIONAL INDICATOR SYMBOL LETTER G}"
emj_Italy = "\N{REGIONAL INDICATOR SYMBOL LETTER I}\N{REGIONAL INDICATOR SYMBOL LETTER T}"
emj_Spain = "\N{REGIONAL INDICATOR SYMBOL LETTER E}\N{REGIONAL INDICATOR SYMBOL LETTER S}"
emj_France = "\N{REGIONAL INDICATOR SYMBOL LETTER F}\N{REGIONAL INDICATOR SYMBOL LETTER R}"
emj_Norway = "\N{REGIONAL INDICATOR SYMBOL LETTER N}\N{REGIONAL INDICATOR SYMBOL LETTER O}"
emj_Sweden = "\N{REGIONAL INDICATOR SYMBOL LETTER S}\N{REGIONAL INDICATOR SYMBOL LETTER E}"
emj_Belgium = "\N{REGIONAL INDICATOR SYMBOL LETTER B}\N{REGIONAL INDICATOR SYMBOL LETTER E}"
emj_Germany = "\N{REGIONAL INDICATOR SYMBOL LETTER D}\N{REGIONAL INDICATOR SYMBOL LETTER E}"
emj_United_Kingdom = "\N{REGIONAL INDICATOR SYMBOL LETTER G}\N{REGIONAL INDICATOR SYMBOL LETTER B}"
emj_Usa = "\N{REGIONAL INDICATOR SYMBOL LETTER U}\N{REGIONAL INDICATOR SYMBOL LETTER S}"
emj_Israel = "\N{REGIONAL INDICATOR SYMBOL LETTER I}\N{REGIONAL INDICATOR SYMBOL LETTER L}"
emj_Estonia = "\N{REGIONAL INDICATOR SYMBOL LETTER E}\N{REGIONAL INDICATOR SYMBOL LETTER E}"
emj_Latvia = "\N{REGIONAL INDICATOR SYMBOL LETTER L}\N{REGIONAL INDICATOR SYMBOL LETTER V}"

emj_game_ets2 = "<:ets2:660268280149311493>"
emj_game_ats = "<:ats:660270150930399236>"
emj_dlc_road_to_the_black_sea = "\N{REGIONAL INDICATOR SYMBOL LETTER R}\N{REGIONAL INDICATOR SYMBOL LETTER O}"
emj_dlc_beyond_the_baltic_sea = "\N{REGIONAL INDICATOR SYMBOL LETTER R}\N{REGIONAL INDICATOR SYMBOL LETTER U}"
emj_dlc_vive_la_france = "\N{REGIONAL INDICATOR SYMBOL LETTER F}\N{REGIONAL INDICATOR SYMBOL LETTER R}"
emj_dlc_italia = "\N{REGIONAL INDICATOR SYMBOL LETTER I}\N{REGIONAL INDICATOR SYMBOL LETTER T}"
emj_dlc_scandinavia = "\N{REGIONAL INDICATOR SYMBOL LETTER N}\N{REGIONAL INDICATOR SYMBOL LETTER O}"
emj_dlc_going_east = "\N{REGIONAL INDICATOR SYMBOL LETTER H}\N{REGIONAL INDICATOR SYMBOL LETTER U}"

emj_truckersmp_blog = "<:truckersmp:658823474025857034>"
emj_scs_blog = "<:scs_software:658816969826500628>"
emj_game_spintires = "🚚"
emj_game_csgo = "<:7575_csgo:658901607454343168>"
emj_game_pubg = "<:pubg:658901611732795421>"
emj_music_blog = "🎵"
