from tortoise import Tortoise, run_async


async def migrate():
    await Tortoise.init(
        db_url="mysql://root:sanicpass@db:3306/sanic",
        modules={"models": ["models"]}
    )
    await Tortoise.generate_schemas()


run_async(migrate())