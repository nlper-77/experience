# 开发经验总结

## 数据分析经验
## 模型选择
## 训练调参tricks

## 版本号命名规范
* [参考维基百科](https://zh.wikipedia.org/wiki/%E8%BB%9F%E4%BB%B6%E7%89%88%E6%9C%AC%E8%99%9F)

按小数命名一般格式： major.minor(.build)(a|b|rc)(1|2|3)

major是最大的版本编号，minor为其次，某些软件可能再细分作build，为更小的版本编号。

通常，正式版的版本编号为“1.0”。1.0以下的版本（0.x）为测试版，代表仍有一些重大错误（bugs），未正式推出。

在新版本推出时，应更新major、minor或是build（如有）的版号，决定于变更的大小。当有极大的更新时，会增加major的版号。而当有大更新，但不至于更新major时，会更新minor的版号。若更新比较小，例如只是修正错误，则会更新build的版号。以下是一个例子：
1.0→1.0.1→1.0.2→1.1→1.1.1→2.0→2.1→2.1.1→3.0→…
以上例子中，1.0至1.0.1至1.0.2、1.1至1.1.1、2.1至2.1.1都是小更新；1.0.2至1.1、2.0至2.1都是较大的更新；而1.1.1至2.0和2.1.1至3.0则是重大更新。

有时，小数版本号码后面会有“a”、“b”、“rc”等字样，代表某版本的测试版。“a”、“b”、“rc”分别代表“alpha”、“beta”和“release candidate”。（详见软件出版周期，软件版本周期）例如“2.0a”是2.0的alpha测试版，接着可能发布“2.0b”，是2.0的beta测试版。跟着，又可能出现“2.0b2”，代表2.0的第2个beta测试版。当beta测试完结后，又可能推出“2.0rc1”、“2.0rc2”两个版本，分别代表2.0的第一和第二个release candidate测试版。当一切测试结束后，就会有“2.0”正式版。