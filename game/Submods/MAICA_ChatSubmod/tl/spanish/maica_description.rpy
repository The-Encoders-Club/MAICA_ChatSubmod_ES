translate spanish python:

    import maica_instance

    maica_instance.MaicaAiStatus.STATUS_MESSAGES.update({
        maica_instance.MaicaAiStatus.IDLE: "MAICA está inactiva actualmente",
        maica_instance.MaicaAiStatus.WAIT_AVAILABILITY: "Comprobando la disponibilidad del servicio",
        maica_instance.MaicaAiStatus.WEBSOCKET_CONNECTING: "Conectando WebSocket (esto debería completarse pronto)",
        maica_instance.MaicaAiStatus.CONNECTED: "MAICA está conectada y lista",
        maica_instance.MaicaAiStatus.TOKEN_MISSING: "Aún no se ha configurado un token",
        maica_instance.MaicaAiStatus.TOKEN_CORRUPTED: "El token está dañado",
        maica_instance.MaicaAiStatus.TOKEN_INVALID: "Usuario o contraseña no válidos",
        maica_instance.MaicaAiStatus.LOGIN_BLOCKED: "El inicio de sesión está bloqueado temporalmente",
        maica_instance.MaicaAiStatus.ACCOUNT_BANNED: "La cuenta ha sido suspendida",
        maica_instance.MaicaAiStatus.EMAIL_UNVERIFIED: "El correo de la cuenta aún no ha sido verificado",
        maica_instance.MaicaAiStatus.TOS_UNACCEPTED: "Aún no has aceptado los Términos de Servicio más recientes",
        maica_instance.MaicaAiStatus.CONNECTION_REUSE_DENIED: "Ya existe una conexión activa para esta cuenta",
        maica_instance.MaicaAiStatus.SERVER_REJECTED: "Ocurrió un error a nivel de usuario",
        maica_instance.MaicaAiStatus.SERVER_ERROR: "Ocurrió un error a nivel del servidor",
        maica_instance.MaicaAiStatus.TOKEN_GENERATION_FAILED: "Error al generar el token",
        maica_instance.MaicaAiStatus.CONNECT_PROBLEM: "No se puede conectar al servidor, revisa tu conexión y submod_log",
        maica_instance.MaicaAiStatus.RESPONSE_INVALID: "La respuesta del servidor no es válida",
        maica_instance.MaicaAiStatus.SERVER_MAINTAIN: "El servidor está en mantenimiento, por favor espera los próximos avisos",
        maica_instance.MaicaAiStatus.CERTIFI_BROKEN: "SSL/TLS está dañado, posiblemente por otro submod. Se requiere reinstalar MAS",
        maica_instance.MaicaAiStatus.FAILED_GET_NODE: "Error al obtener el nodo del servicio; el servidor podría estar en mantenimiento o desconectado",
        maica_instance.MaicaAiStatus.VERSION_OLD: "Se detectó una versión instalada obsoleta, por favor actualiza a la más reciente",
        maica_instance.MaicaAiStatus.NO_INTERNET: "Submod desconectado. Por favor revisa tu instalación y conexión según el Readme",
        maica_instance.MaicaAiStatus.CERTIFI_RESTART_REQUIRED: "Se realizó una reparación de certificados, por favor reinicia para aplicar los cambios",
    })

    import mas_topics

    mas_topics.event_database["maica_heaven_forest"].prompt = "Vamos al Bosque del Cielo"
    mas_topics.event_database["maica_heaven_forest"].category = ["Tú", "Nosotros", "Submods", "MAICA"]

    mas_topics.event_database["maica_pre_set_location"].prompt = "Cambiar la ubicación de [player]"
    mas_topics.event_database["maica_pre_set_location"].category = ["Tú", "Nosotros", "Submods", "MAICA"]

    mas_topics.event_database["maica_pre_set_preferences"].prompt = "Cambiar las preferencias de [player]"
    mas_topics.event_database["maica_pre_set_preferences"].category = ["Tú", "Nosotros", "Submods", "MAICA"]

    mas_topics.event_database["maica_pre_heaven_forest_what"].prompt = "¿Qué es exactamente el Bosque del Cielo?"
    mas_topics.event_database["maica_pre_heaven_forest_what"].category = ["Tú", "Nosotros", "Submods", "MAICA"]

    mas_topics.event_database["maica_wants_location"].prompt = "Acerca de la ubicación de [player]"
    mas_topics.event_database["maica_wants_location"].category = ["Tú", "Nosotros", "Submods", "MAICA"]

    mas_topics.event_database["maica_wants_preferences"].prompt = "Acerca de las preferencias de [player]"
    mas_topics.event_database["maica_wants_preferences"].category = ["Tú", "Nosotros", "Submods", "MAICA"]

    mas_topics.event_database["maica_pre_wants_mspire"].prompt = "Acerca de 'MSpire'"
    mas_topics.event_database["maica_pre_wants_mspire"].category = ["Tú", "Nosotros", "Submods", "MAICA"]

    mas_topics.event_database["maica_pre_wants_mpostal"].prompt = "Acerca de 'MPostal'"
    mas_topics.event_database["maica_pre_wants_mpostal"].category = ["Tú", "Nosotros", "Submods", "MAICA"]

    mas_topics.event_database["maica_pre_wants_mvista"].prompt = "Acerca de 'MVista'"
    mas_topics.event_database["maica_pre_wants_mvista"].category = ["Tú", "Nosotros", "Submods", "MAICA"]

    mas_topics.event_database["maica_pre_heaven_forest_sce"].prompt = "Acerca de HeavenForest.sce"
    mas_topics.event_database["maica_pre_heaven_forest_sce"].category = ["Tú", "Nosotros", "Submods", "MAICA"]

    import maica_provider_manager as mpm

    mpm.MAICAProviderManager._isfailedresponse.update(
        {
            "name": "ERROR: No se pudo obtener la información del nodo.",
            "description": "Consulta el registro de actualizaciones para ver el estado actual del servicio, o revisa submod_log.log para conocer el motivo del fallo.",
            "isOfficial": False,
            "portalPage": "https://forum.monika.love/d/3954",
            "servingModel": "Consulta el registro de actualizaciones para ver el estado actual del servicio, o revisa submod_log.log para conocer el motivo del fallo.",
            "modelLink": "",
            "wsInterface": "wss://maicadev.monika.love/websocket",
            "httpInterface": "https://maicadev.monika.love/api"
        }
    )
    mpm.MAICAProviderManager._fakelocalprovider.update(
        {
            "name": "Despliegue local",
            "description": "Selecciona este nodo cuando dispongas de un despliegue local operativo.",
            "isOfficial": False,
            "portalPage": "https://github.com/PencilMario/MAICA",
            "servingModel": "None",
            "modelLink": "",
            "wsInterface": "ws://127.0.0.1:5000",
            "httpInterface": "http://127.0.0.1:6000",
        }
    )
