import { PwaMobileToolkitPage } from './app.po';

describe('pwa-mobile-toolkit App', () => {
  let page: PwaMobileToolkitPage;

  beforeEach(() => {
    page = new PwaMobileToolkitPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
