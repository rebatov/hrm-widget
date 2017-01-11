/*
* @Author: bishal
* @Date:   2017-01-11 12:14:57
* @Last Modified by:   bishal
* @Last Modified time: 2017-01-11 18:07:29
*/

'use strict'
var webdriver = require('selenium-webdriver');
var browser = new webdriver.Builder().usingServer().withCapabilities({ 'browserName': 'phantomjs' }).build();
browser.manage().window().setSize(1920, 1080)
browser.get('http://hrm.javra.com/login');
// console.log(a);
browser.wait(
        webdriver.until.elementLocated(
            webdriver.By.xpath('//*[@id="username"]')), 15000);
browser.findElement(
        webdriver.By.xpath('//*[@id="username"]'))
    .sendKeys('bishald');
    browser.findElement(
        webdriver.By.xpath('//*[@id="password"]'))
    .sendKeys('ynwajft96');
browser.findElement(
	webdriver.By.xpath('//*[@id="testLogin"]/div/div/div/div[2]/form/div[3]/button')
	)
    .click();
browser.wait(
        webdriver.until.elementLocated(
            webdriver.By.className('today-date')), 15000);
browser.findElement(webdriver.By.css('#testDashboard > div > div.row.punctual.ng-scope > div > div.topBar > div > div:nth-child(3) > div > table > tbody > tr > td.today-date.ng-binding'))
.getAttribute('innerHTML').then(function(html){
	console.log(html);
})
browser.findElement(webdriver.By.xpath('//*[@id="testDashboard"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/ul/li[2]/p/label/span[1]'))
.getAttribute('innerHTML').then(function(html){
	console.log(html);
})
browser.quit();
//*[@id="password"]
//*[@id="testLogin"]/div/div/div/div[2]/form/div[3]/button
//*[@id="headDiv"]/div/div/div/div/table/tbody/tr/td[2]/h2/a