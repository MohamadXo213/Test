import telebot

bot = telebot.TeleBot("5285225106:AAHpgVWSu-im_uB2tSX8YOFYbVS094nKtMQ")

lista = {
	"الأرشيفات" : "🍃",
	"مؤسسة الخير الإعلامية" : "https://t.me/ARCHIVE_63",
	"خدمات الأنصار" : "https://t.me/Archive_Ansarr_Services",
	"مؤسسة صرح الخلافة" : "https://t.me/Archive_3000",
	"الغلام الدولاوي" : "https://t.me/Algoolam_135_bot",
	"مؤسسة إرث الخـلافة الإعلامية" : "https://t.me/iRTH1443",

	"القنوات الإخبارية" : "🍃",
	"الإعلام مالركزي" : "https://t.me/ggff26",
	"قناة IR EV" : "https://t.me/IRA_EVE",
	"ناعور العراق" : "https://t.me/n3o3r",
	"ناعور سوريا" : "https://t.me/NA3ORSYRIA",
	"ناعور كردى" : "https://t.me/na3or",
	"وكالة أخبار الشام" : "https://t.me/Al_Sham_News1",
	"ناعور للمقالات" : "https://t.me/DRNASART",
	"مجريات أحداث 2021" : "https://t.me/mogryata7dath2021",
	"صلاح الدين الحدث" : "https://t.me/SDNEWS8",
	
	"توزيع الأرقام والحسابات" : "🍃",
	"بنك الأنصار - حسابات" : "https://t.me/Alansarb1443",
	"بنك الأنصار - أرقام" : "https://t.me/Bankofno",
	"فرسان العقيدة" : "https://t.me/furrsan_ff_bot",
	
	"المجموعات" : "🍃",
	"منتدى شباب الجزيرة" : "https://t.me/jaabjZvx",
	"مجموعة ناشر " : "https://t.me/nashr7j",


	"قنوات أخرى" : "🍃",
	"علوا الهمة" : "https://t.me/ELO_ALHEMA",
	"عـفــيـفــات فـي زمـن الـفـتـن" : "https://t.me/Afifat3",
	"مجزأة - Quraísh" : "https://t.me/db96rs",
	"#بيعة_الموت" : "https://t.me/a_s_h_y_r_u_1876",
	"أحداث معركة غويران" : "https://t.me/A7DaTh_IS",
	"خبر عاجل" : "https://t.me/khabar_news1188",
	
	"المواقع" : "🍃",
	"موقع الرعود" : "https://al-raud.fun",
	"موقع مؤسسة أعلام" : "https://i3l.in",
	"موقع مؤسسة آفاق الألكترونية" : "https://ehorizons.cc",

}
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	help_msg = "🌷 القائمة 🌷"
	help_msg += "\n"
	num = 0
	for i in lista:
		if lista[i] == "🍃":
			help_msg += "\n🍃 " + i + " : \n"
		else:
			num += 1
			help_msg += str(num) + " - " + i + "\n"
	help_msg += "\n"
	help_msg += " ❖ إعداد : إخوانكم في ( جيش الخلافة الإلكتروني )."
	help_msg += "\n"
	help_msg += " ❖ في حال تم حذف البوت فقط أكتب في البحث ( زاد المناصر ) وسوف تجده إن شاء الله."
	help_msg += "\n"
	help_msg += " ❖ للتواصل :  ( @KIA_X1 )."
	help_msg += "\n"
	help_msg += "https://t.me/ZAD_1_bot"
	bot.reply_to(message, help_msg)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	try:
		int(message.text)
		array = list(lista.values())
		for i in array:
			if i == "🍃":
				array.remove(i)
		replay = array[int(message.text) - 1]
		if replay == "":
			bot.reply_to(message, "محذوف - سوف نضيفه حالما يتم أنشاء آخر جديد")
		else:
			bot.reply_to(message, replay)
	except:
		pass

bot.polling()
