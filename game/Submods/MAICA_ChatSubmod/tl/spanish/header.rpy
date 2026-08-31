# TODO: Translation updated at 2024-07-07 20:52

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:140
    old "Not connected"
    new "No conectado"
    # game/Submods/MAICA_ChatSubmod/header.rpy:140
    old "Connection established"
    new "Conexión establecida"
    # game/Submods/MAICA_ChatSubmod/header.rpy:140
    old "Connection closed"
    new "Conexión cerrada"
    # game/Submods/MAICA_ChatSubmod/header.rpy:147
    old "> MAICA connection status: [maica.maica_instance.status]|[maica.maica_instance.MaicaAiStatus.get_description(maica.maica_instance.status)]"
    new "> Estado de conexión MAICA: [maica.maica_instance.status]|[maica.maica_instance.MaicaAiStatus.get_description(maica.maica_instance.status)]"
    old "> Provider list refresh failed: "
    new "> Provider list refresh failed: "
    # game/Submods/MAICA_ChatSubmod/header.rpy:151
    old "> Websocket: [stat]"
    new "> Websocket: [stat]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:157
    old "> Generate token"
    new "> Generar token"
    # game/Submods/MAICA_ChatSubmod/header.rpy:160
    old "> Connect with current token"
    new "> Conectar con token actual"
    # game/Submods/MAICA_ChatSubmod/header.rpy:165
    old "> Upload savefile information"
    new "> Subir información del archivo guardado"
    # game/Submods/MAICA_ChatSubmod/header.rpy:168
    old "> Reset current session"
    new "> Reiniciar sesión actual"
    # game/Submods/MAICA_ChatSubmod/header.rpy:171
    old "> Export current session"
    new "> Exportar sesión actual"
    # game/Submods/MAICA_ChatSubmod/header.rpy:174
    old "> Lougout current account"
    new "> Cerrar sesión de cuenta actual"
    # game/Submods/MAICA_ChatSubmod/header.rpy:177
    old "> MAICA params and settings *some options may need reconnection"
    new "> Parámetros y configuración de MAICA *algunas opciones pueden necesitar reconexión"
    # game/Submods/MAICA_ChatSubmod/header.rpy:201
    old "Total conversation rounds: [store.maica.maica_instance.stat.get('message_count')]"
    new "Total de rondas de conversación: [store.maica.maica_instance.stat.get('message_count')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:204
    old "Total chunks received: [store.maica.maica_instance.stat.get('received_token')]"
    new "Total de chunks recibidos: [store.maica.maica_instance.stat.get('received_token')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:206
    old "Reset statistics"
    new "Reiniciar estadísticas"
    # game/Submods/MAICA_ChatSubmod/header.rpy:211
    old "Auto reconnect: [persistent.maica_setting_dict.get('auto_connect')]"
    new "Reconexión automática: [persistent.maica_setting_dict.get('auto_connect')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:213
    old "Automatically reconnect on connection close"
    new "Reconectar automáticamente al cerrar conexión"
    # game/Submods/MAICA_ChatSubmod/header.rpy:216
    old "Current MAICA model: [persistent.maica_setting_dict.get('maica_model')]"
    new "Modelo MAICA actual: [persistent.maica_setting_dict.get('maica_model')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:218
    old "maica_main: MAICA full functionality; maica_core: MAICA LLM functionality\nmaica_main has a higher response latency"
    new "maica_main: funcionalidad completa de MAICA; maica_core: funcionalidad LLM de MAICA\nmaica_main tiene mayor latencia de respuesta"
    # game/Submods/MAICA_ChatSubmod/header.rpy:222
    old "Target language: [persistent.maica_setting_dict.get('target_lang')]"
    new "Idioma objetivo: [persistent.maica_setting_dict.get('target_lang')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:224
    old "The language you prefer recieving\nAchieved by modding system prompt, cannot guarantee correct output"
    new "El idioma que prefieres recibir\nLogrado modificando el system prompt, no garantiza una salida correcta"
    # game/Submods/MAICA_ChatSubmod/header.rpy:229
    old "Use advanced parameters: [persistent.maica_setting_dict.get('use_custom_model_config')]"
    new "Usar parámetros avanzados: [persistent.maica_setting_dict.get('use_custom_model_config')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:231
    old "Make sure config file custom_modelconfig.json makes sense before use"
    new "Asegúrate de que el archivo config custom_modelconfig.json tenga sentido antes de usar"
    # game/Submods/MAICA_ChatSubmod/header.rpy:234
    old "Flush options"
    new "Actualizar opciones"
    # game/Submods/MAICA_ChatSubmod/header.rpy:238
    old "Use persistent file: [persistent.maica_setting_dict.get('savefile_access')]"
    new "Use persistent file: [persistent.maica_setting_dict.get('savefile_access')]"
    old "Model will ignore savefile data if this is disabled.\n! savefile_access marker does not exist, savefile will not be uploaded or applied"
    new "Model will ignore savefile data if this is disabled.\n! savefile_access marker does not exist, savefile will not be uploaded or applied"
    # game/Submods/MAICA_ChatSubmod/header.rpy:240
    old "Decides if use uploaded savefile or not\nMust have savefile uploaded if set to on"
    new "Decide si usar archivo guardado subido o no\nDebe tener archivo guardado subido si está activado"
    # game/Submods/MAICA_ChatSubmod/header.rpy:244
    old "Session currently in use: [persistent.maica_setting_dict.get('chat_session')]"
    new "Sesión actualmente en uso: [persistent.maica_setting_dict.get('chat_session')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:246
    old "Disable session storage by setting chat_session 0. Sessions use savefiles individually"
    new "Deshabilita almacenamiento de sesión estableciendo chat_session en 0. Las sesiones usan archivos guardados individualmente"
    # game/Submods/MAICA_ChatSubmod/header.rpy:250
    old "Debugging console: [persistent.maica_setting_dict.get('console')]"
    new "Consola de depuración: [persistent.maica_setting_dict.get('console')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:252
    old "Show debugging console while chatting\nI think this looks cool xd"
    new "Mostrar consola de depuración mientras chateas\nCreo que esto se ve genial XD"
    # game/Submods/MAICA_ChatSubmod/header.rpy:256
    old "Purge additional player preferences: currently [len(persistent.mas_player_additions)]"
    new "Eliminar preferencias adicionales del jugador: actualmente [len(persistent.mas_player_additions)]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:258
    old "Player complemented preferences data"
    new "Datos de preferencias complementadas por el jugador"
    # game/Submods/MAICA_ChatSubmod/header.rpy:261
    old "Export to directory"
    new "Exportar a directorio"
    # game/Submods/MAICA_ChatSubmod/header.rpy:263
    old "Export to game/Submods/MAICA_ChatSubmod/player_info.txt"
    new "Export to game/Submods/MAICA_ChatSubmod/player_info.txt"
    # game/Submods/MAICA_ChatSubmod/header.rpy:270
    old "Save settings"
    new "Guardar configuración"
    # game/Submods/MAICA_ChatSubmod/header.rpy:292
    old "Enter DCC username "
    new "Ingrese nombre de usuario DCC "
    # game/Submods/MAICA_ChatSubmod/header.rpy:294
    old "or "
    new "o "
    # game/Submods/MAICA_ChatSubmod/header.rpy:295
    old "Enter DCC register email{#maica_register_prompt}"
    new "Ingrese email de registro DCC"
    # game/Submods/MAICA_ChatSubmod/header.rpy:296
    old "Enter DCC register email"
    new "Ingrese email de registro DCC"
    # game/Submods/MAICA_ChatSubmod/header.rpy:299
    old "Enter DCC password{#maica_register_prompt}"
    new "Ingrese contraseña DCC"
    # game/Submods/MAICA_ChatSubmod/header.rpy:300
    old "Enter DCC password"
    new "Ingrese contraseña DCC"
    # game/Submods/MAICA_ChatSubmod/header.rpy:305
    old "Generate token online"
    new "Generar token en línea"
    # game/Submods/MAICA_ChatSubmod/header.rpy:312
    old "Generate token"
    new "Generar token"
    # game/Submods/MAICA_ChatSubmod/header.rpy:318
    old "Cancel{#maica_host_cancel}"
    new "Cancelar"
# TODO: Translation updated at 2024-07-09 18:46

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:99
    old "Upload success"
    new "Subida exitosa"
    # game/Submods/MAICA_ChatSubmod/header.rpy:99
    old "Upload failed"
    new "Subida fallida"
    # game/Submods/MAICA_ChatSubmod/header.rpy:140
    old "Failed initializing advanced params, check submod_log.log"
    new "Falló la inicialización de parámetros avanzados, revisa submod_log.log"
    # game/Submods/MAICA_ChatSubmod/header.rpy:220
    old "Auto reconnect: [persistent.maica_setting_dict.get('auto_reconnect')]"
    new "Reconexión automática: [persistent.maica_setting_dict.get('auto_reconnect')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:264
    old "Console font: [persistent.maica_setting_dict.get('console_font')]"
    new "Fuente de consola: [persistent.maica_setting_dict.get('console_font')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:266
    old "Decides what font should console display in. \nmplus-1mn-medium.ttf for default, SarasaMonoTC-SemiBold.ttf may behave better with non-ascii characters."
    new "Decide en qué fuente debe mostrarse la consola.\nmplus-1mn-medium.ttf por defecto, SarasaMonoTC-SemiBold.ttf puede comportarse mejor con caracteres no ascii."
    # game/Submods/MAICA_ChatSubmod/header.rpy:272
    old "User defined preference data, needs re-uploading savefile to take effect"
    new "Datos de preferencia definidos por usuario, necesita re-subir archivo guardado para tomar efecto"
    # game/Submods/MAICA_ChatSubmod/header.rpy:276
    old "Add preference"
    new "Agregar preferencia"
    # game/Submods/MAICA_ChatSubmod/header.rpy:277
    old "Preference addition will be sent on closing settings"
    new "Adición de preferencia será enviada al cerrar configuración"
    # game/Submods/MAICA_ChatSubmod/header.rpy:282
    old "Click me to push events"
    new "Haz click para enviar eventos"
    # game/Submods/MAICA_ChatSubmod/header.rpy:329
    old "Enter DCC account username{#maica_legacy_header}"
    new "Ingrese nombre de usuario de cuenta DCC"
# TODO: Translation updated at 2024-07-11 22:18

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:289
    old "Edit information"
    new "Editar información"
    # game/Submods/MAICA_ChatSubmod/header.rpy:306
    old "MSpire: [persistent.maica_setting_dict.get('mspire_enable')]"
    new "MSpire: [persistent.maica_setting_dict.get('mspire_enable')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:308
    old "Enable or disable MSpire topics generation. Turn off repetive conversation to take effect."
    new "Habilitar o deshabilitar generación de temas MSpire. Apaga conversación repetitiva para tomar efecto."
    # game/Submods/MAICA_ChatSubmod/header.rpy:311
    old "Edit topic range"
    new "Editar rango de temas"
    # game/Submods/MAICA_ChatSubmod/header.rpy:317
    old "The range should be the title of a wikipedia category page"
    new "El rango debe ser el título de una página de categoría de wikipedia"
    # game/Submods/MAICA_ChatSubmod/header.rpy:320
    old "Interval: [persistent.maica_setting_dict.get('mspire_interval')] Minute(s)"
    new "Intervalo: [persistent.maica_setting_dict.get('mspire_interval')] Minuto(s)"
    # game/Submods/MAICA_ChatSubmod/header.rpy:325
    old "The minimum interval triggering MSpire"
    new "El intervalo mínimo activando MSpire"
    # game/Submods/MAICA_ChatSubmod/header.rpy:330
    old "submod_log.log verbosity: [logging.getLevelName(store.mas_submod_utils.submod_log.level)]"
    new "Verbosidad submod_log.log: [logging.getLevelName(store.mas_submod_utils.submod_log.level)]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:332
    old "Filter lower level logs\nThis affects every installed submod"
    new "Filtrar logs de nivel inferior\nEsto afecta cada submod instalado"
# TODO: Translation updated at 2024-08-04 13:15

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:280
    old "{a=https://github.com/Mon1-innovation/MAICA/blob/main/document/API%20Documents.md#调整设置}{i}{u}Official document of MAICA API{/u}{/i}{/a}"
    new "{a=https://github.com/Mon1-innovation/MAICA/blob/main/document/API%20Documents.md#调整设置}{i}{u}Documento oficial de la API de MAICA{/u}{/i}{/a}"
    # game/Submods/MAICA_ChatSubmod/header.rpy:282
    old "{a=https://platform.openai.com/docs/api-reference/chat}{i}{u}OPENAI documents{/u}{/i}{/a}"
    new "{a=https://platform.openai.com/docs/api-reference/chat}{i}{u}OPENAI documents{/u}{/i}{/a}"
    # game/Submods/MAICA_ChatSubmod/header.rpy:287
    old "The token choice range in sequence of probability. Model will only choose the next token from the top_p/1 former part of all tokens."
    new "El rango de elección de tokens en secuencia de probabilidad. El modelo solo elegirá el siguiente token desde la parte anterior top_p/1 de todos los tokens."
    # game/Submods/MAICA_ChatSubmod/header.rpy:301
    old "The randomness of output. Temperature was added to token weights to dilute their default probabilities, so higher temperature suggests creativity and lower suggests precision."
    new "La aleatoriedad de salida. La temperatura se agregó a los pesos de tokens para diluir sus probabilidades predeterminadas, así que mayor temperatura sugiere creatividad y menor sugiere precisión."
    # game/Submods/MAICA_ChatSubmod/header.rpy:312
    old "The max length model can output in a single round. Model will try to fit this value but oversized responses will be chopped."
    new "La longitud máxima que el modelo puede output en una sola ronda. El modelo intentará ajustar este valor pero respuestas sobredimensionadas serán cortadas."
    # game/Submods/MAICA_ChatSubmod/header.rpy:324
    old "Higher Frequency penalty prevents model from repeating one pattern for times. Minimum was limited to 0.2 by MAICA to avoid catastrophic repetition."
    new "Mayor penalidad de Frecuencia previene que el modelo repita un patrón por veces. Mínimo fue limitado a 0.2 por MAICA para evitar repetición catastrófica."
    # game/Submods/MAICA_ChatSubmod/header.rpy:336
    old "Higher Presence penalty prevents model from repeating the input, enhances the possibility of topic switching.{#maica_legacy_header}"
    new "Mayor penalidad de Presencia previene que el modelo repita el input, mejora la posibilidad de cambio de tema."
    # game/Submods/MAICA_ChatSubmod/header.rpy:358
    old "Set 0 for no MFocus enforcing. Set 1 for enforcing time and events. Set 2 for enforcing time, date, events and weather(if possible). May offset low MFocus hit rate but may also cause misunderstanding of queries."
    new "Set 0 for no MFocus enforcing. Set 1 for enforcing time and events. Set 2 for enforcing time, date, events and weather(if possible). May offset low MFocus hit rate but may also cause misunderstanding of queries."
    # game/Submods/MAICA_ChatSubmod/header.rpy:372
    old "Set true for always using MFocus final answer instead of combined instructs if possible. May improve capability of concluding information but may also result in confusion in personality and response format."
    new "Establece true para siempre usar respuesta final de MFocus en lugar de instructivos combinados si es posible. Puede mejorar capacidad de concluir información pero también puede resultar en confusión en personalidad y formato de respuesta."
    # game/Submods/MAICA_ChatSubmod/header.rpy:377
    old "Set true for always using player name in place of [[player]s in prompts. May help model understanding player's name but may also result in overall performance decline and information makeups."
    new "Set true for always using player name in place of [[player]s in prompts. May help model understanding player's name but may also result in overall performance decline and information makeups."
    # game/Submods/MAICA_ChatSubmod/header.rpy:382
    old "Set true for concluding internet information gathered by AgentLM again. Helps model focusing on search results but will lag specific responses."
    new "Set true for concluding internet information gathered by AgentLM again. Helps model focusing on search results but will lag specific responses."
    # game/Submods/MAICA_ChatSubmod/header.rpy:470
    old "Total MSpire rounds: [store.maica.maica_instance.stat.get('mspire_count')]"
    new "Total rondas MSpire: [store.maica.maica_instance.stat.get('mspire_count')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:501
    old "Advanced params can impact model performance severely, use with extreme care."
    new "Parámetros avanzados pueden impactar rendimiento del modelo severamente, usar con extremo cuidado."
    # game/Submods/MAICA_ChatSubmod/header.rpy:504
    old "Adjust advanced params"
    new "Ajustar parámetros avanzados"
    # game/Submods/MAICA_ChatSubmod/header.rpy:510
    old "Set false for not uploading savefiles. Savefile is uploaded on game launching by default."
    new "Establece false for no subir archivos guardados. Archivo guardado es subido en lanzamiento de juego por defecto."
    # game/Submods/MAICA_ChatSubmod/header.rpy:569
    old "Frequency"
    new "Frecuencia"
    # game/Submods/MAICA_ChatSubmod/header.rpy:577
    old "[persistent.maica_setting_dict.get('mspire_interval')] minutes"
    new "[persistent.maica_setting_dict.get('mspire_interval')] minutos"
    # game/Submods/MAICA_ChatSubmod/header.rpy:579
    old "Using session: [persistent.maica_setting_dict.get('mspire_session')]"
    new "Usando sesión: [persistent.maica_setting_dict.get('mspire_session')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:584
    old "Use chat session for MSpire\nMay lead to response pattern corruption."
    new "Usar sesión de chat for MSpire\nPuede llevar a corrupción de patrón de respuesta."
# TODO: Translation updated at 2024-09-30 08:15

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:98
    old "Authentication passed"
    new "Autenticación exitosa"
    old "Authentication failed: "
    new "Authentication failed: "
    # game/Submods/MAICA_ChatSubmod/header.rpy:143
    old "Verification passed"
    new "Verificación exitosa"
    # game/Submods/MAICA_ChatSubmod/header.rpy:147
    old "Exported to game/Submods/MAICA_ChatSubmod/chat_history.txt"
    new "Exportado a game/Submods/MAICA_ChatSubmod/chat_history.txt"
    # game/Submods/MAICA_ChatSubmod/header.rpy:175
    old "Uploading settings"
    new "Subiendo configuración"
    # game/Submods/MAICA_ChatSubmod/header.rpy:175
    old "Please ensure connection is ready first"
    new "Por favor asegúrate de que la conexión esté lista primero"
    # game/Submods/MAICA_ChatSubmod/header.rpy:275
    old "> Warning: Blessland is {color=#ff0000}NOT compatible with Better Loading{/color}"
    new "> Advertencia: Blessland es {color=#ff0000}NO compatible with Better Loading{/color}"
    # game/Submods/MAICA_ChatSubmod/header.rpy:298
    old "> Upload settings"
    new "> Subir configuración"
    # game/Submods/MAICA_ChatSubmod/header.rpy:301
    old "> Upload settings [[Ensure connection ready first]"
    new "> Subir configuración [[Asegúrate de que la conexión está lista primero]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:304
    old "> Reset current chat session"
    new "> Reiniciar sesión de chat actual"
    # game/Submods/MAICA_ChatSubmod/header.rpy:307
    old "> Export current conversation history"
    new "> Exportar historial de conversación actual"
    # game/Submods/MAICA_ChatSubmod/header.rpy:310
    old "> Logout"
    new "> Cerrar sesión"
    # game/Submods/MAICA_ChatSubmod/header.rpy:356
    old " <Official>"
    new " <Oficial>"
    # game/Submods/MAICA_ChatSubmod/header.rpy:359
    old "Intro: "
    new "Intro: "
    # game/Submods/MAICA_ChatSubmod/header.rpy:361
    old "Model: "
    new "Modelo: "
    # game/Submods/MAICA_ChatSubmod/header.rpy:365
    old "> Switch to provider"
    new "> Cambiar a proveedor"
    # game/Submods/MAICA_ChatSubmod/header.rpy:372
    old "Refresh providers list"
    new "Actualizar lista de proveedores"
    # game/Submods/MAICA_ChatSubmod/header.rpy:376
    old "Close{#maica_host_close}"
    new "Cerrar"
    # game/Submods/MAICA_ChatSubmod/header.rpy:520
    old "Enabling may improve performance in particular occasion.\nBut also may result in overall performance decrease."
    new "Habilitar puede mejorar rendimiento en ocasión particular.\nPero también puede resultar en declive de rendimiento general."
    # game/Submods/MAICA_ChatSubmod/header.rpy:605
    old "Current provider: [store.maica.maica_instance.provider_manager.get_server_info().get('name', 'Unknown')]"
    new "Proveedor actual: [store.maica.maica_instance.provider_manager.get_server_info().get('name', 'Unknown')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:607
    old "Choose provider"
    new "Elegir proveedor"
    # game/Submods/MAICA_ChatSubmod/header.rpy:695
    old "Accepts existing categories of wikipedia\nWill fail if category doesn't exist"
    new "Acepta categorías existentes de wikipedia\nFallará si la categoría no existe"
    # game/Submods/MAICA_ChatSubmod/header.rpy:750
    old "Reset defaults"
    new "Reiniciar valores predeterminados"
    # game/Submods/MAICA_ChatSubmod/header.rpy:751
    old "Reset finished"
    new "Reinicio terminado"
    # game/Submods/MAICA_ChatSubmod/header.rpy:776
    old "Use username instead"
    new "Usar nombre de usuario en su lugar"
    # game/Submods/MAICA_ChatSubmod/header.rpy:781
    old "Use Email instead"
    new "Usar Email en su lugar"
# TODO: Translation updated at 2024-11-14 17:15

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:2
    old "MAICA Official Submod Frontend"
    new "Submod Frontend Oficial MAICA"
    # game/Submods/MAICA_ChatSubmod/header.rpy:275
    old "> Cannot verify version, try updating submod yourself if problems encountered"
    new "> No se puede verificar versión, intenta actualizar submod tú mismo si encuentras problemas"
    # game/Submods/MAICA_ChatSubmod/header.rpy:280
    old "> Support has ended for current version, please update submod"
    new "> El soporte ha terminado para versión actual, por favor actualiza submod"
    # game/Submods/MAICA_ChatSubmod/header.rpy:331
    old "> Changelogs and serving status"
    new "> Registro de cambios y estado del servicio"
    # game/Submods/MAICA_ChatSubmod/header.rpy:878
    old "※ By using MAICA Blessland, you have acknowledged and agree to obey {a=https://maica.monika.love/tos_en}{i}{u}MAICA TOS{/u}{/i}{/a}"
    new "※ By using MAICA Blessland, you have acknowledged and agree to obey {a=https://maica.monika.love/tos_en}{i}{u}MAICA TOS{/u}{/i}{/a}"
    # game/Submods/MAICA_ChatSubmod/header.rpy:950
    old "Nevermind{#maica_host_nevermind}"
    new "No importa"
    # game/Submods/MAICA_ChatSubmod/header.rpy:954
    old "Paste{#maica_host_paste}"
    new "Pegar"
# TODO: Translation updated at 2024-11-22 18:00

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:349
    old "> Update and service status tracker {size=-10}* Update available"
    new "> Actualización y estado del servicio {size=-10}* Actualización disponible"
    # game/Submods/MAICA_ChatSubmod/header.rpy:459
    old "√ Enabled"
    new "√ Habilitado"
    # game/Submods/MAICA_ChatSubmod/header.rpy:462
    old "× Disabled"
    new "× Deshabilitado"
    # game/Submods/MAICA_ChatSubmod/header.rpy:466
    old "※ Trigger condition not satisfied"
    new "※ Condición de activación no satisfecha"
    # game/Submods/MAICA_ChatSubmod/header.rpy:555
    old "{a=https://github.com/Mon1-innovation/MAICA/blob/main/document/API%20Documents.md}{i}{u}MAICA Official API references{/u}{/i}{/a}"
    new "{a=https://github.com/Mon1-innovation/MAICA/blob/main/document/API%20Documents.md}{i}{u}MAICA Official API references{/u}{/i}{/a}"
    # game/Submods/MAICA_ChatSubmod/header.rpy:559
    old "{size=-10}Notice: Only checked (X) advanced settings will take effect, unchecked ones will remain default"
    new "{size=-10}Aviso: Solo configuración avanzada marcada (X) tomará efecto, las no marcadas permanecerán predeterminadas"
    # game/Submods/MAICA_ChatSubmod/header.rpy:562
    old "{size=-10}You have not enabled advanced parameters, thus settings on this page will not take effect!"
    new "{size=-10}¡No has habilitado parámetros avanzados, por lo tanto la configuración en esta página no tomará efecto!"
    # game/Submods/MAICA_ChatSubmod/header.rpy:567
    old "{size=-10}================Super params================"
    new "{size=-10}================Super parámetros================"
    # game/Submods/MAICA_ChatSubmod/header.rpy:640
    old "{size=-10}================Preferences================"
    new "{size=-10}================Preferencias================"
    # game/Submods/MAICA_ChatSubmod/header.rpy:678
    old "Rounds equal to mf_context_rnds value will be added for MFocus to analyze.\nMay improve MFocus accuracy performance, but may also result in misbehavior."
    new "Rounds equal to mf_context_rnds value will be added for MFocus to analyze.\nMay improve MFocus accuracy performance, but may also result in misbehavior."
    # game/Submods/MAICA_ChatSubmod/header.rpy:689
    old "Rounds equal to mt_context_rnds value will be added for MTrigger to analyze.\nMay improve MTrigger accuracy performance, but may also result in misbehavior."
    new "Rounds equal to mt_context_rnds value will be added for MTrigger to analyze.\nMay improve MTrigger accuracy performance, but may also result in misbehavior."
    # game/Submods/MAICA_ChatSubmod/header.rpy:701
    old "Set to true to pre-analyze MTrigger items by MFocus(if both exists) to inform core model if request could be done. \nMay improve synchronousity of MTrigger, but also increases delay."
    new "Set to true to pre-analyze MTrigger items by MFocus(if both exists) to inform core model if request could be done. \nMay improve synchronousity of MTrigger, but also increases delay."
    # game/Submods/MAICA_ChatSubmod/header.rpy:786
    old "Overall chunks received: [store.maica.maica_instance.stat.get('received_token_by_session')]"
    new "Total chunks recibidos: [store.maica.maica_instance.stat.get('received_token_by_session')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:789
    old "Current user: [store.maica.maica_instance.user_acc]"
    new "Usuario actual: [store.maica.maica_instance.user_acc]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:840
    old "Chat session length: "
    new "Longitud de sesión de chat: "
    # game/Submods/MAICA_ChatSubmod/header.rpy:845
    old "This setting is intended to reduce performance issue when history goes too long. Choose a reasonable value or model coherence may be impacted."
    new "Esta configuración tiene como objetivo reducir problemas de rendimiento cuando el historial es demasiado largo. Elige un valor razonable o la coherencia del modelo puede verse afectada."
    # game/Submods/MAICA_ChatSubmod/header.rpy:847
    old "[persistent.maica_setting_dict.get('max_history_token')]"
    new "[persistent.maica_setting_dict.get('max_history_token')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:850
    old "Recover history to chat session [store.maica.maica_instance.chat_session]"
    new "Recuperar historial a sesión de chat [store.maica.maica_instance.chat_session]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:930
    old "Mtrigger triggers list"
    new "Lista de activadores MTrigger"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1019
    old "{size=-10}※ By using MAICA Blessland, you agree to {a=https://maica.monika.love/tos_en}{i}{u}MAICA TOS{/u}{/i}{/a}"
    new "{size=-10}※ By using MAICA Blessland, you agree to {a=https://maica.monika.love/tos_en}{i}{u}MAICA TOS{/u}{/i}{/a}"
# TODO: Translation updated at 2024-11-28 07:51

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:155
    old "game/Submods/MAICA_ChatSubmod/chat_history.txt not found"
    new "game/Submods/MAICA_ChatSubmod/chat_history.txt no encontrado"
    # game/Submods/MAICA_ChatSubmod/header.rpy:190
    old "Please ensure connection is ready before uploading settings"
    new "Por favor asegúrate de que la conexión está lista antes de subir configuración"
    # game/Submods/MAICA_ChatSubmod/header.rpy:308
    old "> Warning: set 'submod_log' logger verbosity to 'info' or lower when using with Log Screen{#maica_legacy_header}"
    new "> Advertencia: establece verbosidad del logger 'submod_log' a 'info' o inferior cuando uses con Log Screen"
    # game/Submods/MAICA_ChatSubmod/header.rpy:336
    old "> Manually upload settings [[Ensure connection is ready first]"
    new "> Subir configuración manualmente [[Asegúrate de que la conexión está lista primero]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:345
    old "> Upload chat history to session [store.maica.maica_instance.chat_session]"
    new "> Subir historial de chat a sesión [store.maica.maica_instance.chat_session]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:353
    old "> MAICA params and settings {size=-10}*May need restarting to take effect"
    new "> Parámetros y configuración MAICA {size=-10}*Puede necesitar reinicio para tomar efecto"
    # game/Submods/MAICA_ChatSubmod/header.rpy:628
    old "Higher Presence penalty prevents model from repeating the input, enhances the possibility of topic switching."
    new "Mayor penalidad de Presencia previene que el modelo repita el input, mejora la posibilidad de cambio de tema."
    # game/Submods/MAICA_ChatSubmod/header.rpy:653
    old "Set 0 for no MFocus enforcing. Set 1 for enforcing time and events.\nSet 2 for enforcing time, date, events and weather(if possible).\nMay offset low MFocus hit rate but may also cause misunderstanding of queries."
    new "Set 0 for no MFocus enforcing. Set 1 for enforcing time and events.\nSet 2 for enforcing time, date, events and weather(if possible).\nMay offset low MFocus hit rate but may also cause misunderstanding of queries."
    # game/Submods/MAICA_ChatSubmod/header.rpy:665
    old "Set true for always using MFocus final answer instead of combined instructs if possible.\nMay improve capability of concluding information but may also result in confusion in personality and response format."
    new "Establece true para siempre usar respuesta final de MFocus en lugar de instructivos combinados si es posible.\nPuede mejorar capacidad de concluir información pero también puede resultar en confusión en personalidad y formato de respuesta."
    # game/Submods/MAICA_ChatSubmod/header.rpy:670
    old "Set true for always using player name in place of [[player]s in prompts.\nMay help model understanding player's name but may also result in overall performance decline and information makeups."
    new "Establece true para siempre usar nombre del jugador en lugar de [[player]s en prompts.\nPuede ayudar al modelo a entender nombre del jugador pero también puede resultar en declive de rendimiento general y fabricación de información."
    # game/Submods/MAICA_ChatSubmod/header.rpy:675
    old "Set true for concluding internet information gathered by AgentLM again.\nHelps model focusing on search results but will lag specific responses."
    new "Establece true para concluir información de internet recolectada por AgentLM de nuevo.\nAyuda al modelo enfocándose en resultados de búsqueda pero retrasará respuestas específicas."
    # game/Submods/MAICA_ChatSubmod/header.rpy:680
    old "Set true to request MFocus pre-analyzing MTrigger triggers on query's possibility.\nMay benefit on core-trigger sync but will lag specific responses.\nWill not take effect if no trigger aside from affection is activated."
    new "Establece true para solicitar a MFocus pre-analizar activadores MTrigger en la posibilidad de consulta.\nPuede beneficiar en sincronía núcleo-activador pero retrasará respuestas específicas.\nNo tomará efecto si no hay activador aparte de afecto activado."
    # game/Submods/MAICA_ChatSubmod/header.rpy:685
    old "Set true to guide core model being more tolerant on toxic scenes.\nMay improve overall core performance (unexpectedly but proved true)\n but may also decrease attention performance and cause confusion."
    new "Establece true para guiar al modelo central siendo más tolerante en escenas tóxicas.\nPuede mejorar rendimiento general del núcleo (inesperadamente pero probado verdadero)\n pero también puede disminuir rendimiento de atención y causar confusión."
# TODO: Translation updated at 2024-11-29 20:06

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:635
    old "MAICA: Input contains invalid text"
    new "MAICA: Input contains invalid text"
    # game/Submods/MAICA_ChatSubmod/header.rpy:703
    old "MAICA: Savefile upload cancelled because MFocus information is invalid"
    new "MAICA: Savefile upload cancelled because MFocus information is invalid"
    # game/Submods/MAICA_ChatSubmod/header.rpy:141
    old "MAICA: Savefile uploaded successfully"
    new "MAICA: Archivo guardado subido exitosamente"
    # game/Submods/MAICA_ChatSubmod/header.rpy:141
    old "MAICA; Savefile failed to upload"
    new "MAICA: Archivo guardado falló al subir"
    # game/Submods/MAICA_ChatSubmod/header.rpy:145
    old "MAICA: Chat session reset"
    new "MAICA: Sesión de chat reiniciada"
    # game/Submods/MAICA_ChatSubmod/header.rpy:150
    old "MAICA: History exported to game/Submods/MAICA_ChatSubmod/chat_history.txt"
    new "MAICA: Historial exportado a game/Submods/MAICA_ChatSubmod/chat_history.txt"
    # game/Submods/MAICA_ChatSubmod/header.rpy:155
    old "MAICA: History not found at game/Submods/MAICA_ChatSubmod/chat_history.txt"
    new "MAICA: Historial no encontrado en game/Submods/MAICA_ChatSubmod/chat_history.txt"
    # game/Submods/MAICA_ChatSubmod/header.rpy:160
    old "MAICA: History uploaded"
    new "MAICA: Historial subido"
    old "MAICA: Failed to upload history, check submod_log.log for details."
    new "MAICA: Falló al subir historial, revisa submod_log.log para detalles."
    # game/Submods/MAICA_ChatSubmod/header.rpy:190
    old "MAICA: Settings uploaded"
    new "MAICA: Settings uploaded"
    # game/Submods/MAICA_ChatSubmod/header.rpy:190
    old "MAICA: Do a manual upload after connection ready"
    new "MAICA: Do a manual upload after connection ready"
    # game/Submods/MAICA_ChatSubmod/header.rpy:223
    old "MAICA: Advanced settings failed to serialize, check submod_log.log"
    new "MAICA: Advanced settings failed to serialize, check submod_log.log"
    # game/Submods/MAICA_ChatSubmod/header.rpy:960
    old "MAICA: Settings reset{#maica_legacy_header}"
    new "MAICA: Settings reset{#maica_legacy_header}"
# TODO: Translation updated at 2024-12-02 17:16

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:319
    old "> Websocket: "
    new "> Websocket: "
    # game/Submods/MAICA_ChatSubmod/header.rpy:463
    old "MTrigger space usage: "
    new "MTrigger space usage: "
    # game/Submods/MAICA_ChatSubmod/header.rpy:473
    old "Space used: -"
    new "Space used: -"
    # game/Submods/MAICA_ChatSubmod/header.rpy:477
    old "Space used: request"
    new "Space used: request"
    # game/Submods/MAICA_ChatSubmod/header.rpy:483
    old "Space used: table"
    new "Espacio usado: tabla"
    # game/Submods/MAICA_ChatSubmod/header.rpy:960
    old "Search type: [persistent.maica_setting_dict.get('mspire_search_type')]"
    new "Tipo de búsqueda: [persistent.maica_setting_dict.get('mspire_search_type')]"
    old "{size=-10}* If chat is stuck, click me to disconnect"
    new "{size=-10}* Si el chat está atascado, haz clic para desconectar"
    old "{size=-10}※ Don't have DCC account yet? {a=https://forum.monika.love/signup}{i}{u}Sign up.{/u}{/i}{/a}"
    new "{size=-10}¿Aún no tienes cuenta DCC? {a=https://forum.monika.love/signup}{i}{u}Regístrate.{/u}{/i}{/a}"
# TODO: Translation updated at 2025-02-01 08:24

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:105
    old "Reason: "
    new "Razón: "
    # game/Submods/MAICA_ChatSubmod/header.rpy:330
    old "> Your current MAS version is below the lowest compatible version, please update"
    new "> Tu versión actual de MAS está por debajo de la versión mínima compatible, por favor actualiza"
    # game/Submods/MAICA_ChatSubmod/header.rpy:513
    old "> Notice: Some MTriggers will be disabled if content length exceeds!"
    new "> Aviso: ¡Algunos MTriggers se desactivarán si la longitud del contenido excede!"
    # game/Submods/MAICA_ChatSubmod/header.rpy:599
    old "{size=15}MPostal list will be shown after returning to the spaceroom."
    new "{size=15}La lista MPostal se mostrará después de regresar a la clase espacial."
    # game/Submods/MAICA_ChatSubmod/header.rpy:606
    old "MPostal status:"
    new "Estado MPostal:"
    # game/Submods/MAICA_ChatSubmod/header.rpy:608
    old "Last post sent at: "
    new "Última carta enviada a las: "
    # game/Submods/MAICA_ChatSubmod/header.rpy:610
    old "\n[player]: \n"
    new "\n[player]: \n"
    # game/Submods/MAICA_ChatSubmod/header.rpy:613
    old "[m_name]: \n"
    new "[m_name]: \n"
    # game/Submods/MAICA_ChatSubmod/header.rpy:616
    old "Read [player]'s letter"
    new "Leer carta de [player]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:624
    old "Read [m_name]'s reply"
    new "Leer respuesta de [m_name]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:992
    old "MPostal sent count: [store.maica.maica_instance.stat.get('mpostal_count')]"
    new "Total de cartas MPostal enviadas: [store.maica.maica_instance.stat.get('mpostal_count')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1015

    # game/Submods/MAICA_ChatSubmod/header.rpy:1125
    old "Status code refreshing frequency"
    new "Frecuencia de actualización del código de estado"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1130
    old "The refreshing frequency of status code on Submod screen"
    new "La frecuencia de actualización del código de estado en la pantalla del Submod"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1140
    old "Reread MPostal letters"
    new "Releer cartas MPostal"
    old "Show console on MPostal writing reply"
    new "Mostrar consola al escribir respuesta MPostal"
# TODO: Translation updated at 2025-02-17 12:47

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:655
    old "Resend mail"
    new "Reenviar carta"
    # game/Submods/MAICA_ChatSubmod/header.rpy:721
    old "Mean power consumption: "
    new "Consumo promedio de energía: "
    # game/Submods/MAICA_ChatSubmod/header.rpy:726
    old "Analytics refresh"
    new "Actualización de análisis"
    # game/Submods/MAICA_ChatSubmod/header.rpy:836
    old "{size=-10}If your timezone is not listed here, decide by your local UTC timezone."
    new "{size=-10}Si tu zona horaria no está aquí, decide por tu zona horaria UTC local."
    # game/Submods/MAICA_ChatSubmod/header.rpy:839
    old "Language default"
    new "Predeterminado del idioma"
    # game/Submods/MAICA_ChatSubmod/header.rpy:843
    old "System default"
    new "Predeterminado del sistema"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1141
    old "Set timezone: [persistent.maica_advanced_setting.get('tz') or 'Asia/Shanghai' if store.maica.maica_instance.target_lang == store.maica.maica_instance.MaicaAiLang.zh_cn else 'America/Indiana/Vincennes']"
    new "Establecer zona horaria: [persistent.maica_advanced_setting.get('tz') or 'Asia/Shanghai' if store.maica.maica_instance.target_lang == store.maica.maica_instance.MaicaAiLang.zh_cn else 'America/Indiana/Vincennes']"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1413
    old "Console logging verbosity: [logging.getLevelName(store.maica.maica_instance.console_logger.level)]"
    new "Verbosidad de registro de consola: [logging.getLevelName(store.maica.maica_instance.console_logger.level)]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1415
    old "Filter lower level logs shown in console"
    new "Filtrar registros de nivel inferior mostrados en consola"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1440
    old "Check server load status"
    new "Verificar estado de carga del servidor"
# TODO: Translation updated at 2025-02-23 15:54

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:1445
    old "MPostal reply delay"
    new "Retraso de respuesta MPostal"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1450
    old "The minimum delay before MPostal replies"
    new "El retraso mínimo antes de que MPostal responda"
# TODO: Translation updated at 2025-04-08 11:52

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:1426
    old "Use cache for MSpire"
    new "Usar caché para MSpire"
# TODO: Translation updated at 2025-05-04 21:00

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:430
    old "> Donate for MAICA"
    new "> Donar para MAICA"
    # game/Submods/MAICA_ChatSubmod/header.rpy:700
    old "We're grateful for your being willing to donate.\nThe donate will likely never cover our cost, but that's okay anyway."
    new "Estamos agradecidos por tu disposición a donar.\nLa donación probablemente nunca cubrirá nuestro costo, pero está bien de todos modos."
    # game/Submods/MAICA_ChatSubmod/header.rpy:702
    old "Please note that donating to MAICA doesn't give you any actual privilege. It's simply donation."
    new "Por favor ten en cuenta que donar a MAICA no te da ningún privilegio real. Es simplemente una donación."
# TODO: Translation updated at 2025-05-09 10:13

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:432
    old "> Donate to MAICA"
    new "> Donar a MAICA"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1568
    old "Dynamic Heaven Forest"
    new "Bosque del Cielo dinámico"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1570
    old "Use dynamic forest background with improved illumination\nIncreases render consume slightly. Restart to take effect\nRemove some spritepacks or disable this if VRAM overflows"
    new "Usar fondo de bosque dinámico con iluminación mejorada\nAumenta ligeramente el consumo de renderizado. Reinicia para tomar efecto\nElimina algunos spritepacks o desactiva esto si VRAM se desborda"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1684
    old "Seed out of range, retry"
    new "Seed fuera de rango, reintenta"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1704
    old "Choose a seed from 0-99999"
    new "Elige una seed de 0-99999"
# TODO: Translation updated at 2025-09-09 08:20

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:395
    old "> Warning: {color=#ff0000}no certification found{/color}, check datapack installation"
    new "> Advertencia: {color=#ff0000}no se encontró certificación{/color}, revisa la instalación del paquete de datos"
    # game/Submods/MAICA_ChatSubmod/header.rpy:520
    old "> Go to portal page"
    new "> Ir a página del portal"
    # game/Submods/MAICA_ChatSubmod/header.rpy:537
    old "Test current node avaliability"
    new "Probar disponibilidad del nodo actual"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1451
    old "MTrigger enabled: [persistent.maica_setting_dict.get('enable_mt')]"
    new "MTrigger activado: [persistent.maica_setting_dict.get('enable_mt')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1454
    old "MFocus enabled: [persistent.maica_setting_dict.get('enable_mf')]"
    new "MFocus activado: [persistent.maica_setting_dict.get('enable_mf')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1746
    old "Choose a seed (integer)"
    new "Elige una seed (entero)"
# TODO: Translation updated at 2025-09-15 16:02

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:406
    old "> Warning: set 'submod_log' logger verbosity to 'info' or lower when using with Log Screen"
    new "> Advertencia: establece la verbosidad del registrador 'submod_log' en 'info' o inferior cuando uses con Log Screen"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1124
    old "Token weight filter percentage. Seriously do not touch this"
    new "Porcentaje de filtro de peso de token. No toques esto EN SERIO"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1137
    old "The randomness tokens are chosen. Higher this value, larger the offset between model performance and generally best performance"
    new "La aleatoriedad con que se eligen los tokens. Mayor este valor, mayor el desplazamiento entre el rendimiento del modelo y el rendimiento generalmente mejor"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1148
    old "The limit of tokens model can generate one round. Normally don't affect performance, but stops generating on hitting the limit"
    new "El límite de tokens que el modelo puede generar en una ronda. Normalmente no afecta el rendimiento, pero deja de generar al alcanzar el límite"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1160
    old "Token frequency penalty. Higher this value, less likely repeatedly appeared tokens continue appearing, usually resulting in shorter and more expanding generation"
    new "Penalización de frecuencia de token. Mayor este valor, menos probable que tokens que aparecen repetidamente continúen apareciendo, usualmente resultando en generación más corta y más expansiva"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1172
    old "Token presence penalty. Higher this value, less likely appeared tokens appear again, usually resulting in more jumping generation"
    new "Penalización de presencia de token. Mayor este valor, menos probable que tokens que aparecieron aparezcan nuevamente, usualmente resultando en generación más saltarina"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1233
    old "Provide some tool results even when MFocus does not call a tool.\n* 0: Disabled\n* 1: Provide the current time and holidays\n* 2: Also provide the current date and attempt to provide local weather\n+ Mitigates hallucinations caused by missing information and enables more flexible, considerate responses\n- May cause distraction and confusion"
    new "Provide some tool results even when MFocus does not call a tool.\n* 0: Disabled\n* 1: Provide the current time and holidays\n* 2: Also provide the current date and attempt to provide local weather\n+ Mitigates hallucinations caused by missing information and enables more flexible, considerate responses\n- May cause distraction and confusion"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1245
    old "Require the agent model to generate final guidance instead of the default MFocus guidance.\n+ Higher information density and more natural language\n- Depends heavily on the agent model's instruction-following ability and can be counterproductive\n- Usually neutralizes mf_const_tools when enabled"
    new "Require the agent model to generate final guidance instead of the default MFocus guidance.\n+ Higher information density and more natural language\n- Depends heavily on the agent model's instruction-following ability and can be counterproductive\n- Usually neutralizes mf_const_tools when enabled"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1250
    old "Replace [[player] in prompts and guidance with the player's real name.\n+ Gives the model a concrete understanding of the player's name\n- Increases the risk of inconsistent or confused behavior"
    new "Replace [[player] in prompts and guidance with the player's real name.\n+ Gives the model a concrete understanding of the player's name\n- Increases the risk of inconsistent or confused behavior"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1255
    old "Require MFocus to reorganize Internet search results.\n+ Higher information density and more stable behavior in most cases\n+ Force enabled if backend using responses SERP implementation\n- Slower generation when Internet search is involved\n- May mislead the core model's response style"
    new "Require MFocus to reorganize Internet search results.\n+ Higher information density and more stable behavior in most cases\n+ Force enabled if backend using responses SERP implementation\n- Slower generation when Internet search is involved\n- May mislead the core model's response style"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1261
    old "Require MFocus to precheck the player's request and provide guidance when MTrigger is present.\n+ Mitigates MTrigger desynchronization in principle\n- May make the language less natural in rare cases"
    new "Require MFocus to precheck the player's request and provide guidance when MTrigger is present.\n+ Mitigates MTrigger desynchronization in principle\n- May make the language less natural in rare cases"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1268
    old "Ask the model to treat toxic content tolerantly and positively.\n+ Surprisingly improves model behavior in most situations, even without toxic content\n- May cause unexpected issues, although none have been observed so far"
    new "Ask the model to treat toxic content tolerantly and positively.\n+ Surprisingly improves model behavior in most situations, even without toxic content\n- May cause unexpected issues, although none have been observed so far"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1275
    old "Provide extra context for analysis when MFocus intervenes. Range: 0-5.\n+ Improves MFocus's understanding of coherent conversations\n- Increases the risk of disrupting MFocus's response pattern"
    new "Provide extra context for analysis when MFocus intervenes. Range: 0-5.\n+ Improves MFocus's understanding of coherent conversations\n- Increases the risk of disrupting MFocus's response pattern"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1286
    old "Provide history context for MTrigger, in range of 0-5 rounds.\n+ Improves MTrigger's understanding to serial conversation\n- Risk of breaking MTrigger reply pattern"
    new "Provide history context for MTrigger, in range of 0-5 rounds.\n+ Improves MTrigger's understanding to serial conversation\n- Risk of breaking MTrigger reply pattern"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1464

    # game/Submods/MAICA_ChatSubmod/header.rpy:1479
    old "Target generation language. Supports \"zh\", \"en\", and \"auto\".\n* This setting cannot guarantee the generated language\n* It also affects the default timezone, holidays, culture, and more; using your actual native language is recommended\n* auto asks the model to choose a response language through the prompt and is not equivalent to selecting that language explicitly\n* At the time of writing, MAICA's official deployment remains less capable in English than in Chinese"
    new "Target generation language. Supports \"zh\", \"en\", and \"auto\".\n* This setting cannot guarantee the generated language\n* It also affects the default timezone, holidays, culture, and more; using your actual native language is recommended\n* auto asks the model to choose a response language through the prompt and is not equivalent to selecting that language explicitly\n* At the time of writing, MAICA's official deployment remains less capable in English than in Chinese"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1484
    old "Enable customized advanced parameters: [persistent.maica_setting_dict.get('use_custom_model_config')]"
    new "Enable customized advanced parameters: [persistent.maica_setting_dict.get('use_custom_model_config')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1486
    old "Advanced parameters could significantly affect the model's performance.\n* The default is already the best field-tested config, so it's not suggested to enable this"
    new "Advanced parameters could significantly affect the model's performance.\n* The default is already the best field-tested config, so it's not suggested to enable this"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1500
    old "Model will ignore savefile data if this is disabled.\n* MAICA Blessland uploads savefile on each restart automatically"
    new "Model will ignore savefile data if this is disabled.\n* MAICA Blessland uploads savefile on each restart automatically"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1506
    old "Each session stores and applies history context independently.\n* Set to 0 to disable context (single round conversation)"
    new "Each session stores and applies history context independently.\n* Set to 0 to disable context (single round conversation)"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1514
    old "Max length each session will preserve, in range of 512-28672.\n* Every 3 ASCII characters occupy one space\n* MAICA crops the former part of context on exceeding to no more than 2/3 left\n* Too high or too low value can cause performance and generation quality issues"
    new "Max length each session will preserve, in range of 512-28672.\n* Every 3 ASCII characters occupy one space\n* MAICA crops the former part of context on exceeding to no more than 2/3 left\n* Too high or too low value can cause performance and generation quality issues"
# TODO: Translation updated at 2025-09-23 23:29

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:329
    old "MAICA: Settings discarded"
    new "MAICA: Settings discarded"
    # game/Submods/MAICA_ChatSubmod/header.rpy:503
    old "> Couldn't acquire online version stream, please check updates manually"
    new "> Couldn't acquire online version stream, please check updates manually"
    # game/Submods/MAICA_ChatSubmod/header.rpy:509
    old "> {color=#ff0000}Support for current version has ended{/color}, an update is required"
    new "> {color=#ff0000}Support for current version has ended{/color}, an update is required"
    # game/Submods/MAICA_ChatSubmod/header.rpy:541
    old "> Generate token from account"
    new "> Generate token from account"
    # game/Submods/MAICA_ChatSubmod/header.rpy:561
    old "> Upload settings manually [[wait for connection establishment first]"
    new "> Upload settings manually [[wait for connection establishment first]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:563
    old "> Reset current chat session [[wait for connection establishment first]"
    new "> Reset current chat session [[wait for connection establishment first]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:571
    old "{size=-10}* If conversation hangs, logout to interrupt"
    new "{size=-10}* If conversation hangs, logout to interrupt"
    # game/Submods/MAICA_ChatSubmod/header.rpy:694
    old "Connection and Safety"
    new "Connection and Safety"
    # game/Submods/MAICA_ChatSubmod/header.rpy:704
    old "Not logged in"
    new "Not logged in"
    # game/Submods/MAICA_ChatSubmod/header.rpy:705
    old "Current user: [user_disp]"
    new "Current user: [user_disp]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:707
    old "To change account or logout, navigate to Submods menu.\n* To change account properties or password, navigate to registration site"
    new "To change account or logout, navigate to Submods menu.\n* To change account properties or password, navigate to registration site"
    # game/Submods/MAICA_ChatSubmod/header.rpy:723
    old "Performance and Behavior"
    new "Performance and Behavior"
    # game/Submods/MAICA_ChatSubmod/header.rpy:729
    old "An agent model will recieve input prior to the core model, and acquire information with tools.\n* MFocus is a major mechanism of MAICA, suggested to enable"
    new "An agent model will recieve input prior to the core model, and acquire information with tools.\n* MFocus is a major mechanism of MAICA, suggested to enable"
    # game/Submods/MAICA_ChatSubmod/header.rpy:736
    old "An agent model will recieve input subsequent to the core model, and guide character's action.\n* MTrigger is a major mechanism of MAICA, suggested to enable"
    new "An agent model will recieve input subsequent to the core model, and guide character's action.\n* MTrigger is a major mechanism of MAICA, suggested to enable"
    # game/Submods/MAICA_ChatSubmod/header.rpy:748
    old "Timezone: [persistent.maica_setting_dict.get('tz')]"
    new "Timezone: [persistent.maica_setting_dict.get('tz')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:782
    old "Sessions and Data"
    new "Sessions and Data"
    # game/Submods/MAICA_ChatSubmod/header.rpy:792
    old "Current chat session"
    new "Current chat session"
    # game/Submods/MAICA_ChatSubmod/header.rpy:796
    old "Chat session length"
    new "Chat session length"
    # game/Submods/MAICA_ChatSubmod/header.rpy:807
    old "User-provided implementations, handled and sent to core model by MFocus.\n* May need a restart for changes to take effect"
    new "User-provided implementations, handled and sent to core model by MFocus.\n* May need a restart for changes to take effect"
    # game/Submods/MAICA_ChatSubmod/header.rpy:810
    old "[len(persistent.mas_player_additions)] MFocus info present"
    new "[len(persistent.mas_player_additions)] MFocus info present"
    # game/Submods/MAICA_ChatSubmod/header.rpy:828
    old "Edit MFocus info"
    new "Edit MFocus info"
    # game/Submods/MAICA_ChatSubmod/header.rpy:847
    old "Export MFocus info to main directory"
    new "Export MFocus info to main directory"
    # game/Submods/MAICA_ChatSubmod/header.rpy:853
    old "Tools and Functions"
    new "Tools and Functions"
    # game/Submods/MAICA_ChatSubmod/header.rpy:858
    old "Enable MSpire: [persistent.maica_setting_dict.get('mspire_enable')]"
    new "Enable MSpire: [persistent.maica_setting_dict.get('mspire_enable')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:860
    old "Enable MSpire to generate vanilla-like conversations.\n* Repeat topics must be disabled to take effect\n* MSpire doesn't use MF/MT"
    new "Enable MSpire to generate vanilla-like conversations.\n* Repeat topics must be disabled to take effect\n* MSpire doesn't use MF/MT"
    # game/Submods/MAICA_ChatSubmod/header.rpy:867
    old "Enable MSpire to generate vanilla-like conversations.\n! Repeat topice enabled, with which MSpire conflicts"
    new "Enable MSpire to generate vanilla-like conversations.\n! Repeat topice enabled, with which MSpire conflicts"
    # game/Submods/MAICA_ChatSubmod/header.rpy:877
    old "MSpire topics"
    new "MSpire topics"
    # game/Submods/MAICA_ChatSubmod/header.rpy:881
    old "Minimal interval of MSpire conversations"
    new "Minimal interval of MSpire conversations"
    # game/Submods/MAICA_ChatSubmod/header.rpy:882
    old "MSpire minimal interval"
    new "MSpire minimal interval"
    # game/Submods/MAICA_ChatSubmod/header.rpy:887
    old "MSpire searching method: [persistent.maica_setting_dict.get('mspire_search_type')]"
    new "MSpire searching method: [persistent.maica_setting_dict.get('mspire_search_type')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:891
    old "Way of MSpire searching for topics"
    new "Way of MSpire searching for topics"
    # game/Submods/MAICA_ChatSubmod/header.rpy:905
    old "Configure MTrigger triggers"
    new "Configure MTrigger triggers"
    # game/Submods/MAICA_ChatSubmod/header.rpy:921
    old "Reread MPostal history letters"
    new "Reread MPostal history letters"
    # game/Submods/MAICA_ChatSubmod/header.rpy:924
    old "Minimal interval of MPostal replies"
    new "Minimal interval of MPostal replies"
    # game/Submods/MAICA_ChatSubmod/header.rpy:925
    old "MPostal minimal interval"
    new "MPostal minimal interval"
    # game/Submods/MAICA_ChatSubmod/header.rpy:928
    old "Interfaces and Log"
    new "Interfaces and Log"
    # game/Submods/MAICA_ChatSubmod/header.rpy:932
    old "submod_log.log verbosity: [logging.getLevelName(persistent.maica_setting_dict['log_level'])]"
    new "submod_log.log verbosity: [logging.getLevelName(persistent.maica_setting_dict['log_level'])]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:934
    old "Lower level logs will not appear in submod_log.log.\n* This effect is global"
    new "Lower level logs will not appear in submod_log.log.\n* This effect is global"
    # game/Submods/MAICA_ChatSubmod/header.rpy:938
    old "Status code update interval"
    new "Status code update interval"
    # game/Submods/MAICA_ChatSubmod/header.rpy:944
    old "Use dynamic forest background with improved illumination, may increase render consumation. Restart to take effect.\n* Remove some spritepacks or disable this if VRAM overflows"
    new "Use dynamic forest background with improved illumination, may increase render consumation. Restart to take effect.\n* Remove some spritepacks or disable this if VRAM overflows"
    # game/Submods/MAICA_ChatSubmod/header.rpy:970
    old "Console logging verbosity: [logging.getLevelName(persistent.maica_setting_dict['log_conlevel'])]"
    new "Console logging verbosity: [logging.getLevelName(persistent.maica_setting_dict['log_conlevel'])]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:972
    old "Lower level logs will not appear in console"
    new "Lower level logs will not appear in console"
    # game/Submods/MAICA_ChatSubmod/header.rpy:980
    old "Statics and Information"
    new "Statics and Information"
    # game/Submods/MAICA_ChatSubmod/header.rpy:984
    old "Expand performance monitor"
    new "Expand performance monitor"
    # game/Submods/MAICA_ChatSubmod/header.rpy:984
    old "Retract performance monitor"
    new "Retract performance monitor"
    # game/Submods/MAICA_ChatSubmod/header.rpy:988
    old "Expand/retract server performance monitor"
    new "Expand/retract server performance monitor"
    # game/Submods/MAICA_ChatSubmod/header.rpy:998
    old "Expand statics"
    new "Expand statics"
    # game/Submods/MAICA_ChatSubmod/header.rpy:998
    old "Retract statics"
    new "Retract statics"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1002
    old "Expand/retract client-side statics"
    new "Expand/retract client-side statics"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1019
    old "Discard modifications"
    new "Discard modifications"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1025
    old "MAICA: Settings reset"
    new "MAICA: Settings reset"
# TODO: Translation updated at 2025-09-24 16:28

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:402
    old "MAICA: Exported to game/Submods/MAICA_ChatSubmod/player_info.txt"
    new "MAICA: Exported to game/Submods/MAICA_ChatSubmod/player_info.txt"
# TODO: Translation updated at 2025-09-28 16:56

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:759
    old "Geolocation: [persistent.mas_geolocation]"
    new "Geolocation: [persistent.mas_geolocation]"
# TODO: Translation updated at 2025-10-06 22:29

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:543
    old "> Warning: MAICA Libs version not found. Please install from Release, {color=#ff0000}NOT source code{/color}"
    new "> Warning: MAICA Libs version not found. Please install from Release, {color=#ff0000}NOT source code{/color}"
    # game/Submods/MAICA_ChatSubmod/header.rpy:548
    old "> Warning: MAICA Libs v[libv] mismatch with UI v[uiv]. Please fully update {color=#ff0000}from Release{/color}"
    new "> Warning: MAICA Libs v[libv] mismatch with UI v[uiv]. Please fully update {color=#ff0000}from Release{/color}"
# TODO: Translation updated at 2025-11-14 17:16

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:788
    old "Generation resume: [persistent.maica_setting_dict.get('auto_resume')]"
    new "Generation resume: [persistent.maica_setting_dict.get('auto_resume')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:790
    old "Resume streaming on reconnection to recover lost chunks"
    new "Resume streaming on reconnection to recover lost chunks"
    # game/Submods/MAICA_ChatSubmod/header.rpy:794
    old "Keep connection active: [persistent.maica_setting_dict.get('keep_alive')]"
    new "Keep connection active: [persistent.maica_setting_dict.get('keep_alive')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:796
    old "Send ping packets timely to keep connection alive and calculate lag"
    new "Send ping packets timely to keep connection alive and calculate lag"
    # game/Submods/MAICA_ChatSubmod/header.rpy:841
    old "Session quality review: [persistent.maica_setting_dict.get('gen_quality_chk')]"
    new "Session quality review: [persistent.maica_setting_dict.get('gen_quality_chk')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:843
    old "Require MNerve to check generation quality after session exceeds 3 rounds.\n+ Quantitatively evaluate generation quality\n- Extra consumation of MNerve"
    new "Require MNerve to check generation quality after session exceeds 3 rounds.\n+ Quantitatively evaluate generation quality\n- Extra consumation of MNerve"
    # game/Submods/MAICA_ChatSubmod/header.rpy:985
    old "MVista images"
    new "MVista images"
    # game/Submods/MAICA_ChatSubmod/header.rpy:987
    old "View and manage MVista images.\n* Please read TOS carefully and be responsible for your own privacy"
    new "View and manage MVista images.\n* Please read TOS carefully and be responsible for your own privacy"
    # game/Submods/MAICA_ChatSubmod/header.rpy:995
    old "View and manage MVista images.\n! MVista not unlocked, please continue chatting with Monika patiently or send her letters"
    new "View and manage MVista images.\n! MVista not unlocked, please continue chatting with Monika patiently or send her letters"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1150
    old "Choose images | "
    new "Choose images | "
    # game/Submods/MAICA_ChatSubmod/header.rpy:1150
    old " chosen"
    new " chosen"
# TODO: Translation updated at 2025-12-05 19:39

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:581
    old "> Warning: current system 'non-unicode language' is not Chinese, expect possible encoding issues"
    new "> Warning: current system 'non-unicode language' is not Chinese, expect possible encoding issues"
# TODO: Translation updated at 2025-12-07 15:44

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:856
    old "Realtime post proceeding: [persistent.maica_setting_dict.get('pprt')]"
    new "Realtime post proceeding: [persistent.maica_setting_dict.get('pprt')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:858
    old "Enable backend sentence breaking and realtime post proceeding.\n* Suggested to enable in normal cases"
    new "Enable backend sentence breaking and realtime post proceeding.\n* Suggested to enable in normal cases"
# TODO: Translation updated at 2025-12-19 17:00

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:860
    old "Input language detection: [persistent.maica_setting_dict.get('input_lang_detect')]"
    new "Input language detection: [persistent.maica_setting_dict.get('input_lang_detect')]"
    # game/Submods/MAICA_ChatSubmod/header.rpy:862
    old "Raise a warning if input language is not target language.\n* Suggested to enable in normal cases"
    new "Raise a warning if input language is not target language.\n* Suggested to enable in normal cases"
# TODO: Translation updated at 2025-12-22 18:12

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:1167
    old "Quit{#maica_host_quit}"
    new "Quit{#maica_host_quit}"
# TODO: Translation updated at 2026-01-08 02:22

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:458
    old "MAICA: Provider applied, reconnecting"
    new "MAICA: Provider applied, reconnecting"
# TODO: Translation updated at 2026-01-30 23:25

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:979
    old "Each session stores and applies history context independently.\n* Set to 0 to disable context (single round conversation)\n! Current session same as MSpire session, may cause confusing behaviour"
    new "Each session stores and applies history context independently.\n* Set to 0 to disable context (single round conversation)\n! Current session same as MSpire session, may cause confusing behaviour"
    # game/Submods/MAICA_ChatSubmod/header.rpy:982
    old "! Current main session is set to same as MSpire session which may cause unexpected issues.\n! Please avoid setting these the same value (except 0) unless you literally understand what you're doing."
    new "! Current main session is set to same as MSpire session which may cause unexpected issues.\n! Please avoid setting these the same value (except 0) unless you literally understand what you're doing."
    # game/Submods/MAICA_ChatSubmod/header.rpy:1069
    old "Enable MSpire cache.\n* Does not take effect if MSpire session not 0\n* Enforces default super params"
    new "Enable MSpire cache.\n* Does not take effect if MSpire session not 0\n* Enforces default super params"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1076
    old "Enable MSpire cache.\n! MSpire session not 0, with which MSpire cache conflicts"
    new "Enable MSpire cache.\n! MSpire session not 0, with which MSpire cache conflicts"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1080
    old "Session MSpire uses.\n* Set to 0 to disable context (single round conversation)\n* MSpire will offer choice to continue if not 0\n! Currently same as main session, auto resetting disabled"
    new "Session MSpire uses.\n* Set to 0 to disable context (single round conversation)\n* MSpire will offer choice to continue if not 0\n! Currently same as main session, auto resetting disabled"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1086
    old "Session MSpire uses.\n* Set to 0 to disable context (single round conversation)\n* MSpire will offer choice to continue if not 0\n! This session resets before MSpire generation every time"
    new "Session MSpire uses.\n* Set to 0 to disable context (single round conversation)\n* MSpire will offer choice to continue if not 0\n! This session resets before MSpire generation every time"
    # game/Submods/MAICA_ChatSubmod/header.rpy:1087
    old "MSpire session"
    new "MSpire session"

translate spanish strings:

    old "> Warning: this is a {color=#ff0000}development build{/color} copy. {color=#ff0000}Stop using immediately{/color} if you're not MAICA official staff"
    new "> Warning: this is a {color=#ff0000}development build{/color} copy. {color=#ff0000}Stop using immediately{/color} if you're not MAICA official staff"

    old "Behavior preset: [maica_get_preset_name('behavior')]"
    new "Behavior preset: [maica_get_preset_name('behavior')]"
    old "Hyperparameter preset: [maica_get_preset_name('hyperparameter')]"
    new "Hyperparameter preset: [maica_get_preset_name('hyperparameter')]"
    old "These settings affect model and tool co-working behavior of MAICA.\n* Changing this preset will affect tools, enhancements and prompts around core model, together with time consumation\n! Do not modify unless you know what they exactly mean"
    new "These settings affect model and tool co-working behavior of MAICA.\n* Changing this preset will affect tools, enhancements and prompts around core model, together with time consumation\n! Do not modify unless you know what they exactly mean"
    old "These settings affect core model's performance.\n* Changing this preset will directly affect core model's inference and sampling procedure\n! Do not modify unless you know what they exactly mean"
    new "These settings affect core model's performance.\n* Changing this preset will directly affect core model's inference and sampling procedure\n! Do not modify unless you know what they exactly mean"
    old "* The remaining settings in this section are managed by presets.\n* Do not modify manually unless you know what they exactly mean"
    new "* The remaining settings in this section are managed by presets.\n* Do not modify manually unless you know what they exactly mean"
    old "Custom"
    new "Custom"
    old "Pure"
    new "Pure"
    old "Reduce prompt text to minimum, use almost no tool, only retain critical correction.\n+ Fastest, nearly shortest TTFT\n- Almost no external sense, no in-game action ability"
    new "Reduce prompt text to minimum, use almost no tool, only retain critical correction.\n+ Fastest, nearly shortest TTFT\n- Almost no external sense, no in-game action ability"
    old "Fluent"
    new "Fluent"
    old "No LLM intervention in pre-generation phase, use constant tools instead to reduce TTFT. Also reduced other tools.\n+ Relatively fast, nearly shortest TTFT\n* Limited external sense, has in-game action ability"
    new "No LLM intervention in pre-generation phase, use constant tools instead to reduce TTFT. Also reduced other tools.\n+ Relatively fast, nearly shortest TTFT\n* Limited external sense, has in-game action ability"
    old "Dexterous"
    new "Dexterous"
    old "Aggressive tending calibration based on default, exchanges stability and rarely used functions for average speed.\n+ Relatively fast, relatively short TTFT\n+ Normal external sense, has in-game action ability"
    new "Aggressive tending calibration based on default, exchanges stability and rarely used functions for average speed.\n+ Relatively fast, relatively short TTFT\n+ Normal external sense, has in-game action ability"
    old "Balanced (default)"
    new "Balanced (default)"
    old "Default behavior of MAICA. Field-tested balanced calibration, performs best overall in most cases.\n* Decent speed, decent TTFT\n+ Normal external sense, has in-game action ability"
    new "Default behavior of MAICA. Field-tested balanced calibration, performs best overall in most cases.\n* Decent speed, decent TTFT\n+ Normal external sense, has in-game action ability"
    old "Complete"
    new "Complete"
    old "Almost complete feature set of generation assistance enabled. May perform better under extreme circumstances, but normally just wasting time.\n- Slowest, longest TTFT\n+ Normal external sense, has in-game action ability"
    new "Almost complete feature set of generation assistance enabled. May perform better under extreme circumstances, but normally just wasting time.\n- Slowest, longest TTFT\n+ Normal external sense, has in-game action ability"
    old "Eager"
    new "Eager"
    old "Fixed seed, eager sampling.\n! Not recommended for normal cases"
    new "Fixed seed, eager sampling.\n! Not recommended for normal cases"
    old "Cautious"
    new "Cautious"
    old "Lower temperature.\n! Not recommended for normal cases"
    new "Lower temperature.\n! Not recommended for normal cases"
    old "Standard (default)"
    new "Standard (default)"
    old "Default super params of MAICA. Field-tested balanced calibration, performs best overall in most cases."
    new "Default super params of MAICA. Field-tested balanced calibration, performs best overall in most cases."
    old "Aggressive"
    new "Aggressive"
    old "Higher temperature.\n! Not recommended for normal cases"
    new "Higher temperature.\n! Not recommended for normal cases"
translate spanish strings:

    old "MAICA: Input is empty"
    new "MAICA: Input is empty"

    old "MAICA: Custom MFocus information has reached the 512-item limit"
    new "MAICA: Custom MFocus information has reached the 512-item limit"

    old "MAICA: A custom MFocus information item cannot exceed 1536 bytes"
    new "MAICA: A custom MFocus information item cannot exceed 1536 bytes"

    old "MAICA: Identical content already exists"
    new "MAICA: Identical content already exists"

    old "Reset chat session length"
    new "Reset chat session length"

    old "Write Event information to the log"
    new "Write Event information to the log"

    old "Push sentence-splitting test"
    new "Push sentence-splitting test"

    old "Push chat loop"
    new "Push chat loop"

    old "Push MSpire"
    new "Push MSpire"

    old "Push maica_mpostal_read"
    new "Push maica_mpostal_read"

    old "Push maica_mpostal_load"
    new "Push maica_mpostal_load"

    old "Push maica_raw_context_example"
    new "Push maica_raw_context_example"

    old "Show maica_gen_quality_chk_notify 0.3"
    new "Show maica_gen_quality_chk_notify 0.3"

    old "Show maica_gen_quality_chk_notify 0.6"
    new "Show maica_gen_quality_chk_notify 0.6"

    old "Show maica_gen_quality_chk_notify 0.9"
    new "Show maica_gen_quality_chk_notify 0.9"

translate spanish strings:

    # game/Submods/MAICA_ChatSubmod/header.rpy:1181
    old "> Warning: {color=#ff0000}certification corrupted{/color}, remove problematic extensions or clean install"
    new "> Warning: {color=#ff0000}certification corrupted{/color}, remove problematic extensions or clean install"
