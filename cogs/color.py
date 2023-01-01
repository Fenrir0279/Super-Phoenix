import discord
import config
import vitals
import json

red_colors = {
    'indian_red': 0xCD5C5C,
    'light_coral': 0xF08080,
    'salmon': 0xFA8072,
    'dark_salmon': 0xE9967A,
    'crimson': 0xDC143C,
    'red': 0xFF0000,
    'fire_brick': 0xB22222,
    'dark_red': 0x8B0000,
}
pink_colors = {
    'pink': 0xFFC0CB,
    'light_pink': 0xFFB6C1,
    'hot_pink': 0xFF69B4,
    'deep_pink': 0xFF1493,
    'medium_violet_red': 0xC71585,
    'pale_violet_red': 0xDB7093
}
orange_colors = {
    'light_salmon': 0xFF07A,
    'coral': 0xFF7F50,
    'tomato': 0xFF6347,
    'orange_red': 0xFF4500,
    'dark_orange': 0xFF8C00,
    'orange': 0xFFA500
}
yellow_colors = {
    'gold': 0xFFD700,
    'yellow': 0xFFFF00,
    'light_yellow': 0xFFFFE0,
    'lemon_chiffon': 0xFFFACD,
    'light_goldenrod_yellow': 0xFAFAD2,
    'papaya_whip': 0xFFEFD5,
    'moccasin': 0xFFE4B5,
    'peach_puff': 0xFFDAB9,
    'pale_goldenrod': 0xEEE8AA,
    'khaki': 0xF0E68C,
    'dark_khaki': 0xBDB76B
}
purple_colors = {
    'lavender': 0xE6E6FA,
    'thistle': 0xD8BFD8,
    'plum': 0xDDA0DD,
    'violet': 0xEE82EE,
    'orchid': 0xDA70D6,
    'magenta': 0xFF00FF,
    'medium_orchid': 0xBA55D3,
    'medium_purple': 0x9370DB,
    'rebecca_purple': 0x663399,
    'blue_violet': 0x8A2BE2,
    'dark_violet': 0x9400D3,
    'dark_rochid': 0x9932CC,
    'dark_magenta': 0x8B008B,
    'purple': 0x800080,
    'indigo': 0x4B0082,
    'slate_blue': 0x6A5ACD,
    'dark_slate_blue': 0x483D8B
}
green_colors = {
    'green_yellow': 0xADFF2F,
    'chartreuse': 0x7FFF00,
    'lawn_green': 0x7CFC00,
    'lime': 0x00FF00,
    'lime_green': 0x32CD32,
    'pale_green': 0x98FB98,
    'light_green': 0x90EE90,
    'medium_spring_green': 0x00FA9A,
    'spring_green': 0x00FF7F,
    'medium_sea_green': 0x3CB371,
    'sea_green': 0x2E8B57,
    'forest_green': 0x228B22,
    'green': 0x008000,
    'dark_green': 0x006400,
    'yellow_green': 0x9ACD32,
    'olive_drab': 0x6B8E23,
    'olive': 0x808000,
    'dark_olive_green': 0x556B2F,
    'medium_aquamarine': 0x66CDAA,
    'dark_sea_green': 0x8FBC8B,
    'light_sea_green': 0x20B2AA,
    'dark_cyan': 0x008B8B,
    'teal': 0x008080
}
blue_colors = {
    'aqua': 0x00FFFF,
    'cyan': 0x00FFFF,
    'light_cyan': 0xE0FFFF,
    'pale_turquoise': 0xAFEEEE,
    'aquamarine': 0x7FFFD4,
    'turquoise': 0x40E0D0,
    'medium_turquoise': 0x48D1CC,
    'dark_turquoise': 0x00CED1,
    'cadet_blue': 0x5F9EA0,
    'steel_blue': 0x4682B4,
    'light_steel_blue': 0xB0C4DE,
    'powder_blue': 0xB0E0E6,
    'light_blue': 0xADD8E6,
    'sky_blue': 0x87CEEB,
    'light_sky_blue': 0x87CEFA,
    'deep_sky_blue': 0x00BFFF,
    'dodger_blue': 0x1E90FF,
    'cornflower_blue': 0x6495ED,
    'medium_slate_blue': 0x7B68EE,
    'royal_blue': 0x4169E1,
    'blue': 0x0000FF,
    'medium_blue': 0x0000CD,
    'dark_blue': 0x00008B,
    'navy': 0x000080,
    'midnight_blue': 0x191970
}
brown_colors = {
    'cornsilk': 0xFFF8DC,
    'blanched_almond': 0xFFEBCD,
    'bisque': 0xFFE4C4,
    'navajo_white': 0xFFDEAD,
    'wheat': 0xF5DEB3,
    'burly_wood': 0xDEB887,
    'tan': 0xD2B48C,
    'rosy_brown': 0xBC8F8F,
    'sandy_brown': 0xF4A460,
    'goldenrod': 0xDAA520,
    'dark_goldenrod': 0xB8860B,
    'peru': 0xCD853F,
    'chocolate': 0xD2691E,
    'saddle_brown': 0x8B4513,
    'sienna': 0xA0522D,
    'brown': 0xA52A2A,
    'maroon': 0x800000
}
white_colors = {
    'white': 0xFFFFFF,
    'snow': 0xFFFAFA,
    'honey_dew': 0xF0FFF0,
    'mint_cream': 0xF5FFFA,
    'azure': 0xF0FFFF,
    'alice_blue': 0xF0F8FF,
    'ghost_white': 0xF8F8FF,
    'white_smoke': 0xF5F5F5,
    'sea_shell': 0xFFF5EE,
    'beige': 0xF5F5DC,
    'old_lace': 0xFDF5E6,
    'floral_white': 0xFFFAF0,
    'ivory': 0xFFFFF0,
    'antique_white': 0xFAEBD7,
    'linen': 0xFAF0E6,
    'lavender_blush': 0xFFF0F5,
    'misty_rose': 0xFFE4E1,
}
gray_colors = {
    'gainsboro': 0xDCDCDC,
    'light_gray': 0xD3D3D3,
    'silver': 0xC0C0C0,
    'dark_gray': 0xA9A9A9,
    'gray': 0x808080,
    'dim_gray': 0x696969,
    'light_slate_gray': 0x778899,
    'slate_gray': 0x708090,
    'dark_slate_gray': 0x2F4F4F,
    'black': 0x000000
}

color_set = {
    'Red': red_colors,
    'Pink': pink_colors,
    'Orange': orange_colors,
    'Yellow': yellow_colors,
    'Purple': purple_colors,
    'Green': green_colors,
    'Blue': blue_colors,
    'Brown': brown_colors,
    'White': white_colors,
    'Gray': gray_colors
}

def unprocess(text):
    return "_".join(map(str.lower, text.split()))

class ColorEmbed(discord.Embed):
    def __init__(self, color=None, name=None):
        super().__init__(
            title=f'{name} (#{hex(color)[2:]:>06})' if color and name else 'No color chosen',
        )
        if color:
            self.color = color
            self.set_thumbnail(url=f'https://www.htmlcsscolor.com/preview/128x128/{hex(color)[2:]:>06}.png')

class ColorSelectView(discord.ui.View):
    def __init__(self, colors):
        super().__init__()
        self.colors = colors
        self.curr = None

        self.add_item(ColorSelect(self.colors))

    def __call__(self, color, name):
        self.curr = color, name
        return self

    @discord.ui.button(label='Back', emoji='🔙', style=discord.ButtonStyle.green, row=1)
    async def back(self, button, interaction):
        await interaction.response.edit_message(view=MasterColorSelect())

class ColorSelect(discord.ui.Select):
    def __init__(self, colors):
        self.colors = colors
        super(ColorSelect, self).__init__(options=self.proccess())

    def proccess(self):
        return [discord.SelectOption(label=k.replace('_', ' ').title()) for k in self.colors]

    async def callback(self, interaction: discord.Interaction):
        choice = self.values[0]
        items = self.colors[unprocess(choice)], choice
        await interaction.response.edit_message(embed=ColorEmbed(*items), view=self.view(*items))

class MasterColorSelect(discord.ui.View):
    def __init__(self):
        super(MasterColorSelect, self).__init__()

    @discord.ui.button(label='End Interaction', style=discord.ButtonStyle.red)
    async def end_interaction(self, button, interaction):
        self.disable_all_items()
        await interaction.response.edit_message(view=self)

    @discord.ui.select(options=[discord.SelectOption(label=i) for i in color_set], row=1)
    async def on_select(self, select, interaction):
        choice = select.values[0]
        await interaction.response.edit_message(
            embed=ColorEmbed(),
            view=ColorSelectView(color_set[choice])
        )

class Colors(discord.Cog):
    def __init__(self, client):
        self.client = client

    color = discord.SlashCommandGroup(name='color', description='Commands related to your embed color!')

    color_groups = ['Red', 'Pink', 'Orange', 'Yellow', 'Purple', 'Green', 'Blue', 'Brown', 'White', 'Gray']

    @color.command(name='view', description='View a certain color')
    async def view(self, ctx: discord.ApplicationContext, color: discord.Option(input_type=str, required=True, choices=color_groups)):
        await ctx.respond(view=ColorSelectView(color_set[color]), embed=ColorEmbed())

    @color.command(name='hexview', description='View the color corrosponding to a certain hex')
    async def hexview(self, ctx: discord.ApplicationContext, color: discord.Option(input_type=str, required=True)):
        await ctx.respond(view=MasterColorSelect(), embed=ColorEmbed(int(color, 16), 'Custom color'))

    @color.command(name='set', description='Set your embed color')
    async def set(self, ctx: discord.ApplicationContext, color: discord.Option(input_type=str, required=False, default=None)):
        if color is None or not color.startswith('#') or not all(c in 'abcdef1234567890' for c in color[1:]) or len(color) != 7:
            embed = discord.Embed(title='/color set', description='Here\'s how you use `/color set`', color=config.COLOR)
            embed.add_field(name='color', value='This is the hex code of the color you want. If it\'s the hex of an inbuilt color, this number can be found in the `/color view` of that color.\nExample: `#dc143c`')
            await ctx.respond(embed=embed, ephemeral=True)
            return

        is_registered = vitals.is_registered(ctx.user.id)
        if not is_registered:
            await ctx.respond(embed=vitals.UserNotRegistered(), ephemeral=True)
            return

        is_registered[str(ctx.user.id)]['color'] = int(color[1:], 16)
        with open(config.USER_FILES + 'users.json', 'w') as f:
            json.dump(is_registered, f, indent=4)

        await ctx.respond(f"Color updated to {color}!")

def setup(client):
    print(f'Loading cogs/colors.py')
    client.add_cog(Colors(client))

