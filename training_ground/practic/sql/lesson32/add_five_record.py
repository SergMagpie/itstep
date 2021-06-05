from base import engine, Session, Base
from cellphones import Phone
from processor import Processor


Base.metadata.create_all(engine)

session = Session()

processors = (
    Processor(
        name='Snapdragon 820',
        number_of_cores=4,
        clock_speed=2.2,
        manufacturer='Qualcomm'
    ),
    Processor(
        name='Apple A9',
        number_of_cores=2,
        clock_speed=1.85,
        manufacturer='Apple Inc.'

    ),
    Processor(
        name='Samsung Exynos 8890',
        number_of_cores=8,
        clock_speed=2.6,
        manufacturer='Samsung Electronics'

    ),
    Processor(
        name='Kirin 950',
        number_of_cores=8,
        clock_speed=2.4,
        manufacturer='HiSilicon'

    ),
    Processor(
        name='A14 Bionic',
        number_of_cores=6,
        clock_speed=11,
        manufacturer='Apple Inc.'

    )
)
phones = (
    Phone(
        company_manufacturer="Apple Inc.",
        model="Apple iPhone 12 Pro Max 512GB Pacific Blue",
        diagonal=6.7,
        price=52499,
        processor=5
    ),
    Phone(
        company_manufacturer="Google",
        model="Google Pixel 5 8/128GB Sorta Sage",
        diagonal=6,
        price=21999,
        processor=1
    ),
    Phone(
        company_manufacturer="Apple Inc.",
        model="Смартфон Apple iPhone SE 2020 64GB Black",
        diagonal=4.7,
        price=14599,
        processor=2
    ),
    Phone(
        company_manufacturer="Samsung Electronics",
        model="Смартфон Samsung Galaxy S21Ultra G998B 12GB/128GB Phantom Black",
        diagonal=4.7,
        price=14599,
        processor=3
    ),
    Phone(
        company_manufacturer="Huawei",
        model="Huawei P40 Lite Black",
        diagonal=6.4,
        price=6399,
        processor=4
    ),
)

session.add_all(processors)
session.add_all(phones)


session.commit()
session.close()
