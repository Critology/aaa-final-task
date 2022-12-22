# Pizza project

You can order different pizzas 

Pizza choices:
- Pepperoni,
- Hawaiian,
- Margherita.

Size choices:
- L,
- XL.

## Menu
`python cli_pizza.py menu`

## Pizza baking commands
With delivery: `python cli.py order Margherita --delivery`\
Without delivery: `python cli.py order Hawaiian`\
You choose size: `python cli.py order Pepperoni --size=XL`

## Tests
To see tests coverage use command line :`python -m pytest --cov . --cov-report html `
