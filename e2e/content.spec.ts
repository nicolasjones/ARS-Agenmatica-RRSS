import { expect, test } from '@playwright/test'

test.describe('Content page', () => {
  test('renders Content heading', async ({ page }) => {
    await page.goto('/content')
    await expect(page.getByRole('heading', { name: /Content/i })).toBeVisible()
  })

  test('shows content management placeholder text', async ({ page }) => {
    await page.goto('/content')
    await expect(page.getByText(/Content generation/i)).toBeVisible()
  })
})
