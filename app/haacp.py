# --------------------------------------------------------------------------------------
# Description: This file contains the main function of the application.
# Author:      Larry W Jordan Jr
# --------------------------------------------------------------------------------------
# Importq
import os, sys, json, logging, time, datetime, uuid, random, asyncio, threading
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureTextCompletion, OpenAITextCompletion

kernel = sk.Kernel()

useAzureOpenAI = False

# Configure AI service used by the kernel
if useAzureOpenAI:
    deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
    kernel.add_text_completion_service("dv", AzureTextCompletion(deployment, endpoint, api_key))
else:
    api_key, org_id = sk.openai_settings_from_dot_env()
    kernel.add_text_completion_service("chat-gpt", OpenAITextCompletion("gpt-3.5-turbo", api_key, org_id))