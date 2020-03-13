<template>
    <v-container
        fluid
    >
        <v-layout>
            <v-flex
                xs10
                offset-xs1
            >
                <form-editar-area
                    :tipo="'criar'"
                    :texto-cabecalho="'Criação de área'"
                />
            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
import FormEditarArea from '../components/FormEditarArea';

export default {
    name: 'CriarArea',
    components: {
        FormEditarArea,
    },
};
</script>
