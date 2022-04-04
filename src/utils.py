import numpy as np
from colorama import Back, Style
import re

#dummy data to test the tool
wrappers = [{'name': 'univ3',
    'ipfs':'QmWNW25E3M23Uf4ftePoKopuoVtcUSz4DHKFqKfbsz7XBP'},
    {'name': 'ens',
    'ipfs':'QmRYP5qwQd7AotVbtcx7KhN8HuHX9DCg8sS9LVE4kstpVw'},
    {'name': 'gelato',
    'ipfs':'QmUQjJMmM9RLLAGRXuKs26ptKiX945M6cRQ96kRJQ4r7y1'},
    {'name':'pocket',
     'ipfs':'QmUQjJMmM9RLLAGRXuKs26ptKiX945M6cRQ96kRJQ4r7y1'},
    {'name':'defisdk',
     'ipfs':'QmPT3J6kgVW1p1uSMcENGfjNCEPR32nDTyYSbeSRh9huz8'},
    {'name':'pokemon',
     'ipfs':'QmUCSMoeMx2dL8BZWfwAuvgxhVJWQAFY1WV58ayMpEt1rn'},
    {'name':'near',
     'ipfs':'QmcaFhYgkpay8G1KSXgUfh6EzLDev4dAbjAsY3FP3ARXCW'},
    {'name':'dorg',
     'ipfs':'QmWtsvd4PdLBLx7KRkBPGwz2YMFmRNjqUk63EsdQYKEy63'},
    {'name':'gnosis',
     'ipfs':'QmSEbkfMGsCRAQp4Vkgy2oxKp2yDBZKPFBUeSuksCoDLjV'}
            
           ]

ipfs = ['QmQhXyMLvxbKPmZ2RzMJMeHTx5saUfHzZmVR9LDVJaB8Zq'
'QmRXSvBkQxHGTYjVnnQinBX7LTzFLY2MDDdSVHc9psPYik',
'QmWrGuQmTW5VqDwpJWXMDi6F5ZPMPA5xZDTaQbbLXZB36u',
'QmTmfruPVQ92XMZGxa3frLYiaMCVo6DA3ssg1r2UnJjdCa',
'QmRJHqXz951zBqE9W5hajm6DJ18c9DsHfGUi5BDj9DdBg1',
'QmYvaoynTeKeMJpw1YqCKD75d9JrxaSe5771eXCbtvkELB',
'QmQhXyMLvxbKPmZ2RzMJMeHTx5saUfHzZmVR9LDVJaB8Zq',
'QmUhuAcVdCHeA3gH36Nb9z839DM7Hf3iprY8EKeHvRMoDE',
'Qman1CcC2tjHfwFHWTKvhwfUUZBbUDvy8tnb8vzUgkC6eJ',
'QmXLvtPYDMvU78uGDXWz84FoDi6GzrFxCXNVUQ5GzneYa2',
'QmPbeAJUWexcK8gYfNmz6zNrUaDqBEQ4ca49Gkf28C2YXd',
'QmQVTE1tWzJoWvc5KmUMt25XjNfBNk9ZfmVzn8TWQHJdZA',
'QmdwCodsNt4nTcHeE4AHATfyYecMEtGQr9aNQbCAETNPLC',
'QmQYEnZqSuoDh5d7fZtM6LNzhpZizo4bLLsGKBRMDza3Wc',
'QmR3TuFuD2XqCRbyyGhnVSsCtQvSSNVHtgK75fJyTDE2Lj',
'QmXUQXwJ8eb8TjXvXJGYNGEjipKpDPUG933FTiakeD2UTE',
'QmcnrHegojMFqHkRhixazY67Zb9mSbMLv6sSxyDpUtnrQS',
'QmeiPWHe2ixfitcgjRwP5AaJD5R7DbsGhQNQwT4rFNyxx8',
'QmbQBGSp48NJamRRKcXn7utLSNBtWva7jphW64By37fZeq',
'QmSKW5RFjSibPQjyCXDm25VY5q9YuUuEFPYxUKtencUDBt',
'QmRYP5qwQd7AotVbtcx7KhN8HuHX9DCg8sS9LVE4kstpVw',
'QmUQjJMmM9RLLAGRXuKs26ptKiX945M6cRQ96kRJQ4r7y1',
'QmQW7vRg8aBdw6jGW3sPd2xYiQM5wEGc4Cd26T54QJxF9P',
'QmSEbkfMGsCRAQp4Vkgy2oxKp2yDBZKPFBUeSuksCoDLjV',
'QmPT3J6kgVW1p1uSMcENGfjNCEPR32nDTyYSbeSRh9huz8',
'QmWtsvd4PdLBLx7KRkBPGwz2YMFmRNjqUk63EsdQYKEy63',
'QmUCSMoeMx2dL8BZWfwAuvgxhVJWQAFY1WV58ayMpEt1rn',
'QmcaFhYgkpay8G1KSXgUfh6EzLDev4dAbjAsY3FP3ARXCW',
'QmSbWiGSuNbsTEcPfSF9uCWhgFXA9JHEt2ZsfwmxVJHHzP',
'QmRYqTwnA1nH2sqFzQjfHvrHupZ7nAAAburhNUs1GmvVKX',
'QmWNW25E3M23Uf4ftePoKopuoVtcUSz4DHKFqKfbsz7XBP']

def find_locations(n):
    """
    finds the coordinate of the number of wrappers desired

    TODO: Optimize with curves so it's more organic and not a normal distribution
    this shoudl be more evenly separated, they are getting stacked
    """
    return np.random.rand(n,2)

def test_re(txt):
    """
    Test a regular expression and should print the results
    still a WIP
    To run it, use something like test_re(cat_this("./schema.graphql"))
    """
    pattern = re.compile("(?=type Query\s)")     
    match = pattern.search(txt)
    if match:print(match.span())
    else: print(f"{match=}")
    return highlight_regex_matches(pattern, txt)

def color_variant(hex_color, brightness_offset=-10):
    """ takes a color like #87c95f and produces a lighter or darker variant
    credits: https://chase-seibert.github.io/blog/2011/07/29/python-calculate-lighterdarker-rgb-colors.html"""
    if len(hex_color) != 7:
        raise Exception("Passed %s into color_variant(), needs to be in #87c95f format." % hex_color)
    rgb_hex = [hex_color[x:x+2] for x in [1, 3, 5]]
    new_rgb_int = [int(hex_value, 16) + brightness_offset for hex_value in rgb_hex]
    new_rgb_int = [min([255, max([0, i])]) for i in new_rgb_int] # make sure new values are between 0 and 255
    # hex() produces "0x88", we want just "88"
    return "#" + "".join([hex(i)[2:] for i in new_rgb_int])

def cat_this(path):
    """"
    open text file in read mode
    """
    schema = open(path, "r")

    #read whole file to a string
    txt = schema.read()

    #close file
    schema.close()
    return txt

def wrap_me_up(wrappers, filename='sage',darken=10):
    """
    Takes an array of wrappers, analyzes the data, and saves them as a svg composition
    """
    
    w,h = 840, 420 #width height

    def compose_wrapper(wrapper):
        """
        Takes data from a wrapper in a dictionary and returns the circle, radial gradient and blur filters for the svg
        """
        x= int(re.findall(r"\d", wrapper['ipfs'])[0]) / 10
        wrapper_coordinates = find_locations(1)[0] # generate random location
        cx,cy,cr = wrapper_coordinates[0]*w*x, wrapper_coordinates[1]*w*x, w*x/3 #circle x and y position, as well as radius
        rgc = [cx-(cr/2),cy-(cr/2)] # radial gracdient center
        rgs = cr*2.75 # radial gradient scale
        blur_std = int(re.findall(r"\d", wrapper['ipfs'])[0])/1.5
        color_highlight = ''.join(re.findall(r"[A-Fa-f0-9]", wrapper['ipfs']))[-6:]   
        color_shadow = color_variant(f"#{color_highlight}", brightness_offset= -darken)
        print(f"{color_highlight=}, {color_shadow=}")

        circle  = f"""<circle cx="{cx}" cy="{cy}" r="{cr}" fill="url(#{wrapper['name']}_color)" filter="url(#{wrapper['name']}_filters)" />"""
        defs = f"""<radialGradient id="{wrapper['name']}_color" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse"
            gradientTransform="translate({rgc[0]} {rgc[1]}) 
                scale({rgs})">
            <stop offset="0.04204206969691337" stop-color="#{color_highlight}" />
            <stop offset="0.7" stop-color="{color_shadow}" />
        </radialGradient>
        
        <filter id="{wrapper['name']}_filters" x="0" y="0" width="{w}" height="{h}" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
            <feFlood flood-opacity="0" result="BackgroundImageFix"/>
            <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
            <feGaussianBlur stdDeviation="{blur_std}" result="effect1_foregroundBlur_1773_341"/>
        </filter>
        """
        return circle, defs

    #now iterate over the wrappers to create the composition
    circles, defs = [], []
    print(wrappers)
    for wrapper in wrappers:
        shape, props = compose_wrapper(wrapper)
        circles.append(shape)
        defs.append(props)

    #set out the svg document structure 
    svg = f"""
    <svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" fill="none" xmlns="http://www.w3.org/2000/svg">
        {' '.join(circles)}
        <defs>
            {' '.join(defs)}
        </defs>
    </svg>"""
    svg_file = open(f"{filename}.svg", "w")
    n = svg_file.write(svg)
    svg_file.close()
    return "you're wrapped"

# def highlight_regex_matches(pattern, text, print_output=True):
#     """
#     Credits to : https://github.com/nikhilkumarsingh/RegEx-In-Python/blob/master/utils.py
#     """
# 	output = text
# 	len_inc = 0
# 	for match in pattern.finditer(text):
# 		start, end = match.start() + len_inc, match.end() + len_inc
# 		output = output[:start] + Back.YELLOW + Style.BRIGHT + output[start:end] + Style.RESET_ALL + output[end:]
# 		len_inc = len(output) - len(text)  

# 	if print_output:
# 		print(output)
# 	else:
# 		return output

