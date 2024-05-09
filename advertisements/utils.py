from pyppeteer import launch
import asyncio


async def facebook_marketplace_vehicle_post(email, password, vehicle):
    # Launch chromium browser in the background
    browser = await launch({"headless": False, "args": ["--start-maximized"]})
    # Open a new tab in the browser
    page = await browser.newPage()

    try:
        # Navigate to the login page
        await page.goto("https://www.facebook.com/login")
        # Wait for the login form to appear
        await page.waitForSelector("input[name='email']")
        await page.waitForSelector("input[name='pass']")

        # Enter email and password
        await page.type("input[name='email']", email)
        await page.type("input[name='pass']", password)

        # Click on the login button
        await page.click("button[name='login']")

        # Wait for navigation to complete
        await page.waitForNavigation()
        # Ignore dialog request
        page.on("dialog", lambda dialog: asyncio.ensure_future(dialog.dismiss()))
        # Navigate to the Marketplace vehicle listing page
        await page.goto("https://www.facebook.com/marketplace/create/vehicle")
        page.on("dialog", lambda dialog: asyncio.ensure_future(dialog.dismiss()))
        # Vehicle type - tabindex = 0 = "Car/Truck"
        await page.click('[aria-label="Vehicle type"]')
        await page.click('[tabindex="0"]')
        print(vehicle.make)
        print(vehicle.model)
        print(vehicle.price)
        print("Listing created successfully!")
    except Exception as e:
        print(f"error: {e}")

    finally:
        # Close the browser
        await browser.close()
