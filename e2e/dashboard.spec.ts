import { expect, test } from '@playwright/test'

test.describe('Dashboard', () => {
  test('loads with Dashboard heading', async ({ page }) => {
    await page.goto('/')
    await expect(page.getByRole('heading', { name: /Dashboard/i })).toBeVisible()
  })

  test('shows System Status section', async ({ page }) => {
    await page.goto('/')
    await expect(page.getByText('System Status')).toBeVisible()
  })

  test('shows KPI cards', async ({ page }) => {
    await page.goto('/')
    await expect(page.getByText('Posts This Week')).toBeVisible()
    await expect(page.getByText('Engagement Rate')).toBeVisible()
    await expect(page.getByText('Scheduled')).toBeVisible()
    await expect(page.getByText('Platforms')).toBeVisible()
  })
})
