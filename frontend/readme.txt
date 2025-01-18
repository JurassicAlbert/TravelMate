1. Sprawdź instalację Node.js. Upewnij się, że masz zainstalowane Node.js i npm (Node Package Manager):
Uruchom w terminalu:
    bash
        node -v
        npm -v
Powinno wyświetlić się coś w rodzaju:
    scss
        v18.15.0  (przykład dla Node.js)
        9.5.0     (przykład dla npm)
Jeśli Node.js nie jest zainstalowany, pobierz go z nodejs.org i zainstaluj wersję LTS.

2. Zainstaluj Vue CLI globalnie przy użyciu npm:
    bash
        npm install -g @vue/cli
Po instalacji sprawdź, czy Vue CLI działa:
    bash
        vue --version

3. Utworzenie katalogu dla frontendu: W głównym katalogu projektu (TravelMate) utwórz nowy katalog o nazwie frontend, w którym będzie znajdować się aplikacja Vue.js.
    bash
        cd TravelMate
        mkdir frontend
        cd frontend
4. Inicjalizacja projektu Vue.js: W katalogu frontend zainicjuj nowy projekt Vue.js.
    bash
        vue create .

Podczas konfiguracji wybierz odpowiednie opcje, takie jak integracja z routerem Vue.

Opcje konfiguracji Vue CLI

Default ([Vue 3] babel, eslint)
    Tworzy projekt oparty na Vue 3.
    Domyślnie dodaje Babel (transpiler JS) oraz ESLint (narzędzie do lintingu kodu).
    Polecana opcja, jeśli chcesz szybko zacząć pracę z najnowszą wersją Vue.

Default ([Vue 2] babel, eslint)
    Tworzy projekt oparty na Vue 2.
    Używaj tej opcji tylko, jeśli musisz pracować z wcześniejszą wersją Vue (np. w przypadku ograniczeń kompatybilności z bibliotekami lub backendem).

Manually select features
    Pozwala ręcznie wybrać dodatkowe funkcje, takie jak:
    Router: Do obsługi nawigacji między stronami.
    Vuex/Pinia: Do zarządzania stanem aplikacji.
    CSS Pre-processors: Jak Sass, Less lub Stylus.
    Testing: Konfiguracja testów jednostkowych lub e2e.
    Wybierz tę opcję, jeśli chcesz dostosować projekt do swoich potrzeb.

5. Po wyborze konfiguracji Vue CLI rozpocznie instalację zależności.
Po zakończeniu instalacji uruchomić projekt:
    bash
        npm run serve
Projekt będzie dostępny pod adresem http://localhost:8080


Jeśli brakuje dodatkowych zależności należy je zainstalować:
Brakuje dwóch podstawowych pakietów:
    axios – do wykonywania żądań HTTP.
    vue-router – do zarządzania nawigacją w Vue.
Uruchom poniższe polecenia w katalogu projektu frontend:
    bash
        npm install axios vue-router