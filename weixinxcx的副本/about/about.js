Page({
  tapname(event) {
    console.log(enen) //打印
  },

  zongcaiBtn: function (options) {
    wx.navigateTo({
      url: '../zongcai/zongcai',
    })
  },
  jingliBtn: function (options) {
    wx.navigateTo({
      url: '../jingli/jingli',
    })
  },
  gongquBtn: function (options) {
    wx.navigateTo({
      url: '../gongqu/gongqu',
    })
  },
  yiziBtn: function (options) {
    wx.navigateTo({
      url: '../yizi/yizi',
    })
  },



  pinpaiBtn: function(options) {
    wx.navigateTo({
      url: '../jianjie/jianjie',
    })
  },
  shangchengBtn: function(options) {
    wx.navigateTo({
      url: '../shangcheng/shangcheng',
    })
  },
  lianxiBtn: function(options) {
    wx.navigateTo({
      url: '../lianxi/lianxi',
    })
  },
})