<template>
    <v-container
        fluid
    >
        <v-layout>
            <v-flex
                xs10
                offset-xs1
            >
                <form-editar-especie
                    :texto-cabecalho="'Criação de espécie'"
                />
            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';
import FormEditarEspecie from '../components/FormEditarEspecie';

export default {
    name: 'CriarEspecie',
    components: {
        FormEditarEspecie,
    },
};
</script>
