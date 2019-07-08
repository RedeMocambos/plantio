<template>
    <v-container
        fluid
    >
        <v-layout>
            <v-flex v-if="loading">
                <carregando
                    :text="'Carregando dados da edição'"
                />
            </v-flex>
            <v-flex
                v-else
                xs10
                offset-xs1
            >
                <form-editar-area
                />
            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
import _ from 'lodash';
import Carregando from '@/components/CarregandoVuetify';
import { mapActions, mapGetters } from 'vuex';
import FormEditarArea from '../components/FormEditarArea';

export default {
    name: 'EditarArea',
    components: {
        Carregando,
        FormEditarArea,
    },
    data() {
        return {
            loaded: {
                dados: false,
                metadados: false,
                localidades: false,
            },
            loading: true,
        };
    },
    computed: {
        ...mapGetters({
            dadosArea: 'area/area',
            listaLocalidades: 'localidade/localidades',
            getAreaMetadata: 'area/getAreaMetadata',
        }),
        id() {
            return this.$route.params.id;
        },
    },
    watch: {
        dadosArea() {
            if (this.dadosArea.id !== 'undefined') {
                this.loaded.dados = true;
            }
        },
        listaLocalidades() {
            this.loaded.localidades = true;
        },
        getAreaMetadata() {
            if (this.getAreaMetadata.id !== 'undefined') {
                this.loaded.metadados = true;
            }
        },
        loaded: {
            handler(value) {
                const fullyLoaded = _.keys(value).every(i => value[i]);
                if (fullyLoaded) {
                    this.loading = false;
                }
            },
            deep: true,
        },
    },
    created() {
        if (typeof this.$route.params.id !== 'undefined') {
            this.buscarArea(this.$route.params.id);
            this.buscarAreaMetadata();
            this.buscarLocalidades();
        }
    },
    methods: {
        ...mapActions({
            buscarArea: 'area/buscarArea',
            buscarAreaMetadata: 'area/buscarAreaMetadata',
            updateArea: 'area/updateArea',
            buscarLocalidades: 'localidade/buscarLocalidades',
        }),
    },
};
</script>
