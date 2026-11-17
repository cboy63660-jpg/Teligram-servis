import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

TOKEN = "8990328066:AAH3IEdURkPchZ7UVa95hg8LZJxG_8Ah99w"
UPI_ID = "chetramsingh905@upi"

PLANS = {
    "child_corn": {
        "name": "🔥 CH!LD CORN 🥵💦",
        "amount": "149",
        "videos": "20000+ PRIVATE VIDEOS",
    },
    "animal_girls": {
        "name": "🔥 ANIMAL GIRLS SAX 💋",
        "amount": "76",
        "videos": "10000+ PRIVATE VIDEOS",
    },
    "insta_leaks": {
        "name": "🍑 INSTA LEAKS INFULENCER 🍑",
        "amount": "66",
        "videos": "15000+ PRIVATE VIDEOS",
    },
    "bro_sister": {
        "name": "💀 BRO SISTER 💦",
        "amount": "68",
        "videos": "8000+ PRIVATE VIDEOS",
    },
    "boy_gay": {
        "name": "🥵 BOY GAY VIDEOS",
        "amount": "88",
        "videos": "12000+ PRIVATE VIDEOS",
    },
    "rape_videos": {
        "name": "🥵 R@PE VIDEOSS 💦",
        "amount": "96",
        "videos": "14000+ PRIVATE VIDEOS",
    },
    "all_in_one": {
        "name": "❤️‍🔥 All in one pack",
        "amount": "180",
        "videos": "1 Lakh+ PRIVATE VIDEOS",
    },
    "ultra_vip": {
        "name": "🔥 ULTRA VIP 👑 (1 lakh videos)",
        "amount": "298",
        "videos": "1 Lakh+ VIP VIDEOS",
    },
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  keyboard = [
      [
          InlineKeyboardButton(
              "🥵 CH!LD CORN 💦 • ₹149", callback_data="plan_child_corn"
          )
      ],
      [
          InlineKeyboardButton(
              "💋 ANIMAL GIRLS SAX 💋 • ₹76", callback_data="plan_animal_girls"
          )
      ],
      [
          InlineKeyboardButton(
              "🍑 INSTA LEAKS INFULENCER 🍑 • ₹66",
              callback_data="plan_insta_leaks",
          )
      ],
      [
          InlineKeyboardButton(
              "💀 BRO SISTER 💦 • ₹68", callback_data="plan_bro_sister"
          )
      ],
      [
          InlineKeyboardButton(
              "🥵 BOY GAY VIDEOS • ₹88", callback_data="plan_boy_gay"
          )
      ],
      [
          InlineKeyboardButton(
              "🥵 R@PE VIDEOSS 💦 • ₹96", callback_data="plan_rape_videos"
          )
      ],
      [
          InlineKeyboardButton(
              "❤️‍🔥 All in one pack • ₹180", callback_data="plan_all_in_one"
          )
      ],
      [
          InlineKeyboardButton(
              "🔥 ULTRA VIP 👑 (1 lakh videos) • ₹298",
              callback_data="plan_ultra_vip",
          )
      ],
      # Yeh raha Proofs aur Demo ka link
      [
          InlineKeyboardButton(
              "📸 1 Lakh Proofs", url="https://t.me/+hNRQIJqDDRVhMGU1"
          )
      ],
      [
          InlineKeyboardButton(
              "🎬 Demo", url="https://t.me/+CDKt29m-_JI4NzU1"
          )
      ],
  ]

  reply_markup = InlineKeyboardMarkup(keyboard)
  text = (
      "👑 **MONO PAID SERVICE** 👑\n"
      "35,672 monthly users\n\n"
      "1 Lakh+ videos At just ₹180/-\n"
      "All Categories in One Package\n\n"
      "💰 **ONE TIME PAYMENT**\n"
      "💯 **LIFETIME ACCESS**\n"
      "✅ **DIRECT VIDEOS GROUP**\n\n"
      "Starting AT ₹66/- Don't miss it !! 👑\n\n"
      "👇 **Choose a plan below:**"
  )
  await update.message.reply_text(text, reply_markup=reply_markup)


async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
  query = update.callback_query
  await query.answer()
  data = query.data

  if data == "main_menu":
    await start_menu_edit(query)
    return

  if data.startswith("plan_"):
    plan_key = data.replace("plan_", "")
    plan = PLANS[plan_key]

    text = (
        f"🐉 Plan: {plan['name']}\n"
        f"💸 Amount: ₹{plan['amount']}\n"
        f"**{plan['videos']}**\n\n"
        "👉 *These are demos. Confirm to buy?*"
    )

    keyboard = [
        [
            InlineKeyboardButton(
                "✅ Confirm", callback_data=f"confirm_{plan_key}"
            ),
            InlineKeyboardButton("🔙 Back", callback_data="main_menu"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text, reply_markup=reply_markup, parse_mode="Markdown"
    )

  elif data.startswith("confirm_"):
    plan_key = data.replace("confirm_", "")
    plan = PLANS[plan_key]

    txn_id = f"TXN-261117-{random.randint(10000, 99999)}"
    context.user_data["current_plan"] = plan["name"]
    context.user_data["current_amount"] = plan["amount"]
    context.user_data["txn_id"] = txn_id

    upi_payment_link = (
        f"upi://pay?pa={UPI_ID}&pn=PaidService&am={plan['amount']}&cu=INR"
    )

    text = (
        "🔥 **Pay To Get Paid Access**\n\n"
        f"🆔 **TXN:** `{txn_id}`\n"
        f"💲 **UPI ID:** `{UPI_ID}` ✅ (tap to copy)\n\n"
        f"🐉 Plan: {plan['name']}\n"
        f"💸 Amount: ₹{plan['amount']}\n\n"
        f"[👉 CLICK HERE TO PAY VIA UPI APPS]({upi_payment_link})\n\n"
        "UPI ID copy karke ya upar link par click karke exact amount pay karein."
    )

    keyboard = [
        [
            InlineKeyboardButton(
                "📸 Send Payment Screenshot", callback_data="send_ss"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 Back", callback_data=f"plan_{plan_key}"
            )
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text, reply_markup=reply_markup, parse_mode="Markdown"
    )

  elif data == "send_ss":
    txn_id = context.user_data.get("txn_id", "TXN-261117-18278")
    amount = context.user_data.get("current_amount", "149")

    text = (
        "📸 **Send Payment Screenshot**\n\n"
        f"🆔 **TXN:** `{txn_id}`\n"
        f"💲 **₹{amount}**\n\n"
        "Upload the screenshot of your successful payment here as a photo.\n\n"
        "Send `/cancel` to abort."
    )
    await query.edit_message_text(text, parse_mode="Markdown")
    context.user_data["waiting_for_screenshot"] = True


async def start_menu_edit(query):
  keyboard = [
      [
          InlineKeyboardButton(
              "🥵 CH!LD CORN 💦 • ₹149", callback_data="plan_child_corn"
          )
      ],
      [
          InlineKeyboardButton(
              "💋 ANIMAL GIRLS SAX 💋 • ₹76", callback_data="plan_animal_girls"
          )
      ],
      [
          InlineKeyboardButton(
              "🍑 INSTA LEAKS INFULENCER 🍑 • ₹66",
              callback_data="plan_insta_leaks",
          )
      ],
      [
          InlineKeyboardButton(
              "💀 BRO SISTER 💦 • ₹68", callback_data="plan_bro_sister"
          )
      ],
      [
          InlineKeyboardButton(
              "🥵 BOY GAY VIDEOS • ₹88", callback_data="plan_boy_gay"
          )
      ],
      [
          InlineKeyboardButton(
              "🥵 R@PE VIDEOSS 💦 • ₹96", callback_data="plan_rape_videos"
          )
      ],
      [
          InlineKeyboardButton(
              "❤️‍🔥 All in one pack • ₹180", callback_data="plan_all_in_one"
          )
      ],
      [
          InlineKeyboardButton(
              "🔥 ULTRA VIP 👑 (1 lakh videos) • ₹298",
              callback_data="plan_ultra_vip",
          )
      ],
      [
          InlineKeyboardButton(
              "📸 1 Lakh Proofs", url="https://t.me/+hNRQIJqDDRVhMGU1"
          )
      ],
      [
          InlineKeyboardButton(
              "🎬 Demo", url="https://t.me/+CDKt29m-_JI4NzU1"
          )
      ],
  ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  text = (
      "👑 **MONO PAID SERVICE** 👑\n"
      "35,672 monthly users\n\n"
      "1 Lakh+ videos At just ₹180/-\n"
      "All Categories in One Package\n\n"
      "💰 **ONE TIME PAYMENT**\n"
      "💯 **LIFETIME ACCESS**\n"
      "✅ **DIRECT VIDEOS GROUP**\n\n"
      "Starting AT ₹66/- Don't miss it !! 👑\n\n"
      "👇 **Choose a plan below:**"
  )
  try:
    await query.edit_message_text(text, reply_markup=reply_markup)
  except Exception:
    await query.message.reply_text(text, reply_markup=reply_markup)


async def handle_screenshot(update: Update, context: ContextTypes.DEFAULT_TYPE):
  if context.user_data.get("waiting_for_screenshot"):
    await update.message.reply_text(
        "✅ **Screenshot Received Successfully!**\n\n"
        "Aapki payment verify ki ja rahi hai. Thodi der mein aapko group ka link mil jayega.",
        parse_mode="Markdown",
    )
    context.user_data["waiting_for_screenshot"] = False


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
  context.user_data["waiting_for_screenshot"] = False
  await update.message.reply_text(
      "Process cancelled. Use /start to view menu again."
  )


if __name__ == "__main__":
  application = ApplicationBuilder().token(TOKEN).build()
  application.add_handler(CommandHandler("start", start))
  application.add_handler(CommandHandler("cancel", cancel))
  application.add_handler(CallbackQueryHandler(button_click))
  application.add_handler(
      MessageHandler(filters.PHOTO & ~filters.COMMAND, handle_screenshot)
  )
  print("Bot is running...")
  application.run_polling()
