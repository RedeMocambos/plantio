<template>
    <div id="app">
        <v-app>
            <div id="nav">
                <router-link to="/">Inicial</router-link> |
                <router-link to="/especies">Espécies</router-link> |
                <router-link to="/localidades">Localidades</router-link> |
                <router-link to="/areas">Áreas</router-link>
            </div>
            <router-view/>
        </v-app>
    </div>
</template>

<style>
#app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
}
#nav {
    padding: 30px;
}

#nav a {
    font-weight: bold;
    color: #2c3e50;
}

#nav a.router-link-exact-active {
    color: #42b983;
}
</style>
<script>

export default {
    name: 'App',
};
</script>
