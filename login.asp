<html>
	<head>
		<link href="/css_js/histyle.css" rel="stylesheet" type="text/css">
		<script>
		function checkform()
		{
			var form=document.regform;
			
			if(!form.id.value) {
				alert("아이디를 입력하세요");
				form.id.focus();
				return false;
			}  	
			if(!form.pwd.value)	{
				alert("비밀번호를 입력하세요");
				form.pwd.focus();
				return false;
			}
			
			if(form.gubun[0].checked){
				form.action = "LoginProc.asp"
			}else{
				form.action = "/serviceCompany/LoginProc.asp"
			}
			
			form.submit();
			
			//window.open('/UbiLocker_Center.html','','fullscreen');
		}	
		function loginBtn()
		{
			if (event.keyCode == 13){
				checkform();
				}
		}		
	</script>	
	</head>
	<body onload="document.regform.id.focus();">

<form name="regform" method="post">				
		<table cellpadding="0" cellspacing="0" border="0" align="center" width="360">
			<tr height="60"><td></td></tr>
			<tr><td><img src="/images/login/title_logo.gif" WIDTH="152" HEIGHT="31"></td></tr>
		</table>
				
		<table cellpadding="0" cellspacing="0" border="0" align="center" width="360">
			<tr>
				<td><img src="/images/login/title_login.gif" WIDTH="362" HEIGHT="128"></td>
			</tr>			
		</table>
		
		<table cellpadding="0" cellspacing="0" border="0" align="center" width="360">			
			
		</table>
		
		<table cellpadding="0" cellspacing="0" border="0" align="center" width="361" BGCOLOR="#ffffff">		
			<tr>
				<td width="6" background="/images/login/login_bar.gif"></td>
				<td colspan=5 style="padding:0 0 10 35">
					<input type=radio name="gubun" checked>운영자 및 관리자	
					<input type=radio name="gubun">서비스업체					
				</td>
				<td width="6" background="/images/login/login_bar.gif"></td>
			</tr>				
			<tr> 
				<td ROWSPAN="2" width="6" background="/images/login/login_bar.gif"></td>
				<td rowspan="2" WIDTH="41"></td>
				<td>아이디</td>
				<td>&nbsp;&nbsp;<input type="text" name="id" size="18" tabindex="1" onblur="document.regform.pwd.focus();"></td>
				<td rowspan="2" WIDTH="57">
				<a href="#" onclick="javacsript:checkform();" tabindex="3" border="1"><img src="/images/login/login_btn.gif"   onClick="" style="cursor:hand;" WIDTH="57" HEIGHT="41" border="0"></a>
				<!--<input type="image"  name="accept" onClick="javacsript:checkform();" style="cursor:hand;" src="/images/login/login_btn.gif" WIDTH="57" HEIGHT="41">-->
				</td>
				<td rowspan="2" WIDTH="40"></td>
				<td ROWSPAN="2" width="6" background="/images/login/login_bar.gif"></td>
			</tr>
			<tr> 
				<td WIDTH="50">패스워드</td>
				<td WIDTH="161">&nbsp;&nbsp;<input type="password" name="pwd" size="19" tabindex="2" onKeypress="loginBtn();"></td>
			</tr>
		</table>
		<table cellpadding="0" cellspacing="0" border="0" align="center" width="361" height="68" BACKGROUND="/images/login/login_bottom.gif">
			<tr HEIGHT="30"><td></td></tr>
			<tr>
				<td ALIGN="CENTER">					
					<!--<a href="#">아이디찾기</a>
					&nbsp;&nbsp;│&nbsp;&nbsp;<a href="#">비밀번호찾기</a>-->
				</td>
			</tr>
		</table>
</form>		

	</body>
</html>	
 

