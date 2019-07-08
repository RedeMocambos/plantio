<template>
    <v-container
        fluid
    >
        <v-layout>
            <v-flex v-if="dadosEspecie.id === 'undefined'">
                <carregando
                    :text="'Carregando dados da edição'"
                />
            </v-flex>
            <v-flex
                v-else
                xs10
                offset-xs1
            >
                <form-editar-especie
                />
            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
import Carregando from '@/components/CarregandoVuetify';
import { mapActions, mapGetters } from 'vuex';
import FormEditarEspecie from '../components/FormEditarEspecie';

export default {
    name: 'EditarEspecie',
    components: {
        Carregando,
        FormEditarEspecie,
    },
    data() {
        return {
        };
    },
    computed: {
        ...mapGetters({
            dadosEspecie: 'especie/especie',
            dadosEspecieMetadata: 'especie/getEspecieMetadata',
        }),
        id() {
            return this.$route.params.id;
        },
    },
    created() {
        if (typeof this.$route.params.id !== 'undefined') {
            this.buscarEspecie(this.$route.params.id);
            this.buscarEspecieMetadata();
        }
    },
    methods: {
        ...mapActions({
            buscarEspecie: 'especie/buscarEspecie',
            buscarEspecieMetadata: 'especie/buscarEspecieMetadata',
        }),
    },
};
</script>
