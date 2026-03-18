import { expect, test } from '@playwright/test'

const routes = [
  { path: '/', label: 'Dashboard' },
  { path: '/content', label: 'Content' },
  { path: '/calendar', label: 'Calendar' },
  { path: '/analytics', label: 'Analytics' },
  { path: '/engagement', label: 'Engagement' },
  { path: '/settings', label: 'Settings' },
]

test.describe('Navigation', () => {
  test('sidebar renders all nav links', async ({ page }) => {
    await page.goto('/')
    for (const route of routes) {
      await expect(page.getByRole('link', { name: new RegExp(route.label, 'i') })).toBeVisible()
    }
  })

  for (const route of routes) {
    test(`navigates to ${route.label} page`, async ({ page }) => {
      await page.goto('/')
      await page.getByRole('link', { name: new RegExp(route.label, 'i') }).click()
      await expect(page).toHaveURL(route.path)
      await expect(page.getByRole('heading', { name: new RegExp(route.label, 'i') })).toBeVisible()
    })
  }
})
