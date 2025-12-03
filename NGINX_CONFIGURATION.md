# Nginx 反向代理配置完成

## ✅ 配置完成

### 域名信息
- **域名**: whisperlivekit-enhanced.aws.xin
- **Nginx 服务器**: 107.172.39.47
- **后端服务器**: 44.193.212.118:8000
- **访问地址**: https://whisperlivekit-enhanced.aws.xin

---

## 📋 配置详情

### 1. HTTP 重定向到 HTTPS
```nginx
server {
    listen 80;
    server_name whisperlivekit-enhanced.aws.xin;
    return 301 https://$host$request_uri;
}
```

### 2. HTTPS 配置
```nginx
server {
    listen 443 ssl;
    server_name whisperlivekit-enhanced.aws.xin;
    
    # SSL 证书
    ssl_certificate /etc/nginx/aws.xin.pem;
    ssl_certificate_key /etc/nginx/aws.xin.pem;
    
    # SSL 协议和加密套件
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    
    # 安全头
    add_header Strict-Transport-Security "max-age=63072000" always;
    add_header X-Content-Type-Options nosniff;
    add_header X-Frame-Options DENY;
    add_header X-XSS-Protection "1; mode=block";
    
    # 密码认证
    auth_basic "Restricted Access";
    auth_basic_user_file /etc/nginx/.htpasswd;
    
    # 反向代理配置...
}
```

### 3. 反向代理路由

#### 主页和静态资源
```nginx
location / {
    proxy_pass http://44.193.212.118:8000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_buffering off;
    client_max_body_size 100M;
}
```

#### WebSocket 实时转录
```nginx
location /asr {
    proxy_pass http://44.193.212.118:8000;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_read_timeout 3600s;
    proxy_send_timeout 3600s;
}
```

#### REST API 文件转录
```nginx
location /api/transcribe {
    proxy_pass http://44.193.212.118:8000;
    proxy_read_timeout 300s;
    proxy_connect_timeout 300s;
    proxy_send_timeout 300s;
    client_max_body_size 100M;
}
```

#### 健康检查（无需认证）
```nginx
location /health {
    proxy_pass http://44.193.212.118:8000;
    auth_basic off;
}
```

#### API 文档
```nginx
location /docs {
    proxy_pass http://44.193.212.118:8000;
}
```

---

## 🔒 安全配置

### 密码认证
- ✅ 使用 HTTP Basic Auth
- ✅ 密码文件：`/etc/nginx/.htpasswd`
- ✅ 健康检查端点无需认证

### SSL/TLS
- ✅ 强制 HTTPS（HTTP 自动重定向）
- ✅ TLS 1.2 和 1.3
- ✅ 安全的加密套件
- ✅ HSTS 启用（2 年）

### 安全头
- ✅ X-Content-Type-Options: nosniff
- ✅ X-Frame-Options: DENY
- ✅ X-XSS-Protection: 1; mode=block
- ✅ Strict-Transport-Security

---

## ✅ 验证测试

### 1. 配置语法检查
```bash
sudo nginx -t
```
**结果**: ✅ 通过

### 2. Nginx 重载
```bash
sudo nginx -s reload
```
**结果**: ✅ 成功

### 3. 域名访问测试
```bash
curl -I https://whisperlivekit-enhanced.aws.xin
```
**结果**: ✅ 返回 401（需要认证，符合预期）

### 4. 健康检查（无需认证）
```bash
curl https://whisperlivekit-enhanced.aws.xin/health
```
**预期**: 返回健康状态 JSON

---

## 🌐 访问方式

### 浏览器访问
```
https://whisperlivekit-enhanced.aws.xin
```

**首次访问**：
1. 浏览器会提示输入用户名和密码
2. 输入正确凭据后即可访问
3. 凭据会被浏览器记住

### API 访问（带认证）
```bash
# 使用用户名密码
curl -u username:password https://whisperlivekit-enhanced.aws.xin/api/transcribe

# 或使用 Authorization header
curl -H "Authorization: Basic base64(username:password)" https://whisperlivekit-enhanced.aws.xin/
```

### 健康检查（无需认证）
```bash
curl https://whisperlivekit-enhanced.aws.xin/health
```

---

## 📊 配置总结

| 项目 | 配置 |
|------|------|
| 域名 | whisperlivekit-enhanced.aws.xin |
| 协议 | HTTPS（强制） |
| 认证 | HTTP Basic Auth |
| 后端 | 44.193.212.118:8000 |
| WebSocket | /asr（支持） |
| REST API | /api/transcribe |
| 文档 | /docs |
| 健康检查 | /health（无需认证） |
| 文件上传限制 | 100MB |
| WebSocket 超时 | 3600 秒 |
| API 超时 | 300 秒 |

---

## 🔧 管理命令

### 查看配置
```bash
ssh 107.172.39.47
sudo grep -A 60 "whisperlivekit-enhanced.aws.xin" /etc/nginx/nginx.conf
```

### 重载配置
```bash
ssh 107.172.39.47
sudo nginx -s reload
```

### 查看日志
```bash
ssh 107.172.39.47
sudo tail -f /var/log/nginx/access.log | grep whisperlivekit
sudo tail -f /var/log/nginx/error.log | grep whisperlivekit
```

---

## ✅ 完成确认

- [x] 备份原配置文件
- [x] 添加新域名配置
- [x] 配置 HTTP 到 HTTPS 重定向
- [x] 配置 SSL 证书
- [x] 配置密码认证
- [x] 配置反向代理（所有端点）
- [x] 配置 WebSocket 支持
- [x] 验证配置语法
- [x] 重载 Nginx
- [x] 测试域名访问

---

**状态**: ✅ 配置完成

**访问地址**: https://whisperlivekit-enhanced.aws.xin

**配置时间**: 2025-12-04 01:01
