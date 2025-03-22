# 网易云音乐链接解析插件

## 一、插件信息
- **名称**：网易云音乐链接解析插件
- **功能**：自动解析网易云音乐歌曲链接中的 `id`、`userid` 和 `dlt` 参数并发送到群聊

## 二、核心功能
1. **链接监听**：实时检测群消息中的网易云音乐链接
2. **参数提取**：从链接中提取以下参数：
   - `id`（歌曲ID）
   - `userid`（用户ID）
   - `dlt`（设备类型标识）
3. **结果回传**：将解析结果格式化为文本消息发送到原群

## 三、使用示例
### 输入链接：https://y.music.163.com/m/song?id=00000&userid=0000&dlt=000
### 输出结果：解析结果：id=00000, userid=0000, dlt=000