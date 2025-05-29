from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Bem-vindo à API Bookstore!</h1>
        <p>Escolha uma opção:</p>
        <ul>
            <li><a href="/admin/">Admin</a></li>
            <li><a href="/api-token-auth/">Token Auth</a></li>
            <li><a href="/bookstore/v1/">API v1</a></li>
            <li><a href="/bookstore/v2/">API v2</a></li>
        </ul>
    """)

def api_version_home(request, version):
    return HttpResponse(f"""
        <h1>API Bookstore {version}</h1>
        <p>Escolha uma opção:</p>
        <ul>
            <li><a href="/bookstore/{version}/order/">Order</a></li>
            <li><a href="/bookstore/{version}/product/">Product</a></li>
        </ul>
        <p><a href="/">Voltar para a página inicial</a></p>
    """)