import asyncio
import aiofiles
from playwright.async_api import async_playwright, expect

EXTENSIONS_PATH = f"PATH_TO_METAMASK_FOLDER"
MM_PASSWORD = "B7601As5T78"
SEED_PHRASE = ["food", "report", "vanish", "faint", "gown", "expose", "please", "mandate", "birth", "elegant", "find",
               "cotton"]


async def write_file(filename, seed, text):
    async with aiofiles.open(filename, mode='a') as f:
        await f.write(seed + " - " + text + '\n')


async def switch_to_last_page(pages):
    last_page = pages[-1]
    await last_page.bring_to_front()


async def main(seed_phrase):
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            '',
            headless=False,
            args=[
                f"--disable-extensions-except={EXTENSIONS_PATH}",
                f"--load-extension={EXTENSIONS_PATH}"
            ],
        )

        if len(context.background_pages) == 0:
            background_page = await context.wait_for_event('backgroundpage')
        else:
            background_page = await context.background_pages[0]

        titles = [await p.title() for p in context.pages]
        while "MetaMask" not in titles:
            titles = [await p.title() for p in context.pages]

        mm_page = context.pages[1]
        await mm_page.wait_for_load_state()

        await asyncio.sleep(3)
        checkbox = mm_page.locator('//*[@id="onboarding__terms-checkbox"]')
        await mm_page.wait_for_load_state(state='domcontentloaded')
        await checkbox.click()

        import_wallet = mm_page.get_by_test_id(test_id="onboarding-import-wallet")
        await expect(import_wallet).to_be_enabled()
        await import_wallet.click()

        i_dont_agree = mm_page.get_by_test_id(test_id="metametrics-no-thanks")
        await expect(i_dont_agree).to_be_enabled()
        await i_dont_agree.click()

        for i in range(12):
            await mm_page.get_by_test_id(test_id=f'import-srp__srp-word-{i}').fill(seed_phrase[i])

        confirm_seed = mm_page.get_by_test_id(test_id="import-srp-confirm")
        await expect(confirm_seed).to_be_enabled()
        await confirm_seed.click()

        await mm_page.get_by_test_id(test_id='create-password-new').fill(MM_PASSWORD)
        await mm_page.get_by_test_id(test_id='create-password-confirm').fill(MM_PASSWORD)
        terms_button = mm_page.get_by_test_id(test_id="create-password-terms")
        await expect(terms_button).to_be_enabled()
        await terms_button.click()

        terms_button_2 = mm_page.get_by_test_id(test_id="create-password-import")
        await expect(terms_button_2).to_be_enabled()
        await terms_button_2.click()

        terms_button_3 = mm_page.get_by_test_id(test_id="onboarding-complete-done")
        await expect(terms_button_3).to_be_enabled()
        await terms_button_3.click()

        terms_button_4 = mm_page.get_by_test_id(test_id="onboarding-complete-done")
        await expect(terms_button_4).to_be_enabled()
        await terms_button_4.click()

        terms_button_5 = mm_page.get_by_test_id(test_id="pin-extension-next")
        await expect(terms_button_5).to_be_enabled()
        await terms_button_5.click()

        terms_button_6 = mm_page.get_by_test_id(test_id="pin-extension-done")
        await expect(terms_button_6).to_be_enabled()
        await terms_button_6.click()

        await mm_page.click(
            'body > div.mm-modal.mm-modal__custom-scrollbar.mm-smart-transactions-opt-in-modal > div:nth-child(3) > div > section > div > button.mm-box.mm-text.mm-button-base.mm-button-base--size-md.mm-button-primary.mm-text--body-md-medium.mm-box--margin-top-8.mm-box--padding-0.mm-box--padding-right-4.mm-box--padding-left-4.mm-box--display-inline-flex.mm-box--justify-content-center.mm-box--align-items-center.mm-box--width-full.mm-box--color-primary-inverse.mm-box--background-color-primary-default.mm-box--rounded-pill')

        await mm_page.goto("https://personajourney.io/")
        await asyncio.sleep(10)

        await mm_page.click("body > div > div.css-zqcg1r > div.content.css-sf4vl0 > div:nth-child(3) > button > div")
        await asyncio.sleep(10)

        await mm_page.click(
            "body > div:nth-child(27) > div > div > div._9pm4ki5.ju367va.ju367v15.ju367v8r > div > div > div > div > div.iekbcc0.ju367va.ju367v15.ju367v4y._1vwt0cg3 > div.iekbcc0.ju367v6p._1vwt0cg2.ju367v7a.ju367v7v > div.iekbcc0.ju367va.ju367v15.ju367v1n > div:nth-child(3) > button > div > div > div:nth-child(2) > div")
        await asyncio.sleep(5)

        pages = context.pages
        mm_page = context.pages[-1]
        await switch_to_last_page(pages)
        await asyncio.sleep(5)

        terms_button_7 = mm_page.get_by_test_id(test_id="page-container-footer-next")
        await expect(terms_button_7).to_be_enabled()
        await terms_button_7.click()

        await asyncio.sleep(5)

        terms_button_8 = mm_page.get_by_test_id(test_id="page-container-footer-next")
        await expect(terms_button_8).to_be_enabled()
        await terms_button_8.click()

        await asyncio.sleep(5)

        mm_page = context.pages[1]
        await mm_page.wait_for_load_state()
        await asyncio.sleep(5)

        await mm_page.click(
            'body > div:nth-child(27) > div > div > div._9pm4ki5.ju367va.ju367v15.ju367v8r > div > div > div > div > div.iekbcc0.ju367v8i.ju367v6r.ju367v7a.ju367v7v.ju367v4.ju367va.ju367v15.ju367v1x > div.iekbcc0.ju367v4.ju367va.ju367v15.ju367v1q.ju367v9f > button.iekbcc0.iekbcc9.ju367v77.ju367v7s.ju367v88.ju367v6h.ju367vc6.ju367vt.ju367vv.ju367vm.ju367v8.ju367v2u.ju367v8v.ju367v9i.ju367v2b._12cbo8i3.ju367v8r._12cbo8i4._12cbo8i7 > div')
        await asyncio.sleep(5)

        pages = context.pages
        mm_page = context.pages[-1]
        await switch_to_last_page(pages)
        await asyncio.sleep(5)

        terms_button_8 = mm_page.get_by_test_id(test_id="page-container-footer-next")
        await expect(terms_button_8).to_be_enabled()
        await terms_button_8.click()
        await asyncio.sleep(3)

        mm_page = context.pages[1]
        await mm_page.wait_for_load_state()

        await mm_page.goto("https://personajourney.io/quests")
        await mm_page.wait_for_load_state(state='domcontentloaded')

        await asyncio.sleep(5)

        elements = await mm_page.query_selector_all('.css-137r5hr')
        for el in elements:
            await el.click()
            await asyncio.sleep(3)
        points = await mm_page.query_selector('.css-l4axle')
        seed_to_string = " ".join(seed_phrase)
        await write_file("results.txt", seed_to_string, await points.text_content())

        elements = await mm_page.query_selector_all(".css-137r5hr")
        for element in elements:
            await element.click()
            await asyncio.sleep(1)

        await asyncio.sleep(10)

        await context.close()


if __name__ == "__main__":
    with open('file.txt', 'r') as file:
        data = [line.strip() for line in file.readlines()]

    for line in data:
        seed = line.split()
        asyncio.run(main(seed))
