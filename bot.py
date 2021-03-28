import datetime
import os
import random
import re
from itertools import cycle
import discord
import sqlite3
import requests
from discord.ext import tasks, commands

import cfg

# Starting bot
token = "NjU5Mzg5ODg1OTcwMzgyODU4.XkzqXw._EvIK4o8jjRRtlTZFaUhw9lLaWk"
print("Bot starting")

path_to_script = os.path.dirname(os.path.abspath(__file__))
path_to_image_123 = r"{}/123.png".format(path_to_script)
path_to_image_222 = r"{}/222.png".format(path_to_script)

bot = commands.Bot(command_prefix="/")
# players = {}
# emoji


int_id_message_for_give_and_remove_auto_role_rus = 738323287687561236
int_id_message_for_give_and_remove_auto_role_eng = 738323288446730284

int_id_message_for_give_and_remove_auto_role_game_and_dlc = 738323368494891076
int_id_message_for_give_and_remove_auto_role_blog_and_acc_music = 738323384449892432

status = cycle(['www.imperialvtc.com', 'www.truckersmp.com', 'www.worldoftrucks.com'])


@bot.event
async def on_message(message):
    await bot.process_commands(message)


@bot.event
async def on_ready():
    bot.remove_command('help')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="www.imperialvtc.com"))
    if path_to_script == r"с:\Users\anban\Documents\GitHub\bot-imperial":
        print("m")
        await bot.change_presence(status=discord.Status.idle, activity=discord.Game("Testing new function"))
    # bot.loop.create_task(testings())
    print("Bot started working")
    print(path_to_script)


@bot.event
async def on_raw_reaction_add(payload):
    guild = bot.get_guild(567041857385660416)
    channel_create_new_event = "761704568203116615"
    print("New action! Add reaction on message")
    print(type(payload))
    print(payload)
    print("              ")
    chat_id_send_from = str(payload.channel_id)
    # ru roles
    if chat_id_send_from == "658796638285987841" or chat_id_send_from == "710271101284122626":
        role_ru_flag = discord.utils.get(guild.roles, id=603209579614044161)
        role_kz_flag = discord.utils.get(guild.roles, id=658801692145614869)
        role_ukr_flag = discord.utils.get(guild.roles, id=603209690007994388)
        role_by_flag = discord.utils.get(guild.roles, id=603209620562903040)
        role_uz_flag = discord.utils.get(guild.roles, id=675805237126103082)

        # eng roles
        role_pt_flag = discord.utils.get(guild.roles, id=675804843440603166)
        role_ca_flag = discord.utils.get(guild.roles, id=675804841582264344)
        role_bg_flag = discord.utils.get(guild.roles, id=675804840068382722)
        role_it_flag = discord.utils.get(guild.roles, id=675803362872262666)
        role_es_flag = discord.utils.get(guild.roles, id=675803362280603658)
        role_fr_flag = discord.utils.get(guild.roles, id=675803362259632132)
        role_no_flag = discord.utils.get(guild.roles, id=675804842450747403)
        role_se_flag = discord.utils.get(guild.roles, id=675805600646692907)
        role_be_flag = discord.utils.get(guild.roles, id=675804731385446410)
        role_de_flag = discord.utils.get(guild.roles, id=675803360183582783)
        role_gb_flag = discord.utils.get(guild.roles, id=675803359516557315)
        role_us_flag = discord.utils.get(guild.roles, id=675805234546868235)
        role_il_flag = discord.utils.get(guild.roles, id=675804840848392192)
        role_ee_flag = discord.utils.get(guild.roles, id=658799876062052407)
        role_lv_flag = discord.utils.get(guild.roles, id=603209657653395457)

        # adding roles
        role_game_ets2 = discord.utils.get(guild.roles, id=659886174097113101)
        role_game_ats = discord.utils.get(guild.roles, id=659886207312068629)
        role_dlc_road_to_the_black_sea = discord.utils.get(guild.roles, id=659932340713422850)
        role_dlc_beyond_baltic_sea = discord.utils.get(guild.roles, id=659932093408870414)
        role_dlc_france = discord.utils.get(guild.roles, id=659932091768897559)
        role_dlc_italia = discord.utils.get(guild.roles, id=659932089642385418)
        role_dlc_scandinavia = discord.utils.get(guild.roles, id=659932087083597834)
        role_dlc_going_east = discord.utils.get(guild.roles, id=659931317244526599)

        role_blog_tmp_news = discord.utils.get(guild.roles, id=603206651155185664)
        role_blog_scs_news = discord.utils.get(guild.roles, id=658804470943055881)
        role_game_spintires = discord.utils.get(guild.roles, id=604734134081814572)
        role_game_csgo = discord.utils.get(guild.roles, id=658897902051131414)
        role_game_pubg = discord.utils.get(guild.roles, id=609489283371237376)
        role_get_acc_music = discord.utils.get(guild.roles, id=658895517602021388)

        # print(str(payload))
        # Выдача ролей на сообщение русскоязычных стран
        if payload.message_id == int_id_message_for_give_and_remove_auto_role_rus:
            if payload.event_type == "REACTION_ADD":
                if str(payload.emoji) == cfg.emj_Russia:  # RU
                    await payload.member.add_roles(role_ru_flag)
                if str(payload.emoji) == cfg.emj_Kazakhstan:  # KZ
                    await payload.member.add_roles(role_kz_flag)
                if str(payload.emoji) == cfg.emj_Ukraine:  # UA
                    await payload.member.add_roles(role_ukr_flag)
                if str(payload.emoji) == cfg.emj_Belarus:  # BY
                    await payload.member.add_roles(role_by_flag)
                if str(payload.emoji) == cfg.emj_Uzbekistan:  # UZ
                    await payload.member.add_roles(role_uz_flag)
        # Выдача ролей на сообщение англоязычных стран.
        if payload.message_id == int_id_message_for_give_and_remove_auto_role_eng:
            if payload.event_type == "REACTION_ADD":
                if str(payload.emoji) == cfg.emj_Portugal:
                    await payload.member.add_roles(role_pt_flag)
                if str(payload.emoji) == cfg.emj_Canada:
                    await payload.member.add_roles(role_ca_flag)
                if str(payload.emoji) == cfg.emj_Bulgaria:
                    await payload.member.add_roles(role_bg_flag)
                if str(payload.emoji) == cfg.emj_Italy:
                    await payload.member.add_roles(role_it_flag)
                if str(payload.emoji) == cfg.emj_Spain:
                    await payload.member.add_roles(role_es_flag)
                if str(payload.emoji) == cfg.emj_France:
                    await payload.member.add_roles(role_fr_flag)
                if str(payload.emoji) == cfg.emj_Norway:
                    await payload.member.add_roles(role_no_flag)
                if str(payload.emoji) == cfg.emj_Sweden:
                    await payload.member.add_roles(role_se_flag)
                if str(payload.emoji) == cfg.emj_Belgium:
                    await payload.member.add_roles(role_be_flag)
                if str(payload.emoji) == cfg.emj_Germany:
                    await payload.member.add_roles(role_de_flag)
                if str(payload.emoji) == cfg.emj_United_Kingdom:
                    await payload.member.add_roles(role_gb_flag)
                if str(payload.emoji) == cfg.emj_Usa:
                    await payload.member.add_roles(role_us_flag)
                if str(payload.emoji) == cfg.emj_Israel:
                    await payload.member.add_roles(role_il_flag)
                if str(payload.emoji) == cfg.emj_Estonia:
                    await payload.member.add_roles(role_ee_flag)
                if str(payload.emoji) == cfg.emj_Latvia:
                    await payload.member.add_roles(role_lv_flag)
        if payload.message_id == int_id_message_for_give_and_remove_auto_role_game_and_dlc:
            if payload.event_type == "REACTION_ADD":
                if str(payload.emoji) == cfg.emj_game_ets2:
                    await payload.member.add_roles(role_game_ets2)
                if str(payload.emoji) == cfg.emj_game_ats:
                    await payload.member.add_roles(role_game_ats)
                if str(payload.emoji) == cfg.emj_dlc_road_to_the_black_sea:
                    await payload.member.add_roles(role_dlc_road_to_the_black_sea)
                if str(payload.emoji) == cfg.emj_dlc_beyond_the_baltic_sea:
                    await payload.member.add_roles(role_dlc_beyond_baltic_sea)
                if str(payload.emoji) == cfg.emj_dlc_vive_la_france:
                    await payload.member.add_roles(role_dlc_france)
                if str(payload.emoji) == cfg.emj_dlc_italia:
                    await payload.member.add_roles(role_dlc_italia)
                if str(payload.emoji) == cfg.emj_dlc_scandinavia:
                    await payload.member.add_roles(role_dlc_scandinavia)
                if str(payload.emoji) == cfg.emj_dlc_going_east:
                    await payload.member.add_roles(role_dlc_going_east)
        if payload.message_id == int_id_message_for_give_and_remove_auto_role_blog_and_acc_music:
            if payload.event_type == "REACTION_ADD":
                if str(payload.emoji) == cfg.emj_truckersmp_blog:
                    await payload.member.add_roles(role_blog_tmp_news)
                if str(payload.emoji) == cfg.emj_scs_blog:
                    await payload.member.add_roles(role_blog_scs_news)
                if str(payload.emoji) == cfg.emj_game_spintires:
                    await payload.member.add_roles(role_game_spintires)
                if str(payload.emoji) == cfg.emj_game_csgo:
                    await payload.member.add_roles(role_game_csgo)
                if str(payload.emoji) == cfg.emj_game_pubg:
                    await payload.member.add_roles(role_game_pubg)
                if str(payload.emoji) == cfg.emj_music_blog:
                    await payload.member.add_roles(role_get_acc_music)
    if chat_id_send_from == channel_create_new_event:
        if str(payload.emoji) == "👟":
            await create_new_channel_with_number_convoy_list(guild)


@bot.event
async def on_raw_reaction_remove(payload):
    print("New action! Remove reaction on message")
    print(payload)
    print("              ")
    guild = bot.get_guild(567041857385660416)
    testofw = str(payload.channel_id)
    # ru roles
    if testofw == "658796638285987841" or testofw == "710271101284122626":
        role_ru_flag = discord.utils.get(guild.roles, id=603209579614044161)
        role_kz_flag = discord.utils.get(guild.roles, id=658801692145614869)
        role_ukr_flag = discord.utils.get(guild.roles, id=603209690007994388)
        role_by_flag = discord.utils.get(guild.roles, id=603209620562903040)
        role_uz_flag = discord.utils.get(guild.roles, id=675805237126103082)

        # eng roles
        role_pt_flag = discord.utils.get(guild.roles, id=675804843440603166)
        role_ca_flag = discord.utils.get(guild.roles, id=675804841582264344)
        role_bg_flag = discord.utils.get(guild.roles, id=675804840068382722)
        role_it_flag = discord.utils.get(guild.roles, id=675803362872262666)
        role_es_flag = discord.utils.get(guild.roles, id=675803362280603658)
        role_fr_flag = discord.utils.get(guild.roles, id=675803362259632132)
        role_no_flag = discord.utils.get(guild.roles, id=675804842450747403)
        role_se_flag = discord.utils.get(guild.roles, id=675805600646692907)
        role_be_flag = discord.utils.get(guild.roles, id=675804731385446410)
        role_de_flag = discord.utils.get(guild.roles, id=675803360183582783)
        role_gb_flag = discord.utils.get(guild.roles, id=675803359516557315)
        role_us_flag = discord.utils.get(guild.roles, id=675805234546868235)
        role_il_flag = discord.utils.get(guild.roles, id=675804840848392192)
        role_ee_flag = discord.utils.get(guild.roles, id=658799876062052407)
        role_lv_flag = discord.utils.get(guild.roles, id=603209657653395457)

        # adding roles
        role_game_ets2 = discord.utils.get(guild.roles, id=659886174097113101)
        role_game_ats = discord.utils.get(guild.roles, id=659886207312068629)
        role_dlc_road_to_the_black_sea = discord.utils.get(guild.roles, id=659932340713422850)
        role_dlc_beyond_baltic_sea = discord.utils.get(guild.roles, id=659932093408870414)
        role_dlc_france = discord.utils.get(guild.roles, id=659932091768897559)
        role_dlc_italia = discord.utils.get(guild.roles, id=659932089642385418)
        role_dlc_scandinavia = discord.utils.get(guild.roles, id=659932087083597834)
        role_dlc_going_east = discord.utils.get(guild.roles, id=659931317244526599)

        role_blog_tmp_news = discord.utils.get(guild.roles, id=603206651155185664)
        role_blog_scs_news = discord.utils.get(guild.roles, id=658804470943055881)
        role_game_spintires = discord.utils.get(guild.roles, id=604734134081814572)
        role_game_csgo = discord.utils.get(guild.roles, id=658897902051131414)
        role_game_pubg = discord.utils.get(guild.roles, id=609489283371237376)
        role_get_acc_music = discord.utils.get(guild.roles, id=658895517602021388)

        user = bot.get_user(payload.user_id)
        user = guild.get_member(user_id=int(payload.user_id))
        # print(user)
        # снятие ролей на сообщение русскоязычных стран
        if payload.message_id == int_id_message_for_give_and_remove_auto_role_rus:
            if payload.event_type == "REACTION_REMOVE":
                if str(payload.emoji) == cfg.emj_Russia:  # RU
                    await user.remove_roles(role_ru_flag)
                if str(payload.emoji) == cfg.emj_Kazakhstan:  # KZ
                    await user.remove_roles(role_kz_flag)
                if str(payload.emoji) == cfg.emj_Ukraine:  # UA
                    await user.remove_roles(role_ukr_flag)
                if str(payload.emoji) == cfg.emj_Belarus:  # BY
                    await user.remove_roles(role_by_flag)
                if str(payload.emoji) == cfg.emj_Uzbekistan:  # UZ
                    await user.remove_roles(role_uz_flag)
        # снятие ролей на сообщение англоязычных стран
        if payload.message_id == int_id_message_for_give_and_remove_auto_role_eng:
            if payload.event_type == "REACTION_REMOVE":
                if str(payload.emoji) == cfg.emj_Portugal:
                    await user.remove_roles(role_pt_flag)
                if str(payload.emoji) == cfg.emj_Canada:
                    await user.remove_roles(role_ca_flag)
                if str(payload.emoji) == cfg.emj_Bulgaria:
                    await user.remove_roles(role_bg_flag)
                if str(payload.emoji) == cfg.emj_Italy:
                    await user.remove_roles(role_it_flag)
                if str(payload.emoji) == cfg.emj_Spain:
                    await user.remove_roles(role_es_flag)
                if str(payload.emoji) == cfg.emj_France:
                    await user.remove_roles(role_fr_flag)
                if str(payload.emoji) == cfg.emj_Norway:
                    await user.remove_roles(role_no_flag)
                if str(payload.emoji) == cfg.emj_Sweden:
                    await user.remove_roles(role_se_flag)
                if str(payload.emoji) == cfg.emj_Belgium:
                    await user.remove_roles(role_be_flag)
                if str(payload.emoji) == cfg.emj_Germany:
                    await user.remove_roles(role_de_flag)
                if str(payload.emoji) == cfg.emj_United_Kingdom:
                    await user.remove_roles(role_gb_flag)
                if str(payload.emoji) == cfg.emj_Usa:
                    await user.remove_roles(role_us_flag)
                if str(payload.emoji) == cfg.emj_Israel:
                    await user.remove_roles(role_il_flag)
                if str(payload.emoji) == cfg.emj_Estonia:
                    await user.remove_roles(role_ee_flag)
                if str(payload.emoji) == cfg.emj_Latvia:
                    await user.remove_roles(role_lv_flag)
        if payload.message_id == int_id_message_for_give_and_remove_auto_role_game_and_dlc:
            if payload.event_type == "REACTION_REMOVE":
                if str(payload.emoji) == cfg.emj_game_ets2:
                    await user.remove_roles(role_game_ets2)
                if str(payload.emoji) == cfg.emj_game_ats:
                    await user.remove_roles(role_game_ats)
                if str(payload.emoji) == cfg.emj_dlc_road_to_the_black_sea:
                    await user.remove_roles(role_dlc_road_to_the_black_sea)
                if str(payload.emoji) == cfg.emj_dlc_beyond_the_baltic_sea:
                    await user.remove_roles(role_dlc_beyond_baltic_sea)
                if str(payload.emoji) == cfg.emj_dlc_vive_la_france:
                    await user.remove_roles(role_dlc_france)
                if str(payload.emoji) == cfg.emj_dlc_italia:
                    await user.remove_roles(role_dlc_italia)
                if str(payload.emoji) == cfg.emj_dlc_scandinavia:
                    await user.remove_roles(role_dlc_scandinavia)
                if str(payload.emoji) == cfg.emj_dlc_going_east:
                    await user.remove_roles(role_dlc_going_east)
        if payload.message_id == int_id_message_for_give_and_remove_auto_role_blog_and_acc_music:
            if payload.event_type == "REACTION_REMOVE":
                if str(payload.emoji) == cfg.emj_truckersmp_blog:
                    await user.remove_roles(role_blog_tmp_news)
                if str(payload.emoji) == cfg.emj_scs_blog:
                    await user.remove_roles(role_blog_scs_news)
                if str(payload.emoji) == cfg.emj_game_spintires:
                    await user.remove_roles(role_game_spintires)
                if str(payload.emoji) == cfg.emj_game_csgo:
                    await user.remove_roles(role_game_csgo)
                if str(payload.emoji) == cfg.emj_game_pubg:
                    await user.remove_roles(role_game_pubg)
                if str(payload.emoji) == cfg.emj_music_blog:
                    await user.remove_roles(role_get_acc_music)
    else:
        print("Все заебись, все работает")


@bot.command()
async def print_arole_lang(ctx):
    # Большая функция по выдаче ролей (страны). Реакция на определенные emoji.
    guild = bot.get_guild(567041857385660416)
    # start
    embed_start = discord.Embed(title="Автоматическая выдача ролей | Automatic assignment of roles",
                                description="Нажмите на эмоджик вашей желаемой роли под этим сообщением, чтобы назначить эту роль себе. Удаление реакции приводит к потере роли. \n\n Click on the emoticon of your desired role below this message in order to assign the role to yourself. Removing the reaction results into losing the role.",
                                color=0x4000f0)
    embed_start.set_footer(text="www.imperialvtc.com")
    # message = await ctx.send(embed=embed)
    # Choose a Russian-speaking country
    embed_ch_russian_country = discord.Embed(title="Автоматическая выдача ролей | Automatic assignment of roles",
                                             description="{ru_em} Russia\n{kz_em} Kazakhstan \n{Ua_emoji} Ukraine\n{By_emoji} Belarus\n{Uz_emoji} Uzbekistan"
                                             .format(ru_em=cfg.emj_Russia,
                                                     kz_em=cfg.emj_Kazakhstan,
                                                     Ua_emoji=cfg.emj_Ukraine,
                                                     By_emoji=cfg.emj_Belarus,
                                                     Uz_emoji=cfg.emj_Uzbekistan), color=0x4000f0)
    embed_ch_russian_country.set_footer(text="www.imperialvtc.com")
    # Choose a English-speaking country
    embed_ch_english_country = discord.Embed(title="Автоматическая выдача ролей | Automatic assignment of roles",
                                             description='{pt_em} Portugal\n{canada_em} Canada\n{bulgaria_em} Bulgaria\n{it_em} Italy\n{spain_em} Spain\n{fr_em} France\n{norway_em} Norway\n{sweden_em} Sweden\n{belg_em} Belgium\n{ger_em} Germany\n{un_kin_em} United Kingdom\n{usa_em} USA\n{isr_em} Israel\n{est_em} Estonia\n{lv_em} Latvia'
                                             .format(pt_em=cfg.emj_Portugal, canada_em=cfg.emj_Canada,
                                                     bulgaria_em=cfg.emj_Bulgaria, it_em=cfg.emj_Italy,
                                                     spain_em=cfg.emj_Spain, fr_em=cfg.emj_France,
                                                     norway_em=cfg.emj_Norway, sweden_em=cfg.emj_Sweden,
                                                     belg_em=cfg.emj_Belgium, ger_em=cfg.emj_Germany,
                                                     un_kin_em=cfg.emj_United_Kingdom,
                                                     usa_em=cfg.emj_Usa, isr_em=cfg.emj_Israel, est_em=cfg.emj_Estonia,
                                                     lv_em=cfg.emj_Latvia), color=0x4000f0)
    embed_ch_english_country.set_footer(text="www.imperialvtc.com")

    await ctx.send(embed=embed_start)
    message_ch_russian_country = await ctx.send(embed=embed_ch_russian_country)
    message_ch_eng_country = await ctx.send(embed=embed_ch_english_country)

    await message_ch_russian_country.add_reaction(cfg.emj_Russia)
    await message_ch_russian_country.add_reaction(cfg.emj_Kazakhstan)
    await message_ch_russian_country.add_reaction(cfg.emj_Ukraine)
    await message_ch_russian_country.add_reaction(cfg.emj_Belarus)
    await message_ch_russian_country.add_reaction(cfg.emj_Uzbekistan)

    await message_ch_eng_country.add_reaction(cfg.emj_Portugal)
    await message_ch_eng_country.add_reaction(cfg.emj_Canada)
    await message_ch_eng_country.add_reaction(cfg.emj_Bulgaria)
    await message_ch_eng_country.add_reaction(cfg.emj_Italy)
    await message_ch_eng_country.add_reaction(cfg.emj_Spain)
    await message_ch_eng_country.add_reaction(cfg.emj_France)
    await message_ch_eng_country.add_reaction(cfg.emj_Norway)
    await message_ch_eng_country.add_reaction(cfg.emj_Sweden)
    await message_ch_eng_country.add_reaction(cfg.emj_Belgium)
    await message_ch_eng_country.add_reaction(cfg.emj_Germany)
    await message_ch_eng_country.add_reaction(cfg.emj_United_Kingdom)
    await message_ch_eng_country.add_reaction(cfg.emj_Usa)
    await message_ch_eng_country.add_reaction(cfg.emj_Israel)
    await message_ch_eng_country.add_reaction(cfg.emj_Estonia)
    await message_ch_eng_country.add_reaction(cfg.emj_Latvia)


@bot.command()
async def print_arole_addionally(ctx):
    guild = bot.get_guild(567041857385660416)
    # start
    embed_start = discord.Embed(title="Автоматическая выдача ролей | Automatic assignment of roles",
                                description="Нажмите на эмоджик вашей желаемой роли под этим сообщением, чтобы назначить эту роль себе. Удаление реакции приводит к потере роли. \n\n Click on the emoticon of your desired role below this message in order to assign the role to yourself. Removing the reaction results into losing the role.",
                                color=0x4000f0)
    embed_start.set_footer(text="www.imperialvtc.com")
    # message = await ctx.send(embed=embed)
    # ch game and dlc
    embed_ch_dlc_and_game = discord.Embed(
        title="Автоматическая выдача ролей | Automatic assignment of roles\nВыбор дополнений\nSet DLCs",
        description="{emj_ets2} Euro Truck Simulator 2\n{emj_ats} American Truck Simulator\n{emj_road_blc_sea} Road to the Black Sea\n{emj_baltic_sea} Beyond the Baltic Sea\n{emj_vive_la_france} Vive la France\n{emj_italia} Italia\n{emj_scandinavia} Scandinavia\n{emj_going_east} Going East"
            .format(emj_ets2=cfg.emj_game_ets2, emj_ats=cfg.emj_game_ats,
                    emj_road_blc_sea=cfg.emj_dlc_road_to_the_black_sea,
                    emj_baltic_sea=cfg.emj_dlc_beyond_the_baltic_sea, emj_vive_la_france=cfg.emj_dlc_vive_la_france,
                    emj_italia=cfg.emj_dlc_italia,
                    emj_scandinavia=cfg.emj_dlc_scandinavia, emj_going_east=cfg.emj_dlc_going_east), color=0x4000f0)
    embed_ch_dlc_and_game.set_footer(text="www.imperialvtc.com")

    # ch blog and game and music
    embed_ch_gameblog_and_music = discord.Embed(
        title="Автоматическая выдача ролей | Automatic assignment of roles\nВыбор подписки\nSet a subscription",
        description="{emj_tmp_blog} TruckersMP news blog\n{emj_scs_blog} SCS software news blog\n{emj_spintires} Spintires/Mudrunner\n{emj_csgo} Counter Strike Global Offensive\n{emj_pubg} Playerunknown's battlegrounds\n{emj_music} Music"
            .format(emj_tmp_blog=cfg.emj_truckersmp_blog, emj_scs_blog=cfg.emj_scs_blog,
                    emj_spintires=cfg.emj_game_spintires, emj_csgo=cfg.emj_game_csgo, emj_pubg=cfg.emj_game_pubg,
                    emj_music=cfg.emj_music_blog), color=0x4000f0)
    embed_ch_gameblog_and_music.set_footer(text="www.imperialvtc.com")

    await ctx.send(embed=embed_start)
    message_ch_dlc_and_game = await ctx.send(embed=embed_ch_dlc_and_game)
    await message_ch_dlc_and_game.add_reaction(cfg.emj_game_ets2)
    await message_ch_dlc_and_game.add_reaction(cfg.emj_game_ats)
    await message_ch_dlc_and_game.add_reaction(cfg.emj_dlc_road_to_the_black_sea)
    await message_ch_dlc_and_game.add_reaction(cfg.emj_dlc_beyond_the_baltic_sea)
    await message_ch_dlc_and_game.add_reaction(cfg.emj_dlc_vive_la_france)
    await message_ch_dlc_and_game.add_reaction(cfg.emj_dlc_italia)
    await message_ch_dlc_and_game.add_reaction(cfg.emj_dlc_scandinavia)
    await message_ch_dlc_and_game.add_reaction(cfg.emj_dlc_going_east)

    message_ch_blog_music = await ctx.send(embed=embed_ch_gameblog_and_music)
    await message_ch_blog_music.add_reaction(cfg.emj_truckersmp_blog)
    await message_ch_blog_music.add_reaction(cfg.emj_scs_blog)
    await message_ch_blog_music.add_reaction(cfg.emj_game_spintires)
    await message_ch_blog_music.add_reaction(cfg.emj_game_csgo)
    await message_ch_blog_music.add_reaction(cfg.emj_game_pubg)
    await message_ch_blog_music.add_reaction(cfg.emj_music_blog)


@bot.event
async def on_message_delete(message):
    upper_moderation_logs_channel = bot.get_channel(735121066216914965)
    moderation_logs_channel = bot.get_channel(602938497107624025)
    channel_dev_staff = bot.get_channel(660204377969000459)
    channel_test_dev_staff = bot.get_channel(677134482477940746)
    embed = discord.Embed(title='Member deleted message', colour=discord.Colour(0x121892),
                          description='**Member {} deleted this message:**\n```\n{}\n```'.format(message.author,
                                                                                                 message.content))
    embed.set_author(name=message.author, url="https://imperialvtc.com/", icon_url=message.author.avatar_url)
    embed.set_footer(text="Server time: {}".format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M")))
    await upper_moderation_logs_channel.send(embed=embed)


@bot.event
async def on_member_update(before, after):
    moderation_logs_channel = bot.get_channel(602938497107624025)
    channel_dev_staff = bot.get_channel(660204377969000459)
    channel_test_dev_staff = bot.get_channel(677134482477940746)
    if before.nick == after.nick:
        pass
    if before.nick != after.nick:
        embed = discord.Embed(title='Member changed nickname', colour=discord.Colour(0x121892),
                              description='{}\n**До смены:**\n{}\n**После смены:\n**{}'.format(after.mention,
                                                                                               before.nick, after.nick))
        embed.set_author(name=after, url="https://imperialvtc.com/",
                         icon_url=after.avatar_url)
        embed.set_footer(text="Server time: {}".format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M")))
        await moderation_logs_channel.send(embed=embed)
    if not list(set(before.roles) - set(after.roles)):
        pass
    if not list(set(after.roles) - set(before.roles)):
        pass
    if list(set(before.roles) - set(after.roles)):
        embed = discord.Embed(title='Remove role', colour=discord.Colour(0x121892),
                              description='{}\n**Удалена роль:**\n{}'.format(after.mention, list(
                                  set(before.roles) - set(after.roles))))
        embed.set_author(name=after, url="https://imperialvtc.com/", icon_url=after.avatar_url)
        embed.set_footer(text="Server time: {}".format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M")))
        await moderation_logs_channel.send(embed=embed)
    if list(set(after.roles) - set(before.roles)) != []:
        embed = discord.Embed(title='Add role', colour=discord.Colour(0x121892),
                              description='{}\n**Добавлена роль:**\n{}'.format(after.mention, list(
                                  set(after.roles) - set(before.roles))))
        embed.set_author(name=after, url="https://imperialvtc.com/", icon_url=after.avatar_url)
        embed.set_footer(text="Server time: {}".format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M")))
        await moderation_logs_channel.send(embed=embed)


@bot.event
async def on_member_join(ctx):
    moderation_logs_channel = bot.get_channel(602938497107624025)
    channel_dev_staff = bot.get_channel(660204377969000459)

    embed = discord.Embed(title='New member', colour=discord.Colour(0x121892), description='New member on server - {}\n Accout created : {}'.format(ctx.mention, ctx.created_at.strftime("%d-%m-%Y %H:%M")))
    embed.set_author(name=ctx, url="https://imperialvtc.com/", icon_url=ctx.avatar_url)
    embed.set_footer(text="Server time: {}".format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M")))
    await moderation_logs_channel.send(embed=embed)

    """
    Для каждого нового участника сервера дискорд - выдаются эти роли
    """
    role_guest = ctx.guild.get_role(659889139767836692)
    role_razdelitel1 = ctx.guild.get_role(711201518065418330)
    role_owned_games = ctx.guild.get_role(677164724839907329)
    role_owned_dls = ctx.guild.get_role(677165035159683083)
    role_razdelitel2 = ctx.guild.get_role(711214507808129065)
    role_country = ctx.guild.get_role(677165417113976853)
    role_additionally = ctx.guild.get_role(677165885454024705)

    await ctx.add_roles(role_guest)
    await ctx.add_roles(role_razdelitel1)
    await ctx.add_roles(role_owned_games)
    await ctx.add_roles(role_owned_dls)
    await ctx.add_roles(role_razdelitel2)
    await ctx.add_roles(role_country)
    await ctx.add_roles(role_additionally)


@bot.event
async def on_member_remove(ctx):
    moderation_logs_channel = bot.get_channel(602938497107624025)
    channel_dev_staff = bot.get_channel(660204377969000459)

    embed = discord.Embed(title='Member left', colour=discord.Colour(0x121892),
                          description='Member left on server - {}\n Accout created : {}'.format(ctx.mention, ctx.created_at.strftime("%d-%m-%Y %H:%M")))
    embed.set_author(name=ctx, url="https://imperialvtc.com/", icon_url=ctx.avatar_url)
    embed.set_footer(text="Server time: {}".format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M")))
    await moderation_logs_channel.send(embed=embed)


@bot.event
async def on_voice_state_update(member, before, after):
    print(member)
    print(type(member))
    print(before)
    print(type(before))
    print(after)
    print(type(after))


@bot.command()
async def change_status(ctx, *, args: str):
    # async def echo_km(ctx, bool_everyone, *, args: str)
    emoji = '<:troll_face:671342798791770112>'
    status_int = str(args)
    if status_int == "1":
        await bot.change_presence(activity=discord.Game(name='IMPERIAL WORLD'))
    if status_int == "2":
        await bot.change_presence(activity=discord.Game(name='IMPERIAL VTC'))
    if status_int == "3":
        await bot.change_presence(activity=discord.Game(name='NEWESTAGE'))
    if status_int == "4":
        await bot.change_presence(activity=discord.Game(name='www.imperialvtc.com'))
    if status_int == "tm":
        await bot.change_presence(activity=discord.Game(name='technological mode'))
    message = await ctx.send("done")
    await message.add_reaction(emoji)
    print("Status changed - {}".format(ctx.message.author))


@bot.command()
async def cr_poll(ctx, bool_everyone, *, args: str):
    # create new poll, yes? no?
    if bool_everyone == "0":
        emoji_yes = '<:pixel_yes:671340113539891210>'
        emoji_no = '<:pixel_nop:671340112948494367>'
        embed = discord.Embed(title='', colour=discord.Colour(0x1e88e5), description="{}".format(args))
        embed.set_author(name="Состав администрации компании", url="https://imperialvtc.com", icon_url="https://cdn.discordapp.com/attachments/642462454512615489/664672245129674763/logo_novy_format3.png")
        await ctx.channel.purge(limit=1)
        message = await ctx.send(embed=embed)
        await message.add_reaction(emoji_yes)
        await message.add_reaction(emoji_no)
    if bool_everyone == "1":
        emoji_yes = '<:pixel_yes:671340113539891210>'
        emoji_no = '<:pixel_nop:671340112948494367>'
        embed = discord.Embed(title='', colour=discord.Colour(0x1e88e5), description="{}".format(args))
        embed.set_author(name="Состав администрации компании", url="https://imperialvtc.com", icon_url="https://cdn.discordapp.com/attachments/642462454512615489/664672245129674763/logo_novy_format3.png")
        await ctx.channel.purge(limit=1)
        await ctx.send("@everyone")
        message = await ctx.send(embed=embed)
        await message.add_reaction(emoji_yes)
        await message.add_reaction(emoji_no)
    print("create pool by {}".format(ctx.message.author))


@bot.command()
async def imperial_help_(ctx):
    # dont use
    """
    Метод для печати справки по компандам бота.
    """
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title='Справка команд для IMPERIAL BOT', colour=discord.Colour(0x121892), description=cfg.txt_help)

    embed.set_image(url="https://cdn.discordapp.com/attachments/660204377969000459/660220772773789706/52aa5420668fbffd.png")
    embed.set_author(name="IMPERIAL BOT", url="https://imperialvtc.ru/", icon_url="https://cdn.discordapp.com/attachments/642462454512615489/664672245129674763/logo_novy_format3.png")

    await ctx.send(embed=embed)


# _____________________________________________________________________________________________
# echo
@bot.command(pass_context=True)
async def echo_admin(ctx, bool_everyone, *, args: str):
    if bool_everyone == "0":
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(title='', colour=discord.Colour(0x1e88e5), description="{}".format(args))
        embed.set_author(name="Состав администрации компании", url="https://imperialvtc.com", icon_url="https://cdn.discordapp.com/attachments/642462454512615489/664672245129674763/logo_novy_format3.png")
        await ctx.send(embed=embed)
    if bool_everyone == "1":
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(title='', colour=discord.Colour(0x1e88e5), description="{}".format(args))
        embed.set_author(name="Состав администрации компании", url="https://imperialvtc.com", icon_url="https://cdn.discordapp.com/attachments/642462454512615489/664672245129674763/logo_novy_format3.png")
        await ctx.send("@everyone")
        await ctx.send(embed=embed)


@bot.command()
async def echo(ctx, *, content: str):
    embed = discord.Embed(title='', colour=discord.Colour(0x000000), description="{}".format(content))
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)


# ___________________________________________________________________________________________________
@bot.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()


@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


@bot.command()
async def mvc(ctx, count_user, *, members):
    # dont use
    """
    Метод для создания голосовых каналов с выдаче доступа определённым людям которые были отмечены через @
    mvc - make voice channel

    Только не надо пиздеть , я знаю что это просто пиздец какой хуевый коd, но он работает.
    Когда нибудь я его перепишу.
    """
    guild = ctx.guild
    ch = discord.utils.get(guild.categories, id=602625293328318474)
    random_int = random.randint(0, 10000)
    nutyx_id = guild.get_member(user_id=472517564690333697)
    alcry_id = guild.get_member(user_id=329214969897811969)
    test_id = 159985870458322944

    members_1 = guild.get_member(user_id=test_id)
    members_2 = guild.get_member(user_id=test_id)
    members_3 = guild.get_member(user_id=test_id)
    members_4 = guild.get_member(user_id=test_id)
    members_5 = guild.get_member(user_id=test_id)
    members_6 = guild.get_member(user_id=test_id)
    members_7 = guild.get_member(user_id=test_id)
    members_8 = guild.get_member(user_id=test_id)
    members_9 = guild.get_member(user_id=test_id)
    members_10 = guild.get_member(user_id=test_id)

    members = re.findall(r'(\d+)', members)

    try:
        members_1 = guild.get_member(user_id=int(members[0]))
        members_2 = guild.get_member(user_id=int(members[1]))
        members_3 = guild.get_member(user_id=int(members[2]))
        members_4 = guild.get_member(user_id=int(members[3]))
        members_5 = guild.get_member(user_id=int(members[4]))
        members_6 = guild.get_member(user_id=int(members[5]))
        members_7 = guild.get_member(user_id=int(members[6]))
        members_8 = guild.get_member(user_id=int(members[7]))
        members_9 = guild.get_member(user_id=int(members[8]))
        members_10 = guild.get_member(user_id=int(members[9]))
    except:
        pass

        # member = guild.get_member(user_id=int_id_member)

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(connect=False, create_instant_invite=False),
        # member : discord.PermissionOverwrite(connect=True ,speak=True),
        members_1: discord.PermissionOverwrite(connect=True, speak=True, create_instant_invite=False),
        members_2: discord.PermissionOverwrite(connect=True, speak=True, create_instant_invite=False),
        members_3: discord.PermissionOverwrite(connect=True, speak=True, create_instant_invite=False),
        members_4: discord.PermissionOverwrite(connect=True, speak=True, create_instant_invite=False),
        members_5: discord.PermissionOverwrite(connect=True, speak=True, create_instant_invite=False),
        members_6: discord.PermissionOverwrite(connect=True, speak=True, create_instant_invite=False),
        members_7: discord.PermissionOverwrite(connect=True, speak=True, create_instant_invite=False),
        members_8: discord.PermissionOverwrite(connect=True, speak=True, create_instant_invite=False),
        members_9: discord.PermissionOverwrite(connect=True, speak=True, create_instant_invite=False),
        members_10: discord.PermissionOverwrite(connect=True, speak=True, create_instant_invite=False),
        guild.me: discord.PermissionOverwrite(manage_channels=True, connect=True),
        nutyx_id: discord.PermissionOverwrite(connect=True, speak=True, administrator=True, manage_channels=True),
        alcry_id: discord.PermissionOverwrite(connect=True, speak=True, administrator=True, manage_channels=True),
    }

    await guild.create_voice_channel(category=ch, name=random_int, user_limit=int(count_user), overwrites=overwrites)


@bot.command()
async def del_vc(msg, chan: discord.VoiceChannel):
    """
    delete voice channel
    """
    await chan.delete()


@bot.command()
async def del_tc(msg, chan: discord.TextChannel):
    """
    delete text channel
    """
    await chan.delete()


@bot.command()
async def clear(ctx, count):
    """
    Удаления count предыдущих сообщений
    """
    # await loggins("request /clear", ctx.message.author, ctx.message.author.avatar_url)
    co = int(count) + 1
    await ctx.channel.purge(limit=co)


# _________________________________________________________________________________________________
# Печатать приветвенного текста.

@bot.command()
async def print_welcome_1(ctx):
    await ctx.channel.purge(limit=1)

    embed = discord.Embed(title='Добро пожаловать в Discord сервер международной ВТК "IMPERIAL"!', colour=discord.Colour(0x121892), description=cfg.txt_link_RU)

    embed.set_image(url="https://cdn.discordapp.com/attachments/660204377969000459/660220772773789706/52aa5420668fbffd.png")
    embed.set_author(name="ALCRY", url="https://truckersmp.com/user/1141907", icon_url="https://cdn.discordapp.com/attachments/660204377969000459/660231710780424214/yvpm.jpg")

    await ctx.send(embed=embed)


@bot.command()
async def print_welcome_2(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title='', colour=discord.Colour(0x121892), description=cfg.txt_info_RU)
    await ctx.send(embed=embed)


@bot.command()
async def print_welcome_3(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title='Welcome to Discord server of the international VTC "IMPERIAL"!', colour=discord.Colour(0x121892), description=cfg.txt_link_EN)

    embed.set_image(url="https://cdn.discordapp.com/attachments/660204377969000459/660220772773789706/52aa5420668fbffd.png")
    embed.set_author(name="ALCRY", url="https://truckersmp.com/user/1141907", icon_url="https://cdn.discordapp.com/attachments/660204377969000459/660231710780424214/yvpm.jpg")

    await ctx.send(embed=embed)


@bot.command()
async def print_welcome_4(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title='', colour=discord.Colour(0x121892), description=cfg.txt_info_EN)
    await ctx.send(embed=embed)


@bot.command()
async def print_wc1(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title='Добро пожаловать в ВТК "Imperial Trucking Company"!',
                          colour=discord.Colour(0x4334ff), description=cfg.txt_info_1)

    embed.set_image(url="https://cdn.discordapp.com/attachments/660204377969000459/660220772773789706/52aa5420668fbffd.png")
    embed.set_author(name="ALCRY", url="https://truckersmp.com/user/1141907", icon_url="https://cdn.discordapp.com/attachments/660204377969000459/660231710780424214/yvpm.jpg")
    await ctx.send(embed=embed)


@bot.command()
async def print_wc2(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send(file=discord.File('channels.png'))
    embed = discord.Embed(title='', colour=discord.Colour(0x3529ca), description=cfg.txt_info_2)
    await ctx.send(embed=embed)


@bot.command()
async def print_wc3(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send(file=discord.File('posit.png'))
    embed = discord.Embed(title='', colour=discord.Colour(0x251d8f), description=cfg.txt_info_3)
    await ctx.send(embed=embed)


@bot.command()
async def print_wc4(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send(file=discord.File('categ.png'))
    embed = discord.Embed(title='', colour=discord.Colour(0x18135a), description=cfg.txt_info_4)
    await ctx.send(embed=embed)


@bot.command()
async def print_wc5(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send(file=discord.File('links.png'))
    embed = discord.Embed(title='', colour=discord.Colour(0x050505), description=cfg.txt_links)
    await ctx.send(embed=embed)


# ____________________________________________________________________________________________________
@bot.command()
async def add_reaction(ctx, iddd: discord.Message):
    # dont use
    await ctx.channel.purge(limit=1)
    print(iddd)
    print(type(iddd))
    emoji = '<:troll_face:671342798791770112>'
    message = iddd
    await message.add_reaction(emoji)


@bot.command()
async def pml(ctx):
    position_staff_manager = ctx.guild.get_role(674962425229082634)
    position_hr_manager = ctx.guild.get_role(697181704753905665)
    position_manager_dt = ctx.guild.get_role(711274735081750555)
    position_manager_tl = ctx.guild.get_role(711339597086326834)
    position_manager_media = ctx.guild.get_role(669801637702795264)
    position_staff_dt = ctx.guild.get_role(673096405723643916)
    position_staff_cd = ctx.guild.get_role(602631192180817929)
    position_staff_hr = ctx.guild.get_role(739118581614247966)
    position_staff_media = ctx.guild.get_role(675798265509183508)
    position_CEO = ctx.guild.get_role(668240472090738709)
    position_staff_tl = ctx.guild.get_role(675797820388933663)
    position_staff_recruiter = ctx.guild.get_role(687658408354381869)
    position_COO = ctx.guild.get_role(669928692683636753)
    position_analytic = ctx.guild.get_role(696396963045703810)
    position_ceo_assistant = ctx.guild.get_role(669928692683636753)
    position_developer = ctx.guild.get_role(602805893020647434)
    position_community_manager = ctx.guild.get_role(719560209206608014)
    position_recruitment_manager = ctx.guild.get_role(723115670006398996)
    # PV1 = ctx.guild.get_role(644348628760002561)
    # PV3 = ctx.guild.get_role(644348725644361749)
    # position_senior_staff = ctx.guild.get_role(680821795179331674)

    trial_driver = ctx.guild.get_role(675801368296030222)
    junior_driver = ctx.guild.get_role(675799441005084682)
    driver_vtc = ctx.guild.get_role(675799435573461072)
    _versed_driver = ctx.guild.get_role(675799437104250900)  # 602815862390521893
    senior_driver = ctx.guild.get_role(675799439155396620)
    master_vtc = ctx.guild.get_role(676751936577339423)
    proffesional_vtc = ctx.guild.get_role(676751940163600403)
    expert_vtc = ctx.guild.get_role(676752984201232384)
    veteran_vtc = ctx.guild.get_role(676752983446388736)
    legenda_vtc = ctx.guild.get_role(675799409728159792)

    """
    exception bots:
    """
    bot_assistant_alcry = ctx.guild.get_member(668061143469654026)
    bot_ceo = ctx.guild.get_member(723316480640286731)
    bot_zx1 = ctx.guild.get_member(228537642583588864)
    bot_helper = ctx.guild.get_member(159985870458322944)
    bot_antoha_dj = ctx.guild.get_member(184405311681986560)

    # "\n".join([member.mention for member in ctx.guild.members if voditel_vtc in member.roles])
    return_CEO = "\n ⁣                              \n⁣⁣"
    return_CEO += "\n".join([member.mention for member in ctx.guild.members
                             if position_CEO in member.roles and member != bot_assistant_alcry])
    await ctx.send(embed=discord.Embed(title="Генеральный Директор Компании", colour=discord.Colour(0x1000e0), description=return_CEO))

    return_manager_HR = "\n ⁣                              \n⁣⁣"
    return_manager_HR += "\n".join([member.mention for member in ctx.guild.members if position_hr_manager in member.roles])
    await ctx.send(embed=discord.Embed(title="Исполнительный Директор Компании", colour=discord.Colour(0x673ab7), description=return_manager_HR))

    await ctx.send(file=discord.File(path_to_image_222))

    return_manager_TL = "\n ⁣                              \n⁣⁣"
    return_manager_TL += "\n".join([member.mention for member in ctx.guild.members if position_manager_tl in member.roles and member != bot_zx1])
    await ctx.send(embed=discord.Embed(title="Руководитель отдела транспортной логистики", colour=discord.Colour(0xff5200), description=return_manager_TL))

    return_manager_media = "\n ⁣                              \n⁣⁣"
    return_manager_media += "\n".join([member.mention for member in ctx.guild.members if position_manager_media in member.roles and member != bot_antoha_dj])
    await ctx.send(embed=discord.Embed(title="Руководитель отдела медиа планирования", colour=discord.Colour(0x00f3ff), description=return_manager_media))

    await ctx.send(file=discord.File(path_to_image_222))

    return_staff_cd = "\n ⁣                              \n⁣⁣"
    return_staff_cd += "\n".join([member.mention for member in ctx.guild.members if position_staff_cd in member.roles and member != bot_helper])
    await ctx.send(embed=discord.Embed(title="Координатор персонала", colour=discord.Colour(0x9961fd), description=return_staff_cd))

    return_dev_staff = "\n ⁣                              \n⁣⁣"
    return_dev_staff += "\n".join([member.mention for member in ctx.guild.members if position_developer in member.roles])
    await ctx.send(embed=discord.Embed(title="Разработчик", colour=discord.Colour(0x1565c0), description=return_dev_staff))

    await ctx.send(file=discord.File(path_to_image_222))

    return_staff_hr = "\n ⁣                              \n⁣⁣"
    return_staff_hr += "\n".join([member.mention for member in ctx.guild.members if position_staff_hr in member.roles and member != bot_helper])
    await ctx.send(embed=discord.Embed(title="Кадровый агент", colour=discord.Colour(0xc22525), description=return_staff_hr))

    return_staff_tl = "\n ⁣                              \n⁣⁣"
    return_staff_tl += "\n".join([member.mention for member in ctx.guild.members if position_staff_tl in member.roles])
    await ctx.send(embed=discord.Embed(title="Оператор транспортной логистики", colour=discord.Colour(0xca4a0d), description=return_staff_tl))

    return_staff_media = "\n ⁣                              \n⁣⁣"
    return_staff_media += "\n".join([member.mention for member in ctx.guild.members if position_staff_media in member.roles])
    await ctx.send(embed=discord.Embed(title="Медиа специалист", colour=discord.Colour(0x02bbc7), description=return_staff_media))

    """return_staff_recruiter = "\n ⁣                              \n⁣⁣"
    return_staff_recruiter += "\n".join(
        [member.mention for member in ctx.guild.members if position_staff_recruiter in member.roles])
    await ctx.send(embed=discord.Embed(title="Рекрутер персонала", colour=discord.Colour(0xbb1850),
                                       description=return_staff_recruiter))"""

    await ctx.send(file=discord.File(path_to_image_222))

    return_rank_legend = "\n ⁣                              \n⁣⁣"
    return_rank_legend += "\n".join([member.mention for member in ctx.guild.members if legenda_vtc in member.roles])
    await ctx.send(embed=discord.Embed(title="Легенда ВТК", colour=discord.Colour(0x6052ff), description=return_rank_legend))

    return_rank_veteran = "\n ⁣                              \n⁣⁣"
    return_rank_veteran += "\n".join([member.mention for member in ctx.guild.members if veteran_vtc in member.roles])
    await ctx.send(embed=discord.Embed(title="Ветеран ВТК", colour=discord.Colour(0x7064ff), description=return_rank_veteran))

    return_rank_expert = "\n ⁣                              \n⁣⁣"
    return_rank_expert += "\n".join([member.mention for member in ctx.guild.members if expert_vtc in member.roles])
    await ctx.send(embed=discord.Embed(title="Эксперт ВТК", colour=discord.Colour(0x7f75ff), description=return_rank_expert))

    return_rank_proffesional = "\n ⁣                              \n⁣⁣"
    return_rank_proffesional += "\n".join([member.mention for member in ctx.guild.members if proffesional_vtc in member.roles])
    await ctx.send(embed=discord.Embed(title="Профессионал ВТК", colour=discord.Colour(0xf02328), description=return_rank_proffesional))

    return_rank_master = "\n ⁣                              \n⁣⁣"
    return_rank_master += "\n".join([member.mention for member in ctx.guild.members if master_vtc in member.roles])
    await ctx.send(embed=discord.Embed(title="Мастер ВТК", colour=discord.Colour(0xda3438), description=return_rank_master))

    return_rank_senior_driver = "\n ⁣                              \n⁣⁣"
    return_rank_senior_driver += "\n".join([member.mention for member in ctx.guild.members if senior_driver in member.roles])
    await ctx.send(embed=discord.Embed(title="Cтарший водитель", colour=discord.Colour(0xcc3d40), description=return_rank_senior_driver))

    return_rank_versed_driver = "\n ⁣                              \n⁣⁣"
    return_rank_versed_driver += "\n".join([member.mention for member in ctx.guild.members if _versed_driver in member.roles])
    await ctx.send(embed=discord.Embed(title="Опытный водитель", colour=discord.Colour(0x01cc00), description=return_rank_versed_driver))

    return_rank_vtc_dr_driver = "\n ⁣                              \n⁣⁣"
    return_rank_vtc_dr_driver += "\n".join([member.mention for member in ctx.guild.members if driver_vtc in member.roles])
    await ctx.send(embed=discord.Embed(title="Водитель ВТК", colour=discord.Colour(0x01b900), description=return_rank_vtc_dr_driver))

    return_rank_junior_driver = "\n ⁣                              \n⁣⁣"
    return_rank_junior_driver += "\n".join([member.mention for member in ctx.guild.members if junior_driver in member.roles])
    await ctx.send(embed=discord.Embed(title="Младший водитель", colour=discord.Colour(0x009e00), description=return_rank_junior_driver))

    return_rank_trial_driver = "\n ⁣                              \n⁣⁣"
    return_rank_trial_driver += "\n".join([member.mention for member in ctx.guild.members if trial_driver in member.roles])
    await ctx.send(embed=discord.Embed(title="Стажер ВТК", colour=discord.Colour(0x0a8870), description=return_rank_trial_driver))


@bot.command()
async def nd(ctx, new_driver):
    # await get_log("Request /nd", ctx.message.author)
    # await loggins("request /nd", ctx.message.author, ctx.message.author.avatar_url)
    role_trial_driver = ctx.guild.get_role(675801368296030222)
    role_razdelitel_cathegoria = ctx.guild.get_role(677162694981451817)
    role_shtatniy_voditel = ctx.guild.get_role(573638017823277056)

    id_new_driver = ctx.guild.get_member(user_id=int(re.findall(r'(\d+)', new_driver)[0]))

    print(type(id_new_driver))
    print(id_new_driver)

    role_guest = ctx.guild.get_role(659889139767836692)
    try:
        await id_new_driver.remove_roles(role_guest, reason="request by {}".format(ctx.message.author))
    except:
        pass
    # embed = discord.Embed(title='', colour=discord.Colour(0xc40000), description="Новый клоун в нашей компании {}".format(new_driver))

    await id_new_driver.add_roles(role_trial_driver)
    await id_new_driver.add_roles(role_razdelitel_cathegoria)
    await id_new_driver.add_roles(role_shtatniy_voditel)

    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title='', colour=discord.Colour(0x9961fd), description='{} \n ```py\n"Утвержден на должность штатного водителя компании" ```'.format(new_driver))
    embed.set_author(name="Отдел управления персоналом", url="https://imperialvtc.com/", icon_url="https://cdn.discordapp.com/attachments/642462454512615489/664672245129674763/logo_novy_format3.png")
    await ctx.send(embed=embed)
    print("new driver in company - {} , by - {}".format(new_driver, ctx.message.author))


@bot.command()
async def driverlist(ctx):
    exception_role_upper_managemment = ctx.guild.get_role(617413284311859230)
    exception_role_adminstation = ctx.guild.get_role(692084303613657098)
    exception_role_trialdriver = ctx.guild.get_role(675801368296030222)
    member_dt1 = ctx.guild.get_role(573638017823277056)
    member_dt2 = ctx.guild.get_role(675801368296030222)
    junior_driver = ctx.guild.get_role(675799441005084682)
    driver_vtc = ctx.guild.get_role(675799435573461072)
    _versed_driver = ctx.guild.get_role(675799437104250900)
    senior_driver = ctx.guild.get_role(675799439155396620)
    master_vtc = ctx.guild.get_role(676751936577339423)
    proffesional_vtc = ctx.guild.get_role(676751940163600403)
    expert_vtc = ctx.guild.get_role(676752984201232384)
    veteran_vtc = ctx.guild.get_role(676752983446388736)
    legenda_vtc = ctx.guild.get_role(675799409728159792)
    # await ctx.channel.purge(limit=1)
    return_list_dt1 = "\n ⁣                              \n⁣⁣"
    return_list_dt1 += "\n".join([member.mention for member in ctx.guild.members
                                  if member_dt1 in member.roles and exception_role_adminstation not in member.roles and exception_role_upper_managemment not in member.roles and exception_role_trialdriver not in member.roles])
    await ctx.send(embed=discord.Embed(title="Штатные водители компании", colour=discord.Colour(0x1e88e5), description=return_list_dt1))

    return_list_dt2 = "\n ⁣                              \n⁣⁣"
    return_list_dt2 += "\n".join([member.mention for member in ctx.guild.members if member_dt2 in member.roles])
    await ctx.send(embed=discord.Embed(title="Водители на испытательном сроке", colour=discord.Colour(0x0a8870), description=return_list_dt2))

    await ctx.send(file=discord.File(path_to_image_123))

    return_rank_legend = "\n ⁣                              \n⁣⁣"
    return_rank_legend += "\n".join([member.mention for member in ctx.guild.members if legenda_vtc in member.roles])
    await ctx.send(embed=discord.Embed(title="Легенда ВТК", colour=discord.Colour(0x6052ff), description=return_rank_legend))

    return_rank_veteran = "\n ⁣                              \n⁣⁣"
    return_rank_veteran += "\n".join([member.mention for member in ctx.guild.members if veteran_vtc in member.roles])
    await ctx.send(embed=discord.Embed(title="Ветеран ВТК", colour=discord.Colour(0x7064ff), description=return_rank_veteran))

    return_rank_expert = "\n ⁣                              \n⁣⁣"
    return_rank_expert += "\n".join([member.mention for member in ctx.guild.members if expert_vtc in member.roles])
    await ctx.send(embed=discord.Embed(title="Эксперт ВТК", colour=discord.Colour(0x7f75ff), description=return_rank_expert))

    return_rank_proffesional = "\n ⁣                              \n⁣⁣"
    return_rank_proffesional += "\n".join([member.mention for member in ctx.guild.members if proffesional_vtc in member.roles])
    await ctx.send(embed=discord.Embed(title="Профессионал ВТК", colour=discord.Colour(0x958cff), description=return_rank_proffesional))

    return_rank_master = "\n ⁣                              \n⁣⁣"
    return_rank_master += "\n".join([member.mention for member in ctx.guild.members if master_vtc in member.roles])
    await ctx.send(embed=discord.Embed(title="Мастер ВТК", colour=discord.Colour(0x01cc00), description=return_rank_master))

    return_rank_senior_driver = "\n ⁣                              \n⁣⁣"
    return_rank_senior_driver += "\n".join([member.mention for member in ctx.guild.members if senior_driver in member.roles])
    await ctx.send(embed=discord.Embed(title="Cтарший водитель", colour=discord.Colour(0x01b900), description=return_rank_senior_driver))

    return_rank_versed_driver = "\n ⁣                              \n⁣⁣"
    return_rank_versed_driver += "\n".join([member.mention for member in ctx.guild.members if _versed_driver in member.roles])
    await ctx.send(embed=discord.Embed(title="Опытный водитель", colour=discord.Colour(0x009e00), description=return_rank_versed_driver))

    return_rank_vtc_dr_driver = "\n ⁣                              \n⁣⁣"
    return_rank_vtc_dr_driver += "\n".join([member.mention for member in ctx.guild.members if driver_vtc in member.roles])
    await ctx.send(embed=discord.Embed(title="Водитель ВТК", colour=discord.Colour(0x008800), description=return_rank_vtc_dr_driver))

    return_rank_junior_driver = "\n ⁣                              \n⁣⁣"
    return_rank_junior_driver += "\n".join([member.mention for member in ctx.guild.members if junior_driver in member.roles])
    await ctx.send(embed=discord.Embed(title="Младший водитель", colour=discord.Colour(0x006f00), description=return_rank_junior_driver))


@bot.command()
async def get(ctx, id):
    id = int(id)
    api_token = ''
    api_url_base = 'https://api.truckersmp.com/v2/player/{}'.format(id)
    print(api_url_base)
    jsonResponse = requests.get(api_url_base).json()

    embed = discord.Embed(title="Get information", url="https://truckersmp.com/user/{}".format(id), description="Инфомация о игроке", color=0xff0000)
    embed.set_author(name="IMPERIAL BOT", url="https://imperialvtc.com/", icon_url="https://cdn.discordapp.com/attachments/642462454512615489/664672245129674763/logo_novy_format3.png")
    embed.set_thumbnail(url=jsonResponse['response']['avatar'])
    embed.add_field(name="Дата регистрации TruckersMP", value=jsonResponse['response']['joinDate'], inline=False)
    embed.add_field(name="Steam ID", value=jsonResponse['response']['steamID'], inline=False)
    embed.add_field(name="TruckersMP ID", value=jsonResponse['response']['id'], inline=False)
    embed.add_field(name="Status in project", value=jsonResponse['response']['groupName'], inline=False)
    embed.add_field(name="В данный момент забанен", value=jsonResponse['response']['banned'], inline=False)
    embed.add_field(name="История банов скрыта", value=jsonResponse['response']['displayBans'], inline=False)
    embed.add_field(name="В команде TruckersMP", value=jsonResponse['response']['permissions'], inline=False)

    embed.set_footer(text="www.imperialvtc.com")
    await ctx.send(embed=embed)


@bot.command()
async def update_lists(ctx):
    # channgel id's
    channel_dev_staff_id = 660204377969000459
    channel_dev_01_id = 677134482477940746
    channel_dev_02_id = 677134500957782046
    channel_staff_list_id = 684699605027389451
    channel_drivers_list_not_staff_id = 707216632698634308

    channel_dev_01 = bot.get_channel(channel_dev_01_id)
    channel_dev_02 = bot.get_channel(channel_dev_02_id)
    channel_dev_staff = bot.get_channel(660204377969000459)
    channel_staff_list = bot.get_channel(channel_staff_list_id)
    channel_drivers_list_not_staff = bot.get_channel(channel_drivers_list_not_staff_id)

    await ctx.channel.purge(limit=1)
    await channel_drivers_list_not_staff.purge(limit=100)
    await channel_staff_list.purge(limit=100)

    await driverlist(channel_drivers_list_not_staff)
    await pml(channel_staff_list)
    # await channel_dev_staff.send("Обновление листов завершено.")


@bot.command()
async def log(ctx):
    await loggins("Тестирую логирование", ctx.message.author, ctx.message.author.avatar_url)


@bot.command()
async def loggins(text, author_request, author_request_avatar_url):
    # avatar author = ctx.message.author.avatar_url
    # who author = ctx.message.author
    nowtime = datetime.datetime.now()

    moderation_logs_channel = bot.get_channel(602938497107624025)
    channel_dev_staff = bot.get_channel(660204377969000459)

    embed = discord.Embed(title='', colour=discord.Colour(0x121892), description='{} {}'.format(author_request.mention, text))
    embed.set_author(name=author_request, url="https://imperialvtc.com/", icon_url=author_request_avatar_url)
    embed.set_footer(text="Server time: {}".format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M")))
    await moderation_logs_channel.send(embed=embed)


"""__________________________________________________________________________
Телеметрия 
__________________________________________________________________________
"""


@bot.command()
async def get_xy_city(ctx, name_sity):
    # channel_dev_staff = bot.get_channel(660204377969000459)
    api_url_base = "https://api.truckyapp.com/v2/map/cities/ets2"
    re = requests.get(api_url_base).json()
    print("test")
    print(name_sity)
    print(type(name_sity))
    for a in re['response']:
        # print("test 2")
        if a['realName'] == str(name_sity):
            print(a)
            await ctx.send(a)


def get_bool_access(ctx):
    channel_send_from_id = ctx.message.channel.id
    channel_developer_id = 677134482477940746
    channel_event_id = 761001031822737428
    channel_logitic = 670639477554675753
    channel_test_new_function = 761704568203116615
    date = datetime.datetime.now()
    try:
        if channel_send_from_id == channel_developer_id or channel_send_from_id == channel_event_id or channel_send_from_id == channel_logitic or channel_send_from_id == channel_test_new_function:
            return True
        else:
            embed = discord.Embed(title="IMPERIAL", url="https://imperialvtc.com/", description="ERROR", color=0xca041d)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/660204377969000459/660220772773789706/52aa5420668fbffd.png")
            embed.add_field(name="Warning", value="**Использован неверный канал для отправки запроса.**", inline=False)
            embed.set_footer(text="Server time: {}".format(date))
            return embed
    except:
        embed = discord.Embed(title="IMPERIAL", url="https://imperialvtc.com/", description="ERROR", color=0xca041d)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/660204377969000459/660220772773789706/52aa5420668fbffd.png")
        embed.add_field(name="Warning", value="**Critical error. Send again command.**", inline=False)
        embed.set_footer(text="Server time: {}".format(date))
        return embed


def get_bool_access_upper_command(ctx):
    date = datetime.datetime.now()
    author_id = ctx.message.author.id
    guild = bot.get_guild(567041857385660416)
    role_ceo = discord.utils.get(guild.roles, id=668240472090738709)
    role_developer = discord.utils.get(guild.roles, id=602805893020647434)
    role_coordinator = discord.utils.get(guild.roles, id=602631192180817929)
    # roles_user_send_message = discord.utils.get(guild.get_member, id=author_id)
    author_roles = ctx.message.author.roles
    try:
        if role_ceo in author_roles or role_developer in author_roles or role_coordinator in author_roles:
            return True
        else:
            embed = discord.Embed(title="IMPERIAL", url="https://imperialvtc.com/", description="Error", color=0xca041d)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/660204377969000459/660220772773789706/52aa5420668fbffd.png")
            embed.add_field(name="Warning", value="**У вас нет доступа к этой команде.**", inline=False)
            embed.set_footer(text="Server time: {}".format(date))
            return embed
    except:
        embed = discord.Embed(title="IMPERIAL", url="https://imperialvtc.com/", description="ERROR", color=0xca041d)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/660204377969000459/660220772773789706/52aa5420668fbffd.png")
        embed.add_field(name="Warning", value="**Critical error. Send again command.**", inline=False)
        embed.set_footer(text="Server time: {}".format(date))
        return embed



@bot.command()
async def new_event(ctx, number_event='none', start_point='none', break_point='none', end_point='none'):
    date = datetime.datetime.now()
    author_event = str(ctx.message.author)

    result_access = get_bool_access(ctx)
    if result_access != True:
        await ctx.send(embed=result_access)
        return

    convoy_leader = "Не назначен"
    if number_event == "none":
        await ctx.send('Проверьте введенные данные')
        return
    if start_point == "none":
        await ctx.send('Проверьте введенные данные')
        return
    if break_point == "none":
        await ctx.send('Проверьте введенные данные')
        return
    if end_point == "none":
        await ctx.send('Проверьте введенные данные')
        return

    """if check_valid_data(start_point,break_point,end_point) == True:
        pass
    else:
        embed = discord.Embed(title="IMPERIAL", url="https://imperialvtc.com/", description="Bug report", color=0xca041d)
        embed.set_author(name="Telemetria")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/660204377969000459/660220772773789706/52aa5420668fbffd.png")
        embed.add_field(name="Warning", value="**Проверьте правильность введенных данных.**", inline=False)
        embed.set_footer(text="Server time: {}".format(date))
        await ctx.send(embed=embed)
        return"""
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO History_convoys VALUES ('{}','{}','{}','{}')""".format(number_event, author_event, start_point, break_point))
    conn.commit()
    embed = discord.Embed(title="IMPERIAL", url="https://imperialvtc.com/", description="Создание мероприятия", color=0x4000f0)
    embed.set_author(name="Telemetria")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/660204377969000459/660220772773789706/52aa5420668fbffd.png")
    embed.add_field(name="Путевой лист №: ", value="{}".format(number_event), inline=False)
    embed.add_field(name="Точка старта: ", value="{}".format(start_point), inline=False)
    embed.add_field(name="Точка перерыва: ", value="{}".format(break_point), inline=False)
    embed.add_field(name="Точка финиша: ", value="{}".format(end_point), inline=False)
    embed.add_field(name="Создатель конвоя: ", value="{}".format(author_event), inline=False)
    embed.set_footer(text="Server time: {}".format(date))
    await ctx.send(embed=embed)


@bot.command()
async def online(ctx):
    author_message = ctx.message.author.id

    result_access = get_bool_access_upper_command(ctx)
    if result_access != True:
        await ctx.send(embed=result_access)
        return

    await ctx.send("Список Imperial VTC на серверах TruckersMP")
    # channel_dev_staff = bot.get_channel(660204377969000459)
    members = get_tmp_ids_members_vtc(1221)
    embed = discord.Embed(title="IMPERIAL", url="https://imperialvtc.com/", description="Результаты", color=0x4000f0)
    embed.set_author(name="Telemetria")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/660204377969000459/660220772773789706/52aa5420668fbffd.png")
    members = str(members)[1:-1]
    api_url_base = "https://api.truckyapp.com/v2/map/onlineList?ids={}".format(members)
    members = requests.get(api_url_base).json()['response']
    if members['error'] == True:
        ctx.send('Повторите запрос заново. Ошибка получения данных')
        return
    result = members['players']
    for member in result:
        if member['online'] == True:
            link_live_map_user = "https://web.truckyapp.com/map?follow={}".format(member['mp_id'])
            link_tmp_page = "https://truckersmp.com/user/{}".format(member['mp_id'])
            embed.add_field(name="{}".format(member['name']), value="TMP-ID: {}‌‌‍‍\nMP-ID: {}\nGame: {}\nServer: {}\nName Country: {}\n{}\n{}".format(member['mp_id'], member['p_id'], member['serverDetails']['game'], member['serverDetails']['name'], member['location']['poi']['realName'], link_live_map_user, link_tmp_page), inline=False)

    embed.set_footer(text="Server time: {}".format(datetime.datetime.now()))
    await ctx.send(embed=embed)


@bot.command()
async def event(ctx, command="none", number="none"):
    author = ctx.message.author
    date = datetime.datetime.now()

    result_access = get_bool_access(ctx)
    if result_access != True:
        await ctx.send(embed=result_access)
        return

    if command == "none":
        await ctx.send("Проверьте верность команды.\n/event start\n/event start_break\n/event end_break\n/event stop")
        return
    if command != "start" and command != "stop" and command != "start_break" and command != "end_break":
        await ctx.send("Проверьте верность команды.\n/event start\n/event start_break\n/event end_break\n/event stop")
        return
    if number == "none":
        await ctx.send("Укажите номер маршрутного листа")
        return
    await ctx.send("Please wait")
    if command == "start":
        result = c_start(number, author, ctx)
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=result)
    if command == "stop":
        result = c_stop(number, author, ctx)
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=result)
    if command == "start_break":
        result = s_break(number, author, ctx)
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=result)
    if command == "end_break":
        result = e_break(number, author, ctx)
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=result)

    print("/event done")


@bot.command()
async def get_result_event(ctx):
    date = datetime.datetime.now()
    author = ctx.message.author
    channel_send_from = ctx.message.channel.id

    result_access = get_bool_access_upper_command(ctx)
    if result_access != True:
        await ctx.send(embed=result_access)
        return

    result = calc_points_event()
    embed = discord.Embed(title="IMPERIAL", url="https://imperialvtc.com/", description="Результаты мероприятия", color=0x4000f0)
    embed.set_author(name="Telemetria")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/660204377969000459/660220772773789706/52aa5420668fbffd.png")
    embed.add_field(name="Путевой лист №:", value="pass", inline=False)
    embed.add_field(name="Зарегистрированные участники на старте:", value="{}".format(people_on_start), inline=False)
    embed.add_field(name="Зарегистрированные участники на старте перерыва:", value="{}".format(people_on_s_break), inline=False)
    embed.add_field(name="Зарегистрированные участники на финише перерыва:", value="{}".format(people_on_e_break), inline=False)
    embed.add_field(name="Зарегистрированные участники на финише :", value="{}".format(people_on_stop), inline=False)
    embed.add_field(name="Баллы: ", value="{}".format(result), inline=False)
    embed.set_footer(text="Server time: {}".format(date))
    await ctx.send(embed=embed)


def calc_points_event():
    global people_on_start
    global people_on_s_break
    global people_on_e_break
    global people_on_stop
    global points
    points = dict()

    for member in people_on_start:
        for member in people_on_s_break:
            points[member] = 2

    for member in people_on_e_break:
        for member in people_on_stop:
            points[member] = 2

    for member in people_on_start:
        for member in people_on_s_break:
            for member in people_on_e_break:
                for member in people_on_stop:
                    points[member] = 4

    return points


def get_tmp_ids_members_vtc(id_vtc):
    api_url_base = f"https://api.truckersmp.com/v2/vtc/{id_vtc}/members"
    re = requests.get(api_url_base).json()
    members = list()
    for member in re['response']['members']:
        members.append(member['user_id'])
    return members


points = dict()
people_on_start = list()
people_on_s_break = list()
people_on_e_break = list()
people_on_stop = list()


def c_start(id_route_list, author_start, ctx):
    try:
        date = datetime.datetime.now()
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        api_get_info_on_user = "https://api.truckyapp.com/v3/map/online?playerID={}"
        sql = "SELECT * FROM Convoys WHERE number=?"
        cursor.execute(sql, [(str(id_route_list))])
        info_on_bd_convoy = cursor.fetchall()
        all_members_imperial = get_tmp_ids_members_vtc(1221)
        global people_on_start
        people_on_start = list()
        for member in all_members_imperial:
            sostav = api_get_info_on_user.format(member)
            response = requests.get(sostav).json()
            if response['response']['online'] == True:
                if response['response']['location']['poi']['realName'] == info_on_bd_convoy[0][2]:
                    people_on_start.append(response['response']['name'])

        result_people_in_start = ''
        for member in people_on_start:
            member = str(member)
            result_people_in_start = result_people_in_start + "\n" + member

        embed = discord.Embed(title="IMPERIAL", url="https://imperialvtc.com/", description="Зарегистрирован старт рейса", color=0x4000f0)
        embed.set_author(name="Telemetria")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/660204377969000459/660220772773789706/52aa5420668fbffd.png")
        embed.add_field(name="Путевой лист №:", value="{}‌‌‍‍".format(id_route_list), inline=False)
        embed.add_field(name="Управляющий колонной", value="{}".format(author_start.mention), inline=False)
        embed.add_field(name="Старт", value="{}".format(info_on_bd_convoy[0][2]), inline=False)
        embed.add_field(name="Перерыв", value="{}".format(info_on_bd_convoy[0][3]), inline=False)
        embed.add_field(name="Финиш", value="{}".format(info_on_bd_convoy[0][4]), inline=False)
        embed.add_field(name="Зарегистрированные участники старта", value="{}".format(result_people_in_start), inline=False)
        embed.set_footer(text="Server time: {}".format(date))
        return embed
    except:
        embed = discord.Embed(title="IMPERIAL", url="https://imperialvtc.com/", description="Bug report", color=0xca041d)
        embed.set_author(name="Telemetria")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/660204377969000459/660220772773789706/52aa5420668fbffd.png")
        embed.add_field(name="Warning", value="**Проверьте правильность команды**", inline=False)
        embed.set_footer(text="Server time: {}".format(date))
        return embed


def s_break(id_route_list, author_start, ctx):
    try:
        date = datetime.datetime.now()
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        api_get_info_on_user = "https://api.truckyapp.com/v3/map/online?playerID={}"
        sql = "SELECT * FROM Convoys WHERE number=?"
        cursor.execute(sql, [(str(id_route_list))])
        info_on_bd_convoy = cursor.fetchall()
        all_members_imperial = get_tmp_ids_members_vtc(1221)
        global people_on_s_break
        people_on_s_break = list()
        for member in all_members_imperial:
            sostav = api_get_info_on_user.format(member)
            response = requests.get(sostav).json()
            if response['response']['online'] == True:
                if response['response']['location']['poi']['realName'] == info_on_bd_convoy[0][3]:
                    people_on_s_break.append(response['response']['name'])

        result_people_in_s_break = ''
        for member in people_on_s_break:
            member = str(member)
            result_people_in_s_break = result_people_in_s_break + "\n" + member

        embed = discord.Embed(title="IMPERIAL", url="https://imperialvtc.com/", description="Зарегистрирован старт перерыва рейса", color=0x4000f0)
        embed.set_author(name="Telemetria")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/660204377969000459/660220772773789706/52aa5420668fbffd.png")
        embed.add_field(name="Путевой лист №:", value="{}‌‌‍‍".format(id_route_list), inline=False)
        embed.add_field(name="Управляющий колонной", value="{}".format(author_start.mention), inline=False)
        embed.add_field(name="Старт", value="{}".format(info_on_bd_convoy[0][2]), inline=False)
        embed.add_field(name="Перерыв", value="{}".format(info_on_bd_convoy[0][3]), inline=False)
        embed.add_field(name="Финиш", value="{}".format(info_on_bd_convoy[0][4]), inline=False)
        embed.add_field(name="Зарегистрированные участники остановки", value="{}".format(result_people_in_s_break), inline=False)
        embed.set_footer(text="Server time: {}".format(date))
        return embed
    except:
        embed = discord.Embed(title="IMPERIAL", url="https://imperialvtc.com/", description="Bug report", color=0xca041d)
        embed.set_author(name="Telemetria")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/660204377969000459/660220772773789706/52aa5420668fbffd.png")
        embed.add_field(name="Warning", value="**Проверьте правильность команды**", inline=False)
        embed.set_footer(text="Server time: {}".format(date))
        return embed


def e_break(id_route_list, author_start, ctx):
    try:
        date = datetime.datetime.now()
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        api_get_info_on_user = "https://api.truckyapp.com/v3/map/online?playerID={}"
        sql = "SELECT * FROM Convoys WHERE number=?"
        cursor.execute(sql, [(str(id_route_list))])
        info_on_bd_convoy = cursor.fetchall()
        all_members_imperial = get_tmp_ids_members_vtc(1221)
        global people_on_e_break
        people_on_e_break = list()
        for member in all_members_imperial:
            sostav = api_get_info_on_user.format(member)
            response = requests.get(sostav).json()
            if response['response']['online'] == True:
                if response['response']['location']['poi']['realName'] == info_on_bd_convoy[0][3]:
                    people_on_e_break.append(response['response']['name'])

        result_people_in_e_break = ''
        for member in people_on_e_break:
            member = str(member)
            result_people_in_e_break = result_people_in_e_break + "\n" + member

        embed = discord.Embed(title="IMPERIAL", url="https://imperialvtc.com/", description="Зарегистрирован конец перерыва рейса", color=0x4000f0)
        embed.set_author(name="Telemetria")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/660204377969000459/660220772773789706/52aa5420668fbffd.png")
        embed.add_field(name="Путевой лист №:", value="{}‌‌‍‍".format(id_route_list), inline=False)
        embed.add_field(name="Управляющий колонной", value="{}".format(author_start.mention), inline=False)
        embed.add_field(name="Старт", value="{}".format(info_on_bd_convoy[0][2]), inline=False)
        embed.add_field(name="Перерыв", value="{}".format(info_on_bd_convoy[0][3]), inline=False)
        embed.add_field(name="Финиш", value="{}".format(info_on_bd_convoy[0][4]), inline=False)
        embed.add_field(name="Зарегистрированные участники остановки", value="{}".format(result_people_in_e_break), inline=False)
        embed.set_footer(text="Server time: {}".format(date))
        return embed
    except:
        embed = discord.Embed(title="IMPERIAL", url="https://imperialvtc.com/", description="Bug report", color=0xca041d)
        embed.set_author(name="Telemetria")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/660204377969000459/660220772773789706/52aa5420668fbffd.png")
        embed.add_field(name="Warning", value="**Проверьте правильность команды**", inline=False)
        embed.set_footer(text="Server time: {}".format(date))
        return embed


def c_stop(id_route_list, author_start, ctx):
    try:
        date = datetime.datetime.now()
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        api_get_info_on_user = "https://api.truckyapp.com/v3/map/online?playerID={}"
        sql = "SELECT * FROM Convoys WHERE number=?"
        cursor.execute(sql, [(str(id_route_list))])
        info_on_bd_convoy = cursor.fetchall()
        all_members_imperial = get_tmp_ids_members_vtc(1221)
        global people_on_stop
        people_on_stop = list()
        for member in all_members_imperial:
            sostav = api_get_info_on_user.format(member)
            response = requests.get(sostav).json()
            if response['response']['online'] == True:
                if response['response']['location']['poi']['realName'] == info_on_bd_convoy[0][4]:
                    people_on_stop.append(response['response']['name'])

        result_people_in_stop = ''
        for member in people_on_stop:
            member = str(member)
            result_people_in_stop = result_people_in_stop + "\n" + member

        embed = discord.Embed(title="IMPERIAL", url="https://imperialvtc.com/", description="Зарегистрирован финиш рейса", color=0x4000f0)
        embed.set_author(name="Telemetria")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/660204377969000459/660220772773789706/52aa5420668fbffd.png")
        embed.add_field(name="Путевой лист №:", value="{}‌‌‍‍".format(id_route_list), inline=False)
        embed.add_field(name="Управляющий колонной", value="{}".format(author_start.mention), inline=False)
        embed.add_field(name="Старт", value="{}".format(info_on_bd_convoy[0][2]), inline=False)
        embed.add_field(name="Перерыв", value="{}".format(info_on_bd_convoy[0][3]), inline=False)
        embed.add_field(name="Финиш", value="{}".format(info_on_bd_convoy[0][4]), inline=False)
        embed.add_field(name="Зарегистрированные участники финиша", value="{}".format(result_people_in_stop), inline=False)
        embed.set_footer(text="Server time: {}".format(date))
        return embed
    except:
        embed = discord.Embed(title="IMPERIAL", url="https://imperialvtc.com/", description="Bug report", color=0xca041d)
        embed.set_author(name="Telemetria")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/660204377969000459/660220772773789706/52aa5420668fbffd.png")
        embed.add_field(name="Warning", value="**Проверьте правильность команды**", inline=False)
        embed.set_footer(text="Server time: {}".format(date))
        return embed


async def uptime(ctx):
    pass


"""
________________________________________________________________________________________
Обновленная система телеметрии (использование эмоджи)
"""
"""@bot.command()
async def print_message_for_telemetrial(ctx):
    guild = ctx.guild
    ch = discord.utils.get(guild.categories, id=761704435423379476)
    random_int = random.randint(0, 10000)
    nutyx_id = guild.get_member(user_id=472517564690333697)
    alcry_id = guild.get_member(user_id=329214969897811969)
    test_number = 7788

    reaction_test = "👟"
    date = datetime.datetime.now()
    embed = discord.Embed(title="IMPERIAL", url="https://imperialvtc.com/", description="Test message",color=0xca041d)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/660204377969000459/660220772773789706/52aa5420668fbffd.png")
    embed.add_field(name="Warning", value="**Просто тестим**", inline=False)
    embed.set_footer(text="Server time: {}".format(date))
    _message = await ctx.send(embed=embed)

    await _message.add_reaction(cfg.emj_game_spintires)
    await _message.add_reaction(cfg.emj_truckersmp_blog)
    await _message.add_reaction(reaction_test)

async def create_new_channel_with_number_convoy_lit(guild):
    test_number = 7788
    #guild = ctx.guild
    ch = discord.utils.get(guild.categories, id=761704435423379476)
    role_drive = discord.utils.get(guild.roles, id=573638017823277056)
    anban_id = guild.get_member(user_id=472517564690333697)
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True),
        role_drive: discord.PermissionOverwrite(read_messages=False),
        anban_id: discord.PermissionOverwrite(read_messages=True, administrator=True, manage_channels=True)
    }
    channel_event = await guild.create_text_channel(category=ch,name=test_number, overwrites=overwrites)
    #return channel_event"""

# slow_count.start()
bot.run(token)

# Пример логирования на команды
# await loggins("/update_lists", ctx.message.author, ctx.message.author.avatar_url)

# await ctx.send(file=discord.File(data, '1gen_dir.png'))
