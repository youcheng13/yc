const app = getApp()

Page({
  data: {
    punchList: [{
      "bannerUrl": "https://qiniu-image.qtshe.com/1536067857379_122.png"
    }, {
      "bannerUrl": "https://qiniu-image.qtshe.com/1536068379879_115.png",
    }, {
      "bannerUrl": "https://qiniu-image.qtshe.com/1536068319939_230.png",
    }, {
      "bannerUrl": "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1938730765,610435416&fm=26&gp=0.jpg",
    }, {
      "bannerUrl": "https://www.dious-f.com/UploadFiles/Others/20190624110631499940.jpg",
    }],
    current: 0
  },
  currentHandle(e) {
    let {
      current
    } = e.detail
    this.setData({
      current
    })
    console.log(e)//打印//
  },
  data:{
    bian:"a"
  },
  
})