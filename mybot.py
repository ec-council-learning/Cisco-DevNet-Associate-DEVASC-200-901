#pip install webex-bot
from webex_bot.webex_bot import WebexBot
from webex_bot.commands.echo import EchoCommand

from webex_bot.models.command import Command
import random
import json
from webexteamssdk.models.cards import Colors, TextBlock, FontWeight, FontSize, Column, AdaptiveCard, ColumnSet, \
	Text, Image, HorizontalAlignment
from webex_bot.models.response import response_from_adaptive_card

api_token = "your_token_here"


oracle_card =  json.loads('''
{
	"$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
	"type": "AdaptiveCard",
	"version": "1.2",
	"body": [
		{
			"type": "ColumnSet",
			"columns": [
				{
					"type": "Column",
					"width": 2,
					"items": [
						{
							"type": "TextBlock",
							"text": "Webex Oracle",
							"weight": "Bolder",
							"size": "Medium"
						},
						{
							"type": "TextBlock",
							"text": "Ask the Oracle a question and get an answer",
							"isSubtle": true,
							"wrap": true
						},
						{
							"type": "TextBlock",
							"text": "Ask about past, present or future. The Oracle sees everything",
							"isSubtle": true,
							"wrap": true,
							"size": "Small"
						},
						{
							"type": "TextBlock",
							"text": "Question",
							"wrap": true
						},
						{
							"type": "Input.Text",
							"id": "question",
							"placeholder": "Question"
						}
					]
				},
				{
					"type": "Column",
					"width": 1,
					"items": [
						{
							"type": "Image",
							"url": "https://images.pexels.com/photos/7179799/pexels-photo-7179799.jpeg"
						}
					]
				}
			]
		}
	],
	"actions": [
		{
			"type": "Action.Submit",
			"title": "Submit"
		}
	]
}
'''
)


class AskOracle(Command):
	def __init__(self):
		super().__init__(
			command_keyword="oracle",
			help_message="Ask your question to the Oracle.",
			card=oracle_card
		)

	def pre_execute(self, message, attachment_actions, activity):
		"""
		(optional function).
		Reply before running the execute function.

		Useful to indicate the bot is handling it if it is a long running task.

		:return: a string or Response object (or a list of either). Use Response if you want to return another card.
		"""

		return "Working on it ..."

	def execute(self, message, attachment_actions,activity):

		answers = ["Ask again later", "It is so","Do you really think it will work?","With great power comes great responsability","You will not know untill you try","Don't think so","I think you shouldn't do this","Most likely no",
		"You will certainly fail", "Follow your heart", "You already know the answer yourself", "The truth is in the wine"]

		answer = random.choice(answers)

		image = Image(url="https://previews.123rf.com/images/virtosmedia/virtosmedia2303/virtosmedia230307068/199448031-glowing-lightbulb-with-colorful-paint-splashes-on-dark-background.jpg")
		text1 = TextBlock("The Oracle answer is:", wrap=True, size=FontSize.DEFAULT, horizontalAlignment=HorizontalAlignment.CENTER, color=Colors.DARK)
		text2 = TextBlock(answer,wrap=True, weight=FontWeight.BOLDER, color=Colors.DARK)

		card = AdaptiveCard(
			body=[ColumnSet(columns=[Column(items=[image], width=2)]),
				  ColumnSet(columns=[Column(items=[text1, text2])]),
				  ])
		
		return response_from_adaptive_card(card)

bot = WebexBot(api_token)
bot.add_command(EchoCommand())
bot.add_command(AskOracle())
bot.run()