%from bottle import request
%root = request.environ.get('SCRIPT_NAME')
<!DOCTYPE html>
<html>
    <head>
        <title>test app</title>
    </head>
    <body>
        <form method="POST" id="newcat" action="{{root}}/tanya">
            <input type="text" name="q" id="q" value="{{q}}"/>
            <input type="submit" name="ask" value="tanya"/>
        </form>
        <div id="result" style="width:500px;background-color:#ccc;float:left;padding:8px;">{{a}}<br/>
            {{d}}
        </div>
    </body>
</html>